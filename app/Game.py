import random
from app.EventPublisher import EventPublisher
from app.Player import Player
from app.Enemy import Enemy

class Game():
    # follow the comments step by step to understand the process of the game.
    def play_game(self):
        
        # Create an instance of the EventPublisher
        publisher = EventPublisher()

        # Create instances of the Player and Enemy
        player = Player(publisher)
        enemy = Enemy()

        # Add the player and enemy as subscribers
        publisher.add_subscriber(player)
        publisher.add_subscriber(enemy)

        # Set up the game with random numbers
        choices_allowed = 3  # Number of choices allowed
        number_of_numbers_presented = 20  # Total numbers offered
        min_number = random.randint(0, 1000)  # Minimum random number
        max_number = min_number + 2 * choices_allowed + random.randint(0, 1000)  # Maximum random number
        # then it calls the function to set up the game in event publisher
        publisher.setup_game(
            choices_allowed, 
            number_of_numbers_presented, 
            min_number, 
            max_number
        )
        # sets the player and enemy as remaining so it can check for them in the while loop while the publisher has subscribers.
        player_remains = True
        enemy_remains = True
        while publisher.has_subscribers():
            publisher.publish_next_event()
            # if it has subscribers it checks if the player and enemy are done or not listening and removes them accordingly.
            if player_remains and player.all_numbers_are_chosen():
                publisher.remove_subscriber(player)
                player_remains = False
            if enemy_remains and enemy.all_numbers_are_chosen():
                publisher.remove_subscriber(enemy)
                enemy_remains = False
        #this is what the player sees when the game ends.
        sum_player = sum(player.get_numbers())
        sum_enemy = sum(enemy.get_numbers())
        print(f"You chose: {player.get_numbers()} which total: {sum_player}")
        print(f"Enemy chose: {enemy.get_numbers()} which total: {sum_enemy}")
        
        if sum_player > sum_enemy:
            print("YOU WIN!!")
        else:
            print("The robot won. :-P")
            