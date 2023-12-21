import random

from app.Event import Event

class EventPublisher:
    # initializes itself
    def __init__(self):
        self.subscribers = []
        self.running = True
    # this adds a subscriber (either the player or the enemy) whenever this is called. this allows us to publish the events to the player
    #and enemy so that they can make their choices
    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
    #removes a subscriber from the list of subscribers.
    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)
    #sets everything for the game up using itself to get the values from.
    def setup_game(self, choices_allowed: int, number_of_numbers_presented: int, min_number: int, max_number: int):
        self.choices_allowed = choices_allowed
        self.number_of_numbers_presented = number_of_numbers_presented
        self.min_number = min_number
        self.max_number = max_number
    #the machine equivalent of telling someone to commit suicide. just kills the game whenever this function is called.
    def end_game(self):
        self.running = False
    #this returns it's own values as parameters for the event and then returns the event.
    def get_next_event(self):
        return Event(
            number_of_numbers_offered = self.number_of_numbers_presented,
            choices_allowed = self.choices_allowed,
            current_number = random.randint(self.min_number, self.max_number)
        )
    #sends the event to all the subscribers
    def publish_next_event(self):
                
        event = self.get_next_event()
        
        for subscriber in self.subscribers:
            subscriber.receive_event(event)
    #returns a boolean if it has subscribers   
    def has_subscribers(self):
        
        for subscriber in self.subscribers:
            if subscriber.all_numbers_are_chosen():
                self.remove_subscriber(subscriber)
        
        return len(self.subscribers) > 0
        