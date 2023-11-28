from abc import ABC, abstractmethod
from datetime import datetime
import csv

# clase abstracta Component
class Component(ABC):
    @abstractmethod
    def operacion(self):
        pass