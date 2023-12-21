from app.EventSubscriber import EventSubscriber

class Enemy(EventSubscriber):
    #defines itself with these parameters.
    def __init__(self):
        self.numbers = []
        self.all_numbers_chosen = False
        self.iterations = 0
        self.all_numbers_received = []
    #returns whether or not it's numbers are all chosen
    def all_numbers_are_chosen(self):
        return self.all_numbers_chosen
    #returns it's numbers
    def get_numbers(self):
        return self.numbers
    #returns if the player ran out of choices
    def ran_out_of_choices(self, event):
        return self.iterations >= event.number_of_numbers_offered - len(self.numbers)
    #a function that is the basis of all the choices the enemy makes. the enemy lets 40% of it's options pass by and then 
    #chooses based off of their average, or if it runs out of numbers to choose from it picks the remaining ones.    
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
        