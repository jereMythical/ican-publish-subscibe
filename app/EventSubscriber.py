from abc import ABC, abstractmethod

# Define an abstract base class for subscribers
class EventSubscriber(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def receive_event(self, event):
        pass
    
    @abstractmethod
    def all_numbers_are_chosen(self, event):
        pass
    
    @abstractmethod
    def get_numbers(self):
        pass
    
    