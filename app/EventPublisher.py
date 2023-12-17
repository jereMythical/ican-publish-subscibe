import random

from app.Event import Event

class EventPublisher:
    def __init__(self):
        self.subscribers = []
        self.running = True

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)
            
    def setup_game(self, choices_allowed: int, number_of_numbers_presented: int, min_number: int, max_number: int):
        self.choices_allowed = choices_allowed
        self.number_of_numbers_presented = number_of_numbers_presented
        self.min_number = min_number
        self.max_number = max_number
        
    def end_game(self):
        self.running = False
        
    def get_next_event(self):
        return Event(
            number_of_numbers_offered = self.number_of_numbers_presented,
            choices_allowed = self.choices_allowed,
            current_number = random.randint(self.min_number, self.max_number)
        )
        
    def publish_next_event(self):
                
        event = self.get_next_event()
        
        for subscriber in self.subscribers:
            subscriber.receive_event(event)
            
    def has_subscribers(self):
        
        for subscriber in self.subscribers:
            if subscriber.all_numbers_are_chosen():
                self.remove_subscriber(subscriber)
        
        return len(self.subscribers) > 0
        