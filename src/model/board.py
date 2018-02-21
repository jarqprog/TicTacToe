"""Contains game board. Board has 9 squares (3*3)."""

from .square import Square


class Board():

    @classmethod
    def set_game_board(cls):

        fields = []
        fields_quantity = 9

        for num, field in enumerate(range(fields_quantity)):
            field = Square(str(num+1))
            fields.append(field)

        return fields

    def __init__(self):
        self.fields = self.set_game_board()

    def get_square(self, index):
        if 0 < index < 10:
            return self.fields[index-1]

    def __str__(self):
        
        head_and_bottom_line = '\n'*2
        output_fields = head_and_bottom_line
        
        for field in self.fields:
            output_fields += str(field)
            _id = field.get_id()
            if int(_id) % 3 == 0:
                output_fields += "\n"
        output_fields += head_and_bottom_line
        return output_fields
