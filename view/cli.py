from typing import List, Union


class CLI:
    """Class that defines CLI initialization, characterized by:
    - the display of the labyrinth
    - getting a direction in the labyrinth
    - win and lose messages to end the game"""

    DIRECTIONS = {'Z': 'UP',
                  'Q': 'LEFT',
                  'S': 'DOWN',
                  'D': 'RIGHT'}

    def __init__(self, lines: int, columns: int):
        pass

    def display_lab(self, lab: List[List[str]]):
        """Function that displays labyrinth"""

        for i in lab:
            result = ''.join(i)
            print(result)
            # Ou :
            # r = map(lambda x: ''.join(x), val)
            # r = '\n'.join(r)

    def win(self):
        """Function that prints a 'win' message"""

        print("Congratulation, you win!")

    def lose(self):
        """Function that prints a 'lose' message"""

        print("Sorry, but you died!")

    def get_direction(self) -> Union[None, List[str]]:
        """Function that set a direction in labyrinth"""

        direction = input("Select direction 'Z, Q, S, D' "
                          "or press 'X' to quit : ").upper()
        if direction == "X":
            return None
        elif direction in ['Z', 'Q', 'S', 'D']:
            return [self.DIRECTIONS[direction]]

        print("Please enter a valid direction")
        return self.get_direction()
