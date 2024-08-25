# plugin_abc.py

from abc import ABC, abstractmethod

class PluginABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def execute(self, gui):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_version(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @classmethod
    def register(cls):
        plugin = cls()
        return {
            'name': plugin.get_name(),
            'description': plugin.get_description(),
            'version': plugin.get_version(),
            'run': plugin.execute
        }