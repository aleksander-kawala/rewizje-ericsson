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
            if(ord(litery[0]) == 80):
                for j in range(1, len(litery)):
                    litery2 = litery2 + literyL[j]
                return DocRevision(litery2)

            else:
                if (ord(litery[i]) < 90):
                    if (ord(litery[i]) in (72, 86)):
                        literyL[i] = chr(ord(litery[i]) + 2)

                    elif (ord(litery[i]) == 78):
                        literyL[i] = chr(ord(litery[i]) + 5)

                    else:
                        literyL[i] = chr(ord(litery[i]) + 1)

                    literyL.insert(0, 'P')
                    for j in range(0, len(litery)+1):
                        litery2 = litery2 + literyL[j]

                    return DocRevision(litery2 + '1')

                else:
                    literyL[i] = chr(ord(litery[i]) - 25)
                    if (i + len(litery) == 0):
                        literyL.insert(0, 'P')
                        for j in range(0, len(litery)+1):
                            litery2 = litery2 + literyL[j]
                        return DocRevision(litery2 + 'A' + '1')

    def next_preliminary(self):
        litery = self.literyF()
        if(ord(litery[0]) != 80):
            return DocRevision(litery)
        else:
            if (ord(self.rev[-1]) in range(48, 58)):
                liczby = self.liczbyF()
                liczby = int(liczby) + 1
                return DocRevision(self.literyF() + str(liczby))
            else:
                return DocRevision(self.literyF() + '1')

    def __gt__(self, other):
        litery = self.literyF()
        literyO = other.literyF()
        ciagO = ''
        ciag = ''
        if (ord(litery[0]) == 80):
            ciag = str(len(litery) - 1)
            for i in range(1, len(litery)):
                ciag = ciag + litery[i]
            ciag = ciag + '0'
        else:
            ciag = str(len(litery))
            for i in range(0, len(litery)):
                ciag = ciag + litery[i]
            ciag = ciag + '1'

        if (ord(literyO[0]) == 80):
            ciagO = str(len(literyO) - 1)
            for i in range(1, len(literyO)):
                ciagO = ciagO + literyO[i]
            ciagO = ciagO + '0'
        else:
            ciagO = str(len(literyO))
            for i in range(0, len(literyO)):
                ciagO = ciagO + literyO[i]
            ciagO = ciagO + '1'

        liczby = self.liczbyF()
        ciag = ciag + str(len(liczby))
        for i in range(0, len(liczby)):
            ciag = ciag + liczby[i]

        liczbyO = other.liczbyF()
        ciagO = ciagO + str(len(liczbyO))
        for i in range(0, len(liczbyO)):
            ciagO = ciagO + liczbyO[i]

        if (ciag > ciagO):
            a = 'a'
            return a
        else:
            a = ''
            return a

if __name__ == "__main__":
    rev = DocRevision("PA1")
    for i in range(0, 5):
        print(rev)
        for j in range(0,5):
            rev = rev.next_preliminary()
            if(ord(str(rev)[-1]) not in range(48, 58)):
                break
            else:
                print(rev)
        rev = rev.next_sharp()

    revision_strings = ["PA1", "PA2", "B", "PC1", "PC12", "PC20", "PAA1", "PB1", "PAB3", "PAB21", "PAB30", "C", "AA", "AB", "A"]
    revisions = [DocRevision(r) for r in revision_strings]
    print("Rewizje nieposortowane: {}".format([str(r) for r in revisions]))
    revisions.sort()
    print("Rewizje posortowane:    {}".format([str(r) for r in revisions]))