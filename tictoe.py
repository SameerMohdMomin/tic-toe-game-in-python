import os
os.system("clear")


class Board():
     def __init__(self):
         self.cells=[" ", " ", " ", " ", " ", " ", " ", " ", " "," "]


     def display(self):
        print("%s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
        print("___________")
        print("%s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
        print("___________")
        print("%s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))

     def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no]=player

     def is_winner(self, player):
         
         if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
             return True
         elif self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
             return True
         elif self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
             return True
         elif self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
             return True
         elif self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
             return True
     def reset(self):
         self.cells=[" ", " ", " ", " ", " ", " ", " ", " ", " "," "]
 
board=Board()


def print_header():
    print("Wellcome to tic-tac-toe Game")

def refresh_screen():
    os.system("clear")

    print_header()

    board.display()

while True:
    refresh_screen()

    x_choice=int(input("\nX) please  choose 1-9 >"))

    board.update_cell(x_choice,"X")

    refresh_screen()

    if board.is_winner("X"):
        print("\nX Wins! \n")
        play_again=input("would you like to play again (Y/N)>").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
            


    x_choice=int(input("\n0) please  choose 1-9 >"))

    board.update_cell(x_choice,"0")

    if board.is_winner("0"):
        print("\n0 Wins! \n")
        play_again=input("would you like to play again (Y/N)>").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
