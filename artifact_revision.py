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

    def literyF(self):
        litery = ''
        for i in range(0, len(self.rev)):
            if (ord(self.rev[i]) >= 65):
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
            if (ord(litery[i]) == 90):
                suma = suma + 1

        for i in range(0, len(litery)):
            i = i * (-1) - 1
            if (ord(litery[i]) < 90):
                if (ord(litery[i]) in (72, 86)):
                    literyL[i] = chr(ord(litery[i]) + 2)

                elif (ord(litery[i]) == 78):
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

if __name__ == "__main__":
    rev = ArtifactRevision("A")
    for i in range(0, 5):
        if str(rev) != "A":
            rev.next_sharp()
        print(rev)
        for j in range(0, 4):
            rev = rev.next_subrevision()
            print(rev)

    revisions = ["A", "Z", "C1", "C2", "C12", "C20", "AA1", "AB1", "AB3", "AB21", "AB30"]
    print("Rewizje nieposortowane: {}".format(revisions))
    revisions.sort()
    print("Rewizje posortowane:    {}".format(revisions))