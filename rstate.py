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
         R1B005
         R1A002
         R10Z038
         R19ABC999
         etc.
    '''

    def next_build(self):
        liczby = ''
        rev1 = ''
        liczby = int(self.rev[len(self.rev)-3:len(self.rev)]) + 1
        liczby = str(liczby)
        if(len(liczby) == 1):
            rev1 = self.rev[0:len(self.rev) - 3] + '00' + str(liczby)
        elif(len(liczby) == 2):
            rev1 = self.rev[0:len(self.rev) - 3] + '0' + str(liczby)
        else:
            rev1 = self.rev[0:len(self.rev)-3] + str(liczby)
        return RState(rev1)


    def next_number(self):
        liczby = ''
        for i in range(1,len(self.rev)):
            if(ord(self.rev[i]) in range(48,58)):
                liczby = liczby + self.rev[i]
            else:
                break

        liczby = int(liczby) + 1
        return RState('R' + str(liczby) + 'A001')

    def next_letter(self):
        litery = ''
        litery2 = ''
        litery3 = ''
        literyL = []
        suma = 0
        for i in range(1,len(self.rev)):
            if(ord(self.rev[i]) not in range(48,58)):
                litery = litery + self.rev[i]
                j = i

        for i in range(0, j-len(litery)+1):
            litery3 = litery3 + self.rev[i]

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

                rev = litery3 + litery2 + '001'

                return RState(rev)

            else:
                literyL[i] = chr(ord(litery[i]) - 25)
                if (i + len(litery) == 0):
                    for j in range(0, len(litery)):
                        litery2 = litery2 + literyL[j]
                    return RState(litery3 + litery2 + 'A' + '001')

    def __gt__(self, other):
        liczby = ''
        liczbyO = ''
        litery = ''
        literyO = ''
        ciag = ''
        ciagO = ''
        kod = []
        kodO = []
        for i in range(0, len(self.rev)):
            kod.append(self.rev[i])

        for i in range(0, len(other.rev)):
            kodO.append(other.rev[i])

        for i in range(1, len(self.rev)):
            if (ord(self.rev[i]) not in range(48, 58)):
                j = i
                break
            else:
                liczby = liczby + self.rev[i]

        for i in range(1, len(other.rev)):
            if (ord(other.rev[i]) not in range(48, 58)):
                j = i
                break
            else:
                liczbyO = liczbyO + other.rev[i]

        kod.insert(1, len(liczby))
        kodO.insert(1, len(liczbyO))

        for i in range(j + 1, len(kod)):
            if (ord(kod[i]) in range(48, 58)):
                break
            else:
                litery = litery + self.rev[i]

        kod.insert(j + 1, len(litery))

        for i in range(j + 1, len(kodO)):
            if (ord(kodO[i]) in range(48, 58)):
                break
            else:
                literyO = literyO + other.rev[i]

        kodO.insert(j + 1, len(literyO))

        for i in range(0, len(kod)):
            ciag = ciag + str(kod[i])

        for i in range(0, len(kodO)):
            ciagO = ciagO + str(kodO[i])

        if (ciag > ciagO):
            a = 'a'
            return a
        else:
            a = ''
            return a

if __name__ == "__main__":
    rev = RState("R9A001")
    for i in range(0, 5):
        for i in range(0, 5):
            print(rev)
            for j in range(0, 5):
                rev = rev.next_build()
                print(rev)
            rev = rev.next_letter()
        rev = rev.next_number()

    revision_strings = ["R1A001", "R2A002", "R12ACD003", "R1AB002", "R1Z038", "R1Z037", "R12A002", "R10AB006", "R1B001"]
    revisions = [RState(r) for r in revision_strings]
    print("Rewizje nieposortowane: {}".format([str(r) for r in revisions]))
    revisions.sort()
    print("Rewizje posortowane:    {}".format([str(r) for r in revisions]))