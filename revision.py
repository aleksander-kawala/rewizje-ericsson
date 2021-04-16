class Revision:

    FORBIDDEN_CHARACTERS = ['I', 'O', 'P', 'Q', 'R', 'W']

    def __eq__(self, other):
        raise NotImplementedError()

    def __ne__(self, other):
        raise NotImplementedError()

    def __lt__(self, other):
        raise NotImplementedError()

    def __le__(self, other):
        raise NotImplementedError()

    def __gt__(self, other):
        raise NotImplementedError()

    def __ge__(self, other):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()