from revision import Revision

class ArtifactRevision(Revision):
    '''
    Examples:
        A
        B
        B1
        B2
        B3
        C
        C1
        Z
        AA
        etc.
    '''

    def next_sharp(self):
        return self

    def next_subrevision(self):
        return self

if __name__ == "__main__":
    revision = ArtifactRevision("A")
    for i in range(0, 5):
        if str(revision) != "A":
            revision.next_sharp()
        print(revision)
        for j in range(0, 3):
            revision = revision.next_subrevision()
            print(revision)

    revisions = ["A", "Z", "C1", "C2", "C12", "C20", "AA1", "AB1", "AB3", "AB21", "AB30"]
    print("Rewizje nieposortowane: {}".format(revisions))
    revisions.sort()
    print("Rewizje posortowane:    {}".format(revisions))
