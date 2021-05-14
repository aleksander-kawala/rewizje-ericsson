class Revision:

    FORBIDDEN_CHARACTERS = ['I', 'O', 'P', 'Q', 'R', 'W']

    def __init__(self, revision_string):
        self.rev = revision_string

    def __eq__(self, other):
        return self.rev == other.rev

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __gt__(self, other):
        raise NotImplementedError()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __str__(self):
        return self.rev