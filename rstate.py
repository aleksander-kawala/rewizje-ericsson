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

    def next_build(self):
        return self

    def next_number(self):
        return self

    def next_letter(self):
        return self

if __name__ == "__main__":
    revision = RState("R9V001")
    for i in range(0, 2):
        if str(revision) != "R9V001":
            revision.next_number()
        print(revision)
        for j in range(0, 5):
            revision = revision.next_letter()
            print(revision)
            for k in range(0, 2):
                revision = revision.next_build()
                print(revision)

    revision_strings = ["R1A001", "R2A002", "R12ACD003", "R1AB002", "R1Z038", "R1Z037", "R12A002", "R10AB006", "R1B001"]
    revisions = [RState(r) for r in revision_strings]
    print("Rewizje nieposortowane: {}".format([str(r) for r in revisions]))
    revisions.sort()
    print("Rewizje posortowane:    {}".format([str(r) for r in revisions]))