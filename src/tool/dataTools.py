

class DataTools():

    @staticmethod
    def check_if_element_in_collection(element, collection):
        for el in collection:
            if el == element:
                return True
        return False