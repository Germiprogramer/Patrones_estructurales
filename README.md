# Patrones_estructurales

Germán Llorente

El link al repositorio es el siguiente: https://github.com/Germiprogramer/Patrones_estructurales.git

### Pizzeria

En el ejercicio de la entrega pasada, se decidió emplear el patrón builder para la elaboración de las pizzas, debido a que este patrón habilita declarar subpartes de un elemento e ir indicándolas. Esto era perfecto para una pizza con distintos ingredientes. 

En este caso, debíamos expandir el patrón con la implementación de menús. Para ello se ha requerido del patrón composite, justificado por la necesidad de representar tanto elementos individuales (como entradas, bebidas, pizzas y postres), como menús compuestos que pueden contener otros elementos y/o menús. Las razones de uso de este patrón de diseño son varias:

**Estructura Jerárquica:**

Los menús pueden tener una estructura jerárquica, donde un menú compuesto puede contener otros menús o elementos individuales. En el ejercicio, se han metido menús dobles, que son menús compuestos de otros menús. El patrón Composite permite representar esta estructura de manera eficiente.

**Operaciones Recursivas:**

Al utilizar Composite, se pueden realizar operaciones recursivas en toda la estructura de menús y elementos. Por ejemplo, calcular el precio total de un menú compuesto que contiene otros menús y elementos.

**Facilita la Creación y Modificación:**

La implementación del patrón Composite facilita la creación y modificación de menús. Se pueden agregar, quitar o modificar elementos de manera transparente, ya que todos los elementos comparten la misma interfaz.

**Cálculo Eficiente del Precio:**

El cálculo del precio de un menú compuesto se puede realizar de manera eficiente al aprovechar las operaciones recursivas.  Cada elemento individual contribuye a la suma total del precio, y los menús compuestos propagan la llamada para calcular el precio de sus componentes.

**Persistencia y Reconstrucción:**

Al utilizar Composite, se facilita la persistencia en archivos CSV y la reconstrucción de la estructura de menús a partir de la información almacenada. La recursividad inherente al patrón simplifica la reconstrucción de menús compuestos a partir de sus componentes almacenados.

Además, cabe destacar también que el patron builder y el patrón composite pueden acoplarse el uno al otro y ser usados como una estructura única. Esto permite realizar perfectamente la simulación de la pizzeria.

_____________________________________________________________________________________________________________________________________________________________________

Además de la justificación del uso del patrón, me gustaría resaltar el uso de las interfaces gráficas que se han elegido, dado que lo que creo que le da un toque extra a mi resolución del ejercicio es la conexión de interfaces en función de las conexiones del usuario. Para próximos ejercicios se intentará realizar en frameworks como Django o Flask, pero en este he preferido optar por readaptar la versión anterior-

### SAMUR


En el ejercicio anterior, se utiliza el patrón Proxy para controlar el acceso a la carpeta, agregando una capa adicional de indirección entre el cliente y la carpeta real. Aquí hay algunas justificaciones para el uso del patrón Proxy en ese contexto:

**Control de Acceso:**

El Proxy actúa como una barrera de acceso a la carpeta real. Antes de permitir el acceso a la carpeta, el Proxy solicita al usuario sus credenciales (nombre de usuario y contraseña). Esto proporciona una capa de seguridad y control de acceso.

**Registro de Operaciones:**

El Proxy registra las operaciones realizadas en la carpeta en un archivo CSV. Esto permite llevar un registro de todas las acciones realizadas por los usuarios. El Proxy se encarga de esta funcionalidad sin afectar directamente a la carpeta real.

**Reconstrucción desde el Registro:**

El Proxy utiliza la información almacenada en el archivo de registro para reconstruir la estructura de la carpeta. Esta capacidad de reconstrucción es útil en situaciones en las que la aplicación se reinicia o si se desea restaurar el estado anterior.

**Interfaz Uniforme:**

El Proxy implementa la misma interfaz que la carpeta real, permitiendo que el cliente interactúe con el Proxy de la misma manera que lo haría con la carpeta real. Esto proporciona una interfaz uniforme, independientemente de si se está utilizando el Proxy o la carpeta real.

**Encapsulación de la Complejidad:**

El Proxy encapsula la complejidad asociada con la autenticación, registro y reconstrucción de operaciones. El cliente no necesita preocuparse por estas responsabilidades; simplemente interactúa con el Proxy de la misma manera que interactuaría con la carpeta real.

**Adaptación de Funcionalidades:**

En el futuro, se podrían agregar más funcionalidades al Proxy, como el encriptado de datos, control de acceso basado en roles u otras mejoras de seguridad, sin modificar directamente la carpeta real ni afectar al cliente.

En resumen, el uso del patrón Proxy en este ejercicio proporciona una capa intermedia que ofrece control de acceso, registro de operaciones y la capacidad de reconstruir la estructura de la carpeta desde un archivo de registro. Además, facilita la posible incorporación de características adicionales sin afectar directamente la lógica de la carpeta real.
