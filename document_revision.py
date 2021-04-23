from revision import Revision

class DocRevision(Revision):

    '''
    Examples:
        PA1
        PA2
        PA3
        A
        PB1
        PB2
        B
        PC1
        etc.
    '''

    def next_sharp(self):
        return self

    def next_preliminary(self):
        return self

if __name__ == "__main__":
    revision = DocRevision("PH1")
    for i in range(0, 5):
        if str(revision) != "PH1":
            revision.next_sharp()
        print(revision)
        for j in range(0, 3):
            revision = revision.next_preliminary()
            print(revision)

    revisions = ["PA1", "PA2", "B", "PC1", "PC12", "PC20", "PAA1", "PB1", "PAB3", "PAB21", "PAB30", "C", "AA", "AB", "A"]
    print("Rewizje nieposortowane: {}".format(revisions))
    revisions.sort()
    print("Rewizje posortowane:    {}".format(revisions))