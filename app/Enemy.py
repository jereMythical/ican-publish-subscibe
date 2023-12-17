from app.EventSubscriber import EventSubscriber

class Enemy(EventSubscriber):
    
    def __init__(self):
        self.numbers = []
        self.all_numbers_chosen = False
        self.iterations = 0
        self.all_numbers_received = []
        
    def all_numbers_are_chosen(self):
        return self.all_numbers_chosen
    
    def get_numbers(self):
        return self.numbers
    
    def ran_out_of_choices(self, event):
        return self.iterations >= event.number_of_numbers_offered - len(self.numbers)
        
    def receive_event(self, event):
        
        self.all_numbers_received.append(event.current_number)
        self.iterations += 1
        
        # only chooses a number if it's better than the averag of all numbers received and we've received > 40% of the numbers
        if len(self.all_numbers_received) < 0.4 * event.number_of_numbers_offered:
            return
        
        average = sum(self.all_numbers_received) / len(self.all_numbers_received)
        if event.current_number > average or self.ran_out_of_choices(event):
            print(f"Enemy chose number: {event.current_number} after {self.iterations} iterations.")
            self.numbers.append(event.current_number)
        
        self.all_numbers_chosen = (len(self.numbers) >= event.choices_allowed)
        