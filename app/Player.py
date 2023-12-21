import os
import platform

from app.EventSubscriber import EventSubscriber

class Player(EventSubscriber):
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.numbers = []
        self.all_numbers_chosen = False
        self.iterations = 0
        
    def all_numbers_are_chosen(self):
        return self.all_numbers_chosen
    
    def get_numbers(self):
        return self.numbers
    
    def get_prompt(self, event):
        prompt = f"Hmm... Do I want to keep {event.current_number}? I'm allowed to keep {event.choices_allowed} numbers in all. (y/n/q)"
        prompt += "\n"
        prompt += f"chosen so far: {self.numbers}, numbers left to choose from: {event.number_of_numbers_offered - self.iterations}"
        prompt += "\n"
        return prompt
    # my dad wanted to add this to make it less ugly in the console, with his help. basically we're just using pre-made functions to
    #clear the console after every choice the player makes.
    def clear_terminal(self):
        if platform.system() == "Windows":
            os.system('cls')  # Clear terminal for Windows
        else:
            os.system('clear')  # Clear terminal for macOS and Linux in case you use my code in any of the other operating systems.
    # recieve the heavenly values that make the game tick from the event, and then prompt the player to choose the current number to keep or
    # to let go.
    def receive_event(self, event):
        
        self.clear_terminal()
        choice = 'z'
        while choice not in ['q','n']:
            
            choice = input(self.get_prompt(event)).lower()
            self.iterations += 1
            if choice == 'y':
                self.numbers.append(event.current_number)
                self.all_numbers_chosen = (len(self.numbers) >= event.choices_allowed)
                return
            elif choice == 'q':
                self.publisher.end_game()
                return
            elif choice == 'n':
                return
