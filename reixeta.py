from pytokr import item

class Reixeta():
    # A completar pel grup d'estudiants com a part de la pràctica

    # ** Mètode constructor on crearem algunes variables d'instància que ens seran úitls **
    def __init__(self, n=None, k=None):

        self._n = n                     # tenim una matriu nxn
        self._k = k                     # k: nombre de forats
        self._forats = []               # llista per guardar les posicions inicials dels forats
        self._forats_rotacions = []     # llista on guardarem les 4 rotacions


    
    # ** Getters **
    def valor_n(self):      # per saber la dimensió de la matriu
        return self._n
    
    def valor_k(self):      # per saber el nombre de forats
        return self._k


    # altres funcions 

    # *** Mètode per llegir la entrada de dimensions (n,k) i les posicions dels forats de la reixeta ****
    def llegeix(self):

        '''
        Pre: llegeix una sèrie d'entrades mitjançant pytokr, concretament, la entrada de dimensions (n,k) i les posicions dels forats de a reixeta.
        Post: retorn 1 si la reixeta és vàlida ✅, -1 si els girs de la reixeta no cobreixen totes les posicions ❌,
        -2: les dimensions són incorrectes (k diferent de n^2/4) ❌
        '''

        # Aquí ha de retornar un status que pot ser: 
        # 1: la reixeta és vàlida ✅
        # -1: els girs de la reixeta no cobreixen totes les posicions ❌
        # -2: les dimensions són incorrectes (k diferent de n^2/4) ❌

        self._n = int(item())           # Llegim la dimensió n
        self._k = int(item())           # Llegim el nombre de forats k

        # -2: comprovem si les dimensions són correctes (k és igual a n^2/4)
        if self.valor_k() != (self.valor_n() * self.valor_n()) // 4:
            return -2

        # Si la condició anterior no es compleix, ja sabrem que es complirà que k = n^2/4 ✅
        # Afegim les posicions dels forats en la variable d'instància 'self._forats'
        for _ in range(self.valor_k()): 
            i = int(item())                     # llegim la fila
            j = int(item())                     # llegim la columna
            self._forats.append((i, j))         # afegim (fila, columna) com a tupla

        forats_rotacions = [[] for _ in range(4)]       # llista on guardarem les 4 rotacions (0, 90, 180 i 270 graus)


        # Comprovem que les posicions dels forats són correctes i si els girs de la reixeta (90, 180 i 270 graus) 
        # cobreixen totes les posicions
        for i, j in self._forats: 
            if not (1 <= i <= self.valor_n() and 1 <= j <= self.valor_n()): 

                return -1   # retornem -1 si les posicions i,j no són vàlides

            forats_rotacions[0].append((i,j))                                           # Original, 0º
            forats_rotacions[1].append((self.valor_n()-j+1, i))                         # 90º
            forats_rotacions[2].append((self.valor_n()-i+1, self.valor_n()-j+1))        # 180º      
            forats_rotacions[3].append((j,self.valor_n()-i+1))                          # 270º
            

        totes_posicions = set()             # ens servirà per saber si hi ha alguna posició del forat repetida o no
        for sub_lst in forats_rotacions: 
            totes_posicions.update(sub_lst)         # aquí bàsicament el que fem és posar totes les tuples posicions de cada una de les 4 rotacions en 
                                                    # 'totes_posicions per tal de veure si hem repetit algun forat o no

            
        # Mirem si els 4k forats de la unió de les quatre reixetes cobreixen les n^2 posicions de la matriu
        if len(totes_posicions) != (self.valor_n() * self.valor_n()): 
            return -1
        
        # Obtenim les posicions de les 4 rotacions ordenades. Això és molt útil i eficient perquè ja no ens caldria recalcular les posicions en altres mètodes de la classe
        self._forats_rotacions = [sorted(fila) for fila in forats_rotacions]

        # 1: Si les condicions anteriors no s'han complert ==> és una reixeta vàlida ✅
        return 1
    


    # *** Mètode per escriure els forats de la reixeta després de cada gir antihorari ***
    def escriu(self):
        
        # Imprimim la dimensió (n) de la reixeta i el nombre de forats (k)
        print(self.valor_n(), self.valor_k())

        #Imprimim les posicions dels forats (0º, 90º, 180º, 270º)
        for rotacio in self._forats_rotacions: 
            print(" ".join(f"({i},{j})" for i, j in rotacio))



    # *** Mètode per codificar el missatge ***
    def codifica(self, missatge): 

        '''
        Pre: rep el missatge a codificar
        Post: retorna el missatge codificat
        '''

        block_size = self.valor_n() * self.valor_n()        # per dividir el missatge en blocks de mida n^2
        blocks = [missatge[i:i+block_size] for i in range(0, len(missatge), block_size)]       # Dividim el missatge en blocks de n^2 caràcters
        missatge_codificat = ''     # on posarem el missatge codificat

        # Obtenim els blocs en què s’ha dividit el missatge
        for block in blocks: 

            # Reomplim el bloc abans d'encriptar <=> no es completa amb caràcters del text
            block = block + ' ' * (block_size - len(block)) if len(block) < block_size else block

            # Creem una matriu buida d'espais buits ' '
            matriu = [[' ' for _ in range(self.valor_n())] for _ in range(self.valor_n())]

            # Posem els primers k caràcters del bloc en la matriu buida (ATENCIÓ!!: la matriu comença per 0 però les posicions
            # dels forats comencem per 1). 
            lletra = 0

            # Obtinc les posicions ordenades dels forats en cada rotació/gir
            for rotacio in self._forats_rotacions: 

                # Obtinc la fila 'i' i la columna 'j' del forat
                for i,j in rotacio: 

                    matriu[i-1][j-1] = block[lletra]       # poso el caràcter a la posició del forat corresponent
                    lletra += 1                            # pasem al següent caràcter a afegir


            # Recorrem la matriu per aconseguir el missatge codificat del bloc actual
            bloc_codificat = ""

            for fila in matriu: 
                bloc_codificat += "".join(fila)

            missatge_codificat += bloc_codificat


        # Retornem el missatge codificat
        return missatge_codificat
                

    

    # *** Mètode per descodificar el missatge ***
    def decodifica(self, missatge): 

        '''
        Pre: rep el missatge a descodificar
        Post: retorna el missatge descodificat
        '''


        block_size = self.valor_n() * self.valor_n()                # per dividir el missatge en blocks de mida n^2
        blocks = [missatge[i:i+block_size] for i in range(0, len(missatge), block_size)]       # Dividim el missatge en un bloc de n^2 caràcters
        missatge_original = ''          # on posarem el missatge descodificat

        # Obtenim els blocs en què s’ha dividit el missatge codificat
        for block in blocks: 

            # Creem una matriu buida d'espais buits ' '
            matriu = [[' ' for _ in range(self.valor_n())] for _ in range(self.valor_n())]

            idx = 0      # per posar el caràcter del missatge codificat en la matriu

            # El nostre objectiu és reconstruïr la matriu reixeta amb el missatge codificat: 
            # Obtinc la fila 'i' de la matriu 
            for i in range(self._n): 

                # Obtinc la columna 'j' de la matriu
                for j in range(self._n): 

                    matriu[i][j] = block[idx]       # posem el caràcter en la posició (i,j) de la matriu
                    idx += 1                        # posem el següent caràcter


            # Nota: El pas anterior és bàsicament reconstruïr la matriu reixeta que ens quedaria una vegada codificat. 
            # Ara el següent pas, és obtenir el missatge original que simplement és obtenir els caràcters en l'ordre 
            # que les hem afegit a través de les posicions dels forats

            bloc_original = ''      

            # Obtinc les posicions dels forats de cada rotació/gir
            for rotacio in self._forats_rotacions: 
                for i,j in rotacio: 
                    bloc_original += matriu[i-1][j-1]

            missatge_original += bloc_original


        # Retornem el missatge original (descodificat)
        return missatge_original
    



    # *** Mètode per comprovar si la mida del missatge és adequada per a la reixeta ***
    def valid(self, missatge): 

        # Ha de retornar un booleà
        return ((len(missatge) % (self.valor_n() * self.valor_n())) == 0)