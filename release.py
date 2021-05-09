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

    def grater(self):
        lista = []
        lista2 = []
        rev = ''
        for i in range(0, len(self.rev)):
            if(i > 4):
                lista.append(self.rev[i])
            else:
                pass
                lista.append(self.rev[i])
                lista2.append(self.rev[i])

        if ('.' in lista):
            liczby = self.rev[6:]
            liczby = len(liczby)
            lista.insert(6, liczby)

        else:
            pass

        for i in range(0, len(lista)):
            rev = rev + str(lista[i])

        return rev

    def zmiana(self):
        lista = []
        rev = ''
        for i in range(0, len(self.rev)):
            lista.append(self.rev[i])

        if ('.' in lista):
            lista.pop(6)

        for i in range(0, len(lista)):
            rev = rev + lista[i]

        return rev

if __name__ == "__main__":
    rev = Release("G19Q1")
    for i in range(0, 5):
        print(rev)
        for j in range(0, 5):
            rev = rev.next_version()
            print(rev)
        rev = rev.next_quarter()

    revisions = ["G19Q2","G20Q1.2","G19Q3","G20Q4","G19Q2.1","G20Q1.1","G20Q3.2","G19Q1","G20Q2","G19Q4","G21Q1","G20Q3.10","G20Q3.1","G20Q1","G20Q3"]
    print("Rewizje nieposortowane: {}".format(revisions))
    revisions.sort()
    print("Rewizje posortowane:    {}".format(revisions))

    for i in range(0, len(revisions)):
        rev = Release(revisions[i])
        ciag = rev.grater()
        revisions[i] = ciag

    revisions.sort()

    for i in range(0, len(revisions)):
        ciag = Release(revisions[i])
        rev = ciag.zmiana()
        revisions[i] = rev

    print("Rewizje poprawnie posortowane: {}".format(revisions))