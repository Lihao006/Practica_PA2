from pytokr import item


class Reixeta():
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self, n=None, k=None):

        self._n = n                     # tenim una matriu nxn
        self._k = k                     # k: nombre de forats
        self._forats = []               # llista per guardar les posicions dels forats
        self._matriu = None             # matriu de referència als forats de la reixeta


    '''    
    #Getters
    def valor_n(self):
        return self._n
    
    def valor_k(self):
        return self._k
    
    def nombre_forats(self):
        return self._forats
    
    def mostra_reixeta(self):
        return self._matriu

    '''


    # altres funcions 

    # (hem de fer servir pytokr)
    def llegeix(self):

        # llegim la entrada de dimensions (n,k) i les posicions dels forats de la reixeta

        # Aquí ha de retornar un status que pot ser: 
        # 1: la reixeta és vàlida ✅
        # -1: els girs de la reixeta no cobreixen totes les posicions ❌
        # -2: les dimensions són incorrectes (k diferent de n^2/4) ❌

        self._n = int(item())           # Llegim la dimensió n
        self._k = int(item())           # Llegim el nombre de forats k

        # -2: comprovem si les dimensions són correctes (k és igual a n^2/4)
        if self._k != (self._n * self._n) / 4:
            return -2

        #Es compleix k = n^2/4)
        # Per afegir les posiciones dels forats
        for _ in range(self._k): 
            i = int(item())
            j = int(item())
            self._forats.append((i, j))

        # Comprovem si hi ha duplicats o no
        if len(set(self._forats)) != self._k: 
            return -1
        

        # Comprovem que les posicions dels forats són correctes i si els girs de la reixeta (90, 180 i 270 graus) 
        # cobreixen totes les posicions
        posicions = set()
        
        for i, j in self._forats: 
            if (1 <= i <= self._n and 1 <= j <= self._n): 

                posicions.add((i, j))                                   # Original
                posicions.add((self._n - j + 1, i))                     # 90º
                posicions.add((self._n - i + 1, self._n - j + 1))       # 180º
                posicions.add((j, self._n - i + 1))                     # 270º


            else: 
                return -1


        # Mirem si els 4k forats de la unió de les quatre reixetes cobreixen les n2 posicions de la matriu
        if len(posicions) != self._n * self._n: 
            return - 1
        

        # 1: Si les condicions anteriors no s'han complert ==> és una reixeta vàlida ✅
        return 1
    





    '''def crear_matriu_buit(self):
        # funcio per crear una matriu tot de False de dimensions nxn
        # que ens servirà per saber on està cada forat de la reixeta
        return [[False for _ in range(self._n)] for _ in range(self._n)]
    




    # funcio per girar la matriu, nomes funciona be per a reixetes valides
    def girar(self, matriu, gir):
            # sigui "gir" el nombre de graus a girar la matriu (90, 180 o 270)
            assert gir == 90 or gir == 180 or gir == 270
            matriu_nova = self.crear_matriu_buit()
            
            for i in range(0, self._n):
                for j in range(0, self._n):
                    if matriu[i][j]:
                        if gir == 90:
                            matriu_nova[self._n - 1 - j][i] = True
                        elif gir == 180:
                            matriu_nova[self._n - 1 - i][self._n - 1 - j] = True
                        elif gir == 270:
                            matriu_nova[j][self._n - 1 - i] = True
            return matriu_nova'''
    


    # Funció per escriure els forats de la reixeta després de cada gir antihorari 
    def escriu(self):
        
        #Imprimim la dimensió (n) de la reixeta i el nombre de forats (k)
        print(self._n, self._k)


        # Imprimim les posicions dels forats

        # Imprimim les posicions dels forats originals
        print(" ".join(f"({i},{j})") for i, j in self._forats)

        # Imprimim les posicions dels forats després de 90 graus (antihorari)
        print(" ".join(f"({self._n - j + 1},{i})") for i, j in self._forats)

        # Imprimim les posicions dels forats després de 180 graus
        print(" ".join(f"({self._n - i + 1},{self._n - j + 1})") for i, j in self._forats)

        # Imprimim les posicions dels forats després de 270 graus
        print(" ".join(f"({j},{self._n - i + 1})") for i, j in self._forats)



        '''def escriu_forats(matriu):
            for i in range(self._n):
                for j in range(self._n):
                    if matriu[i][j]:
                        print(f"({i+1}, {j+1})", end=" ")
            print()

        # si transposem la matriu per defecte, obtenim el gir_180 graus
        # fixem-nos que n ha de ser si o si parell, ja que si fos senar, hi hauria una casella en el centre
        # de la matriu de manera que, o bé aquesta casella mai és forat, o bé sempre ho és (per tant mai no pot ser una reixeta vàlida),
        # ja que per molt que girem la matriu, la casella del centre no es mou
        
        self._matriu = self.crear_matriu_buit()    

        for i, j in self._forats:
                self._matriu[i-1][j-1] = True

        # forats originals
        escriu_forats(self._matriu)               

        m90 = self.girar(self._matriu, 90)                                    
        
        # forats girats 90 graus
        escriu_forats(m90)              

        m180 = self.girar(self._matriu, 180)

        # forats girats 180 graus
        escriu_forats(m180)            

        m270 = self.girar(self._matriu, 270)

        # forats girats 270 graus
        escriu_forats(m270)'''           





    def codifica(self, missatge): 

        #codifiquem el 'missatge'

        block_size = self._n * self._n 
        blocks = [missatge[i:block_size+1] for i in range(0, len(missatge), block_size)]


        for block in blocks: 

            




            #Creem una matriu buida de None.
            matriu_buida = [[None for _ in range(self._n)] for _ in range(self._n)]

            # Convertim el missatge en una llista, d'aquesta manera podrem obtenir cada lletra.
            missatge_lst = list(missatge)

            # Posem els primers k caràcters del bloc en la matriu buida (atenció, la matriu comença per 0 però les posicions
            # dels forats comencem per 1). 
            lletra = 0
            





        while lletra < (self._n * self._n): 
            for i, j in sorted(self._forats): 
                matriu_buida[i-1][j-1] = missatge_lst[lletra]
                lletra += 1


            for i, j in sorted((self._n - j + 1, i) for i, j in self._forats): 
                matriu_buida[i-1][j-1] = missatge_lst[lletra]
                lletra += 1

            for i, j in sorted((self._n - i + 1, self._n - j + 1) for i, j in self._forats): 
                matriu_buida[i-1][j-1] = missatge_lst[lletra]
                lletra += 1

            for i, j in sorted((j, self._n - i + 1) for i, j in self._forats): 
                matriu_buida[i-1][j-1] = missatge_lst[lletra]
                lletra += 1


        # Recorrem la matriu per retornar el missatge codificat
        codi = ''        # ** Variable que ens servirà per concatenar les lletres **

        for fila in matriu_buida:                               # Obtenim cada fila de matriu 
            for element in fila:                                # Obtenim cada element de cada fila
                codi += element if element is not None else ' '            

        # Retornem el missatge codificat
        return codi
                

    


    def decodifica(self, missatge): 

        # decodifiquem el missatge
        # si es itera per cada fila
        # sigui una llista de n*n caracters, comencem a escriure per cada n posicio
        
        # si es itera per cada columna
        # anar girant i posant els caracters
        pass
    




    def valid(self, missatge): 

        '''
        missatge: llegeixo una línia de text: Missatge xifrat
        '''

        # He de verificar que la mida del missatge és adeqüada per a la reixeta

        pass