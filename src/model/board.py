"""Contains game board. Board has 9 squares (3*3)."""

from .field import Field


class Board():

    def __init__(self):
        self.fields = []
        self.setup_fields()

    def setup_fields(self):

        self.fields = []
        fields_quantity = 9

        for num, field in enumerate(range(fields_quantity)):
            field = Field(str(num+1))
            self.fields.append(field)

    def get_field_by_index(self, fields_index):
        return self.fields[fields_index-1]

    def change_field(self, index, symbol):
        self.get_field_by_index(index).set_symbol(symbol)

    def get_fields(self):
        return self.fields

    def __str__(self):
        board = """\n
                 {} | {} | {}
                -----------
                 {} | {} | {}
                -----------
                 {} | {} | {}
                \n""".format(
                            self.fields[0], self.fields[1], self.fields[2],
                            self.fields[3], self.fields[4], self.fields[5],
                            self.fields[6], self.fields[7], self.fields[8])

        return board
