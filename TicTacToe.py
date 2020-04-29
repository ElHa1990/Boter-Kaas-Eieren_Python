class TicTacToe:
    nameFirstPlayer = ""
    nameSecondPlayer = ""
    playerName = ""
    activePlayer = 1
    moves = 0
    activeGame = True;
    marker = "X"
    numbersBord = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def setup_game(self):
        # Show rules tic-tac-toe
        print("RULES FOR TIC-TAC-TOE\n" +
        "1. The game is played on a grid that's 3 squares by 3 squares.\n" +
        "2. You are X, your friend is O. Players take turns putting their marks in empty squares.\n" +
        "3. The first player to get 3 of his/her marks in a row (up, down, across, or diagonally) is the winner.\n" +
        "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie. \n")

        # Enter and show name player one
        self.nameFirstPlayer = input("Enter name first player: ")
        print("Name first player: " + self.nameFirstPlayer + "\n");

        # Enter and show name player two
        self.nameSecondPlayer = input("Enter name second player: ")
        print("Name first player: " + self.nameSecondPlayer + "\n");

        print("Okay " + self.nameFirstPlayer + " and " + self.nameSecondPlayer + " lets play! \n")

        self.print_bord()
        self.start_game()


    def print_bord(self):

        bord = ("_" + self.numbersBord[0] + "_|_" + self.numbersBord[1] + "_|_" + self.numbersBord[2] + "_\n"
                "_" + self.numbersBord[3] + "_|_" + self.numbersBord[4] + "_|_" + self.numbersBord[5] + "_\n"
                " " + self.numbersBord[6] + " | " + self.numbersBord[7] + " | " + self.numbersBord[8] + " \n");

        print(bord)


    def ask_position(self):
        # Check number or other keyboard character enterd, only numbers between 1 and 9.
        try:
            self.inputPlayer = int(input(self.playerName + " please enter the number where you would like to place the " + self.marker + ": "))
        except:
            print("Please enter a number.")
            self.ask_position()
            return

        # vraag waar nummer geplaatst moet worden is gesteld in play game
        self.inputPlayer_int = isinstance(self.inputPlayer, int)

        if self.inputPlayer_int == True:
            self.number = self.inputPlayer

            if self.number > 9 or self.number < 1:
                print("Please enter a number between 1 and 9.");
                self.ask_position()
                return

            if self.numbersBord[self.number - 1] == ("X") or self.numbersBord[self.number - 1] == ("O"):
                print ("A marker is already placed on the number you entered. Please try again.")
                self.ask_position()
            else:
                self.numbersBord[self.number - 1] = self.marker;
                self.print_bord()


    def start_game(self):
        # While the game is active, ask players alternately where to place their marker until there is a winner or the game ended in a draw.
        # When game has ended ask if they want to play again or end the game */
        while self.activeGame:
            self.moves += 1

            if self.activePlayer == 1:
                self.marker = "X"
                self.playerName = self.nameFirstPlayer
                self.activePlayer = 2

            elif self.activePlayer == 2:
                self.marker = "O";
                self.playerName = self.nameSecondPlayer
                self.activePlayer = 1

            # Check entered number or other keyboard character
            self.ask_position()
  
            # // End game --> winning or draw
            self.end_game()
            # scanner.nextLine();

    def end_game(self):
        # Win
        self.win = ("Congratulations " + self.playerName +", you won!")
        
        if self.numbersBord[0] == (self.marker) and self.numbersBord[1] == (self.marker) and self.numbersBord[2] == (self.marker):
            print(self.win)
            self.reset_game()
        elif self.numbersBord[3] == (self.marker) and self.numbersBord[4] == (self.marker) and self.numbersBord[5] == (self.marker): 
            print(self.win)
            self.reset_game()
        elif self.numbersBord[6] == (self.marker) and self.numbersBord[7] == (self.marker) and self.numbersBord[8] == (self.marker): 
            print(self.win)
            self.reset_game()
        elif self.numbersBord[0] == (self.marker) and self.numbersBord[3] == (self.marker) and self.numbersBord[6] == (self.marker):
            print(self.win)
            self.reset_game()
        elif self.numbersBord[1] == (self.marker) and self.numbersBord[4] == (self.marker) and self.numbersBord[7] == (self.marker):
            print(self.win)
            self.reset_game()
        elif self.numbersBord[2] == (self.marker) and self.numbersBord[5] == (self.marker) and self.numbersBord[8] == (self.marker):
            print(self.win)
            self.reset_game()
        elif self.numbersBord[0] == (self.marker) and self.numbersBord[4] == (self.marker) and self.numbersBord[8] == (self.marker):
            print(self.win)
            self.reset_game()
        elif self.numbersBord[2] == (self.marker) and self.numbersBord[4] == (self.marker) and self.numbersBord[6] == (self.marker):
            print(self.win)
            self.reset_game()

        # // Draw
        elif self.moves == 9:
            print("Your game has ended, it's a draw!")
            self.reset_game()

    def reset_game(self):
        # stop while loop
        self.activeGame = False
        self.keyboardEnter = input("Press Y if you would like to play a new game. Press N to leave the game. ")

        # Check entered keyboard entry
        # if Y: play new game, if N: stop game, any other keyboard entry repeat question.
        if self.keyboardEnter == "Y":

            # reset the bord, all X and O should be removed and replaced with numbers
            self.numbersBord = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

            # reset activePlayer
            self.activePlayer = 1;
            
            # reset number of moves
            self.moves = 0;

            # Next line so that first player name isn't 'Enter' and start game
            self.activeGame = True;

            # print empty line before starting new game
            print()
            self.setup_game();

        # if N, stop paying the game. ASCII value for 'N' is 78
        elif self.keyboardEnter == "N":
            print("Thank you for playing, have a nice day!");
            self.activeGame = False;

        else:
            self.reset_game();
