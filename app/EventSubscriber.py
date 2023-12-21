from abc import ABC, abstractmethod

# Define an abstract base class for subscribers
# this allows Player and enemy to have these functions/methods in their classes respectfully, without having to make the functions here fully.
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
    
    