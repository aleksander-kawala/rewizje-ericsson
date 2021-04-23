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

    def next_quarter(self):
        return self

    def next_version(self):
        return self

if __name__ == "__main__":
    revision = Release("G19Q1")
    for i in range(0, 5):
        if str(revision) != "G19Q1":
            revision.next_quarter()
        print(revision)
        for j in range(0, 3):
            revision = revision.next_version()
            print(revision)

    revisions = ["G19Q2","G20Q1.2","G19Q3","G20Q4","G19Q2.1","G20Q1.1""G20Q3.2","G19Q1","G20Q2","G19Q4","G21Q1","G20Q3.10","G20Q3.1","G20Q1","G20Q3"]
    print("Rewizje nieposortowane: {}".format(revisions))
    revisions.sort()
    print("Rewizje posortowane:    {}".format(revisions))