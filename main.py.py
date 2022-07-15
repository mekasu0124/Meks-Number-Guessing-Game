import random

class NumberGame:
    def __init__(self):
        super(NumberGame,self).__init__()

        self.comp_num = random.randint(1,100)
        self.start_game()
    
    # start the game
    def start_game(self):
        information = [
            "Welcome To Mek's Number Guessing Game!",
            "A few things to keep in mind.",
            "1) All Guesses Must Be Greater Than 0 (zero) or Less Than The Ending Ranges Number",
            "2) You Start The Game With 5 Tries. Once You've Hit 0 Remaining Tries, The Game Will End."
        ]

        print("\n".join([i for i in information]))

        ready_check = input("Enter 'ready' When You're Ready To Start!\n")

        if ready_check.lower() == "ready":
            self.get_user_input()
        else:
            print("Invalid Entry Option")
            self.start_game()
    
    # end the game
    def end_game(self):
        user_confirm = input("Would You Like To Play Again? Y/N:\n")

        if user_confirm.lower() == "y":
            self.start_game()
        elif user_confirm.lower() == "n":
            print("Ending Game. . .")
            print("Game Ended")
        else:
            print("Invalid Entry Option")
            self.end_game()

    # get and check user input
    def get_user_input(self):
        tries = 5

        while tries > 0:
            user_guess = input("Enter Guess Between 1 and 100 or Enter 'Exit' To Leave The Game:\n")

            if user_guess.lower() == "exit":
                self.end_game()
                break
            elif int(user_guess) < 1 and int(user_guess) > 100:
                tries -= 1
                print(f"Guess Must Be Bigger Than 1 and Smaller Than 100. Try Again! {tries} Remaining")
            elif int(user_guess) >= 1 and int(user_guess) <= 100:
                if int(user_guess) > self.comp_num:
                    tries -= 1
                    print(f"Guess Too High. Try Again! {tries} Remaining")
                elif int(user_guess) < self.comp_num:
                    tries -= 1
                    print(f"Guess Too Low. Try Again! {tries} Remaining")
                elif int(user_guess) == self.comp_num:
                    self.game_won()
                    break
                else:
                    tries -= 1
                    print(f"Your Guess Must Be A Whole Number Between 1 and 100 or The Word 'Exit'! Try Again! {tries} Remaining")
        else:
            self.end_game()

    # win the game!
    def game_won(self):
        print("WOOHOO!!! YOU WON!!!!")
        print("~~~~~~~~~~~~~~~~~~~~~")
        self.end_game()



if __name__ == '__main__':
    NumberGame()