from pytokr import item
import copy


class Reixeta():
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self, n=None, k=None):

        self._n = n                     # tenim una matriu nxn
        self._k = k                     # k: nombre de forats
        self._forats = []       
        self._matriu = None             # matriu de referència als forats de la reixeta



    def llegeix(self):

        # llegim la entrada de dimensions (n,k) i les posicions dels forats de la reixeta

        # Aquí ha de retornar un status que pot ser: 
        # 1: la reixeta és vàlida 
        # -1: els girs de la reixeta no cobreixen totes les posicions
        # -2: les dimensions són incorrectes (k diferent de n^2/4)


        self._n = int(item())           # Llegim la dimensió n
        self._k = int(item())           # Llegim el nombre de forats k

        # -2: comprovem si que les dimensions són correctes (k és igual a n^2/4)
        if self._k != (self._n * self._n) // 4:
            return -2


        for _ in range(self._k): 
            i = int(item())
            j = int(item())
            self._forats.append((i, j))


        # comprovem si els girs de la reixeta (90, 180 i 270 graus) cobreixen totes les posicions
        self._matriu = [[False for j in range(self._n)] for i in range(self._n)]            # creem una matriu nxn amb tots els elements a False


        # comprova si que els girs de la reixeta cobreixen totes les posicions
        if self._forats: 
            
            for i, j in self._forats: 
                assert 1 <= i <= self._n and 1 <= j <= self._n

                i -= 1              # índex 'i' normalitzat
                j -= 1              # índex 'j' normalitzat

                self._matriu[i][j] = True                                   # marquem com a visitat el forat original
                self._matriu[self._n - 1 - j][i] = True                     # marquem com a visitat el forat després d'haver girat 90 graus
                self._matriu[self._n - 1 - i][self._n - 1 - j] = True       # marquem com a visitat el forat després d'haver girat 180 graus
                self._matriu[j][self._n - 1 - i] = True                     # marquem com a visitat el forat després d'haver girat 270 graus

        # Comprovem si hi ha duplicats o no
        if len(set(self._forats)) != self._k: 
            return -1
        
        # comprovem que les posicions dels forats són correctes
        for i, j in self._forats: 
            if not (1 <= i <= self._n and 1 <= j <= self._n): 
                return -1

        # evitar duplicats i si els girs de la reixeta (90, 180 i 270 graus) cobreixen totes les posicions
        posicions = set()
        for i, j in self._forats: 
            posicions.add((i-1, j-1))                               # Original
            posicions.add((self._n - 1 - j, i-1))                   # 90 graus
            posicions.add((self._n - 1 - i, self._n - 1 - j))       # 180 graus
            posicions.add((j-1, self._n - 1 - i))                   # 270 graus

        # comprovem si els girs de la reixeta (90, 180 i 270 graus) cobreixen totes les posicions
        self._matriu = [[False for j in range(self._n)] for i in range(self._n)]            # creem una matriu nxn amb tots els elements a False


        # Mirem si els 4k forats de la unió de les quatre reixetes cobreixen les n2 posicions de la matriu
        if len(posicions) != self._n * self._n: 
            return - 1
        
        # Matriu que ens ajudarà en el mètode codifica()
        self._matriu = [[False for _ in range(self._n)] for _ in range(self._n)]
        for i, j in self._forats:
            self._matriu[i-1][j-1] = True


        # 1: Si les condicions anteriors no s'han complert ==> és una reixeta vàlida
        return 1
    
    # funcio per escriure els forats de la reixeta
    def escriu(self):

        # mostrem les dimensions (n,k) i les posicions dels forats per a la reixeta i els seus girs
        print(self._n, self._k)
        
        def escriu_forats(matriu):
            for i in range(self._n):
                for j in range(self._n):
                    if matriu[i][j]:
                        print(f"({i+1}, {j+1})", end=" ")
            print()

        # funcio per girar la matriu, nomes funciona be per a reixetes valides
        def girar(matriu, gir):
            # sigui "gir" el nombre de graus a girar la matriu (90, 180 o 270)
            assert gir == 90 or gir == 180 or gir == 270
            matriu_nova = [[False for j in range(self._n)] for i in range(self._n)]
            
            for i in range(0, self._n):
                for j in range(0, self._n):
                    if matriu[i][j]:
                        if gir == 90:
                            matriu_nova[self._n - 1 - j][i] = True
                        elif gir == 180:
                            matriu_nova[self._n - 1 - i][self._n - 1 - j] = True
                        elif gir == 270:
                            matriu_nova[j][self._n - 1 - i] = True
            return matriu_nova



        # si transposem la matriu per defecte, obtenim el gir_180 graus
        # fixem-nos que n ha de ser si o si parell, ja que si fos senar, hi hauria una casella en el centre
        # de la matriu de manera que, o bé aquesta casella mai és forat, o bé sempre ho és (per tant mai no pot ser una reixeta vàlida),
        # ja que per molt que girem la matriu, la casella del centre no es mou
        
        self._matriu_reix = [[False for j in range(self._n)] for i in range(self._n)]

        for i, j in self._forats:
                self._matriu_reix[i-1][j-1] = True

        # forats originals
        escriu_forats(self._matriu_reix)               

        m90 = girar(self._matriu_reix, 90)                                    
        
        # forats girats 90 graus
        escriu_forats(m90)              

        m180 = girar(self._matriu_reix, 180)

        # forats girats 180 graus
        escriu_forats(m180)            

        m270 = girar(self._matriu_reix, 270)

        # forats girats 270 graus
        escriu_forats(m270)               




        

        
        
        


    def codifica(self, missatge): 

        # codifiquem el 'missatge'

        pass



    def decodifica(self, missatge): 

        # decodifiquem el missatge

        pass
    


    def valid(self, missatge): 

        '''
        missatge: llegeixo una línia de text: Missatge xifrat
        '''

        # He de verificar que la mida del missatge és adeqüada per a la reixeta

        pass