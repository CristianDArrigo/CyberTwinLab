from abc import ABC, abstractmethod


class BaseBehavior(ABC):
    """
    Base class for all behaviours.
    Each behaviour should implement the generate_bash() method.
    """

    @abstractmethod
    def generate_bash(self):
        """
        Generate bash command for the behaviour.
        """
        pass
