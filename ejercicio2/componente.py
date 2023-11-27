from abc import ABC, abstractmethod
from datetime import datetime
import csv

class Component(ABC):
    @abstractmethod
    def operacion(self):
        pass