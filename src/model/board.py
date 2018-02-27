"""Contains game board. Board has 9 squares (3*3)."""

from .field import Field


class Board():

    def __init__(self):
        self.fields = []
        self.__setup_fields()

    def change_field(self, field_number, symbol):
        self.__get_field_by_number(field_number).set_symbol(symbol)

    def get_fields(self):
        return self.fields

    def __setup_fields(self):

        self.fields = []
        fields_quantity = 9

        for num, field in enumerate(range(fields_quantity)):
            field = Field(str(num+1))
            self.fields.append(field)

    def __get_field_by_number(self, field_number):
        return self.fields[field_number-1]

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
