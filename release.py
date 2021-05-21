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
        lista = []
        listaO = []
        lista2O = []
        lista2 = []
        rev = ''
        revO = ''
        for i in range(0, len(self.rev)):
            if (i > 4):
                lista.append(self.rev[i])
            else:
                pass
                lista.append(self.rev[i])
                lista2.append(self.rev[i])

        for i in range(0, len(other.rev)):
            if (i > 4):
                listaO.append(other.rev[i])
            else:
                pass
                listaO.append(other.rev[i])
                lista2O.append(other.rev[i])

        if ('.' in lista):
            liczby = self.rev[6:]
            liczby = len(liczby)
            lista.insert(6, liczby)
        else:
            pass

        if ('.' in listaO):
            liczbyO = other.rev[6:]
            liczbyO = len(liczbyO)
            listaO.insert(6, liczbyO)
        else:
            pass

        for i in range(0, len(lista)):
            rev = rev + str(lista[i])

        for i in range(0, len(listaO)):
            revO = revO + str(listaO[i])

        if (rev > revO):
            a = 'a'
            return a
        else:
            a = ''
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