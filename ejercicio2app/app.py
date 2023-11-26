from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Modelo de Usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    folders = db.relationship('Folder', backref='user', lazy=True)

# Modelo de Documento
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text)
    access_log = db.relationship('AccessLog', backref='document', lazy=True)

# Modelo de Carpeta
class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    documents = db.relationship('Document', backref='folder', lazy=True)

# Modelo de Registro de Acceso
class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)

# Patrón Composite
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.content = ""
        self.access_log = []

    def get_info(self):
        return f"Document: {self.name}, Type: {self.type}, Size: {self.size}"

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def log_access(self, user_id):
        access_log = AccessLog(user_id=user_id, document_id=self.id)
        db.session.add(access_log)
        db.session.commit()

    def operation(self):
        return self.get_info()

class Link(Component):
    def __init__(self, target):
        self.target = target

    def get_target(self):
        return self.target

    def operation(self):
        return f"Link to: {self.target}"

class FolderComposite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_child(self, index):
        return self.children[index]

    def get_info(self):
        result = f"Folder: {self.name}\n"
        for child in self.children:
            result += child.operation() + "\n"
        return result

    def operation(self):
        return self.get_info()

# Patrón Proxy
class FolderProxy(Component):
    def __init__(self, folder, user_id):
        self.folder = folder
        self.user_id = user_id

    def access(self):
        document_ids = [doc.id for doc in self.folder.documents]
        access_logs = AccessLog.query.filter(AccessLog.user_id == self.user_id, AccessLog.document_id.in_(document_ids)).all()

        if access_logs:
            return self.folder.get_info()
        else:
            return "Access denied."

    def log_access(self):
        for document in self.folder.documents:
            if document.id not in [log.document_id for log in AccessLog.query.filter(AccessLog.user_id == self.user_id).all()]:
                document.log_access(self.user_id)

# Rutas de la aplicación Flask
@app.route('/')
def index():
    return "Welcome to SAMUR-Protección Civil Document Management System"

@app.route('/folders/<int:folder_id>/<int:user_id>')
def view_folder(folder_id, user_id):
    folder = Folder.query.get_or_404(folder_id)
    proxy = FolderProxy(folder, user_id)
    return proxy.access()

# Crear la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
