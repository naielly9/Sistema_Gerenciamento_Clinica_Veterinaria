from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    @abstractmethod
    def remover(self):
        pass

    
