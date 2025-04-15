from pytokr import item

class Reixeta():
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self, n=None, k=None):

        self._n = n                     # tenim una matriu nxn
        self._num_forats = k            # k: nombre de forats
        self._forats = []       
        self._matriu = None             # matriu de referència als forats de la reixeta



    def llegeix(self):

        # llegim la entrada de dimensions (n,k) i les posicions dels forats de la reixeta

        # Aquí ha de retornar un status que pot ser: 
        # 1: la reixeta és vàlida 
        # -1: els girs de la reixeta no cobreixen totes les posicions
        # -2: les dimensions són incorrectes (k diferent de n^2/4)


        self._matriu = [[False for _ in range(n)] for _ in range(n)]


        '''if forats:
            for element in forats:
                assert 1 <= i <= n and 1 <= j <= n

                i = element[0]                       # fila
                j = element[1]                       # columna
                self._matriu[i-1][j-1] = True        # marquem com a visitat a aquell forat'''

        pass

    
    def escriu(self):

        # mostrem les dimensions (n,k) i les posicions dels forats per a la reixeta i els seus girs
        print(self._num_fils, self._num_cols)
        # si transposem la matriu per defecte, obtenim el gir_180 graus
        # fixem-nos que n ha de ser si o si parell, ja que si fos senar, hi hauria una casella en el centre
        # de la matriu de manera que, o bé aquesta casella mai és forat, o bé sempre ho és (per tant mai no pot ser una reixeta vàlida),
        # ja que per molt que girem la matriu, la casella del centre no es mou



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
