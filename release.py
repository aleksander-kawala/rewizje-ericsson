from revision import Revision

class Release(Revision):

    '''
    G19Q2.3
    ||||| |
    ||||| +-version
    |||++---quarter
    +++-----year
    Examples:
        G19Q3
        G19Q4
        G19Q4.1
        G19Q4.2
        G20Q1
        G20Q2
        G20Q3
        G20Q3.1
        etc.
    '''

    def __init__(self, revision_string):
        pass

    def next_quarter(self):
        pass

    def next_version(self):
        pass


