from revision import Revision

class RStateException(Exception):
    pass

class RState(Revision):
    '''
    R1A002
     |||||
     ||+++-build
     |+----letter
     +-----number

     Examples:
         P1B005
         R1A002
         R10Z038
         R19ABC999
         etc.
    '''

    def __init__(self, rstate_string):
        pass

    def next_build(self):
        pass

    def next_number(self):
        pass

    def next_letter(self):
        pass