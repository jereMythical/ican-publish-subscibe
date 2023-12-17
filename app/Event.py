# Each event will tell you the number of numbers that you'll be offered before the game is over
# It will also give you the number of choices you can have, before you are no longer offered any more
# current number is the current randomly generated number

class Event:
    def __init__(self, number_of_numbers_offered: int, choices_allowed: int, current_number: int):
        self.number_of_numbers_offered = number_of_numbers_offered
        self.choices_allowed = choices_allowed
        self.current_number = current_number
