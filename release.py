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
        kwartal = int(self.rev[4])
        rok = int(self.rev[1:3])
        if(kwartal == 4):
            kwartal = 1
            rok = rok + 1
        else:
            kwartal = kwartal + 1

        rev = 'G' + str(rok) + 'Q' + str(kwartal)

        return Release(rev)

    def next_version(self):
        lista = []
        lista2 = []
        rev = ''
        liczby = ''
        for i in range(0, len(self.rev)):
            if(i > 4):
                lista.append(self.rev[i])
            else:
                pass
                lista.append(self.rev[i])
                lista2.append(self.rev[i])

        if('.' in lista):
            liczby = self.rev[6:]
            liczby = int(liczby)
            liczby = liczby + 1

        else:
            for i in range(0,5):
                rev = rev + lista2[i]
            rev = rev + '.' + '1'
            return Release(rev)

        for i in range(0,5):
            rev = rev + lista2[i]

        rev = rev + '.' + str(liczby)

        return Release(rev)

    def __gt__(self, other):
        a = ''
        b = 'a'
        if(int(self.rev[1:3]) > int(other.rev[1:3])):
            return b
        elif(int(self.rev[1:3]) == int(other.rev[1:3])):
            if(int(self.rev[4]) > int(other.rev[4])):
                return b
            elif(int(self.rev[4]) == int(other.rev[4])):
                if(len(self.rev) > 5):
                    if(len(other.rev) > 5):
                        if(int(self.rev[6:]) > int(other.rev[6:])):
                            return b
                        else:
                            return a
                    else:
                        return b
                else:
                    return a
            else:
                return a
        else:
            return a

if __name__ == "__main__":
    rev = Release("G19Q1")
    for i in range(0, 5):
        print(rev)
        for j in range(0, 5):
            rev = rev.next_version()
            print(rev)
        rev = rev.next_quarter()

    revision_strings = ["G19Q2","G20Q1.2","G19Q3","G20Q4","G19Q2.1","G20Q1.1","G20Q3.2","G19Q1","G20Q2","G19Q4","G21Q1","G20Q3.10","G20Q3.1","G20Q1","G20Q3"]
    revisions = [Release(r) for r in revision_strings]
    print("Rewizje nieposortowane: {}".format([str(r) for r in revisions]))
    revisions.sort()
    print("Rewizje posortowane:    {}".format([str(r) for r in revisions]))