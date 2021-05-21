from revision import Revision

class ArtifactRevision(Revision):
    """
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
    """
    def __init__(self, _rev_string):
        super().__init__(_rev_string)
        self.letters = self.literyF()
        self.digits = self.liczbyF()

    def literyF(self):
        litery = ''
        for i in range(0, len(self.rev)):
            if ord(self.rev[i]) >= 65:
                litery = litery + self.rev[i]
            else:
                return litery

        return litery

    def liczbyF(self):
        x = len(self.literyF())
        liczby = ''
        for i in range(x, len(self.rev)):
            liczby = liczby + self.rev[i]

        return liczby
        pass

    def next_sharp(self):
        litery = self.literyF()
        literyL = []
        litery2 = ''
        suma = 0
        for i in range(0, len(litery)):
            literyL.append(litery[i])
            if ord(litery[i]) == 90:
                suma = suma + 1

        for i in range(0, len(litery)):
            i = i * (-1) - 1
            if ord(litery[i]) < 90:
                if ord(litery[i]) in (72, 86):
                    literyL[i] = chr(ord(litery[i]) + 2)

                elif ord(litery[i]) == 78:
                    literyL[i] = chr(ord(litery[i]) + 5)

                else:
                    literyL[i] = chr(ord(litery[i]) + 1)

                for j in range(0, len(litery)):
                    litery2 = litery2 + literyL[j]

                return ArtifactRevision(litery2)

            else:
                literyL[i] = chr(ord(litery[i]) - 25)
                if (i + len(litery) == 0):
                    for j in range(0, len(litery)):
                        litery2 = litery2 + literyL[j]
                    return ArtifactRevision(litery2 + 'A')

    def next_subrevision(self):
        if (ord(self.rev[-1]) in range(48, 58)):
            liczby = self.liczbyF()
            liczby = int(liczby) + 1
            return ArtifactRevision(self.literyF() + str(liczby))
        else:
            return ArtifactRevision(self.literyF() + '1')

    def __gt__(self, other):
        litery = self.literyF()
        literyO = other.literyF()
        ciag = ''
        ciagO = ''
        ciag = ciag + str(len(litery))
        ciagO = ciagO + str(len(literyO))
        for i in range(0, len(litery)):
            ciag = ciag + litery[i]
        for i in range(0, len(literyO)):
            ciagO = ciagO + literyO[i]
        liczby = self.liczbyF()
        liczbyO = other.liczbyF()
        ciag = ciag + str(len(liczby))
        ciagO = ciagO + str(len(liczbyO))
        for i in range(0, len(liczby)):
            ciag = ciag + liczby[i]
        for i in range(0, len(liczbyO)):
            ciagO = ciagO + liczbyO[i]

        if(ciag > ciagO):
            a='a'
            return a
        else:
            a=''
            return a

if __name__ == "__main__":
    rev = ArtifactRevision("A")
    for i in range(0, 5):
        print(rev)
        for j in range(0, 4):
            rev = rev.next_subrevision()
            print(rev)
        rev = rev.next_sharp()

    revision_strings = ["AB3", "Z", "C1", "C2", "AA1", "C20", "C12", "AB1", "A", "AB30", "AB21"]
    revisions = [ArtifactRevision(r) for r in revision_strings]
    print("Rewizje nieposortowane: {}".format([str(r) for r in revisions]))
    revisions.sort()
    print("Rewizje posortowane:    {}".format([str(r) for r in revisions]))