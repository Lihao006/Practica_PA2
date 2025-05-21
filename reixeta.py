from pytokr import item


class Reixeta():
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self, n=None, k=None):

        self._n = n                     # tenim una matriu nxn
        self._k = k                     # k: nombre de forats
        self._forats = []               # llista per guardar les posicions inicials dels forats
        self._forats_rotacions = []     # llista on guardarem les 4 rotacions


    
    # ** Getters **
    def valor_n(self):
        return self._n
    
    def valor_k(self):
        return self._k
    
    def lst_forats(self):
        return self._forats



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
        if self.valor_k() != (self.valor_n() * self.valor_n()) // 4:
            return -2

        #Es compleix k = n^2/4)
        # Per afegir les posiciones dels forats
        for _ in range(self.valor_k()): 
            i = int(item())
            j = int(item())
            self._forats.append((i, j))


        forats_rotacions = [[] for _ in range(4)]       # guardarem les 4 rotacions


        # Comprovem que les posicions dels forats són correctes i si els girs de la reixeta (90, 180 i 270 graus) 
        # cobreixen totes les posicions
        for i, j in self._forats: 
            if not (1 <= i <= self.valor_n() and 1 <= j <= self.valor_n()): 

                return -1   # retornem -1 si les posicions i,j no són vàlides

            forats_rotacions[0].append((i,j))                                           # Original, 0º
            forats_rotacions[1].append((self.valor_n()-j+1, i))                         # 90º
            forats_rotacions[2].append((self.valor_n()-i+1, self.valor_n()-j+1))        # 180º      
            forats_rotacions[3].append((j,self.valor_n()-i+1))                          # 270º
            

        totes_posicions = set()
        for sub_lst in forats_rotacions: 
            totes_posicions.update(sub_lst)         # aquí bàsicament el que fem és posar totes les tuples posicions de les 4 rotacions en 'totes_posicions'
                                                    # per tal de veure si hem repetit algun forat o no

            
        # Mirem si els 4k forats de la unió de les quatre reixetes cobreixen les n^2 posicions de la matriu
        if len(totes_posicions) != (self.valor_n() * self.valor_n()): 
            return - 1
        
        # Obtenim les posicions de les 4 rotacions ordenades. Això és molt útil i eficient perquè ja no ens caldria recalcular les posicions en altres mètodes de la classe
        self._forats_rotacions = [sorted(fila) for fila in forats_rotacions]

        # 1: Si les condicions anteriors no s'han complert ==> és una reixeta vàlida ✅
        return 1
    



    # Funció per escriure els forats de la reixeta després de cada gir antihorari 
    def escriu(self):
        
        # Imprimim la dimensió (n) de la reixeta i el nombre de forats (k)
        print(self.valor_n(), self.valor_k())


        #Imprimim les posicions dels forats (0º, 90º, 180º, 270º)

        for rotacio in self._forats_rotacions: 

            print(" ".join(f"({i},{j})" for i, j in rotacio))



    def codifica(self, missatge): 

        # codifiquem el 'missatge'

        block_size = self.valor_n() * self.valor_n()
        blocks = [missatge[i:i+block_size] for i in range(0, len(missatge), block_size)]       # Dividim el missatge en un bloc de n^2 caràcters
        missatge_codificat = ''

        # Obtenim cada missatge de blocks
        for block in blocks: 

            # Reomplim el bloc abans d'encriptar si i només si no es completa amb caràcters del text
            block = block + ' ' * (block_size - len(block)) if len(block) < block_size else block


            # Creem una matriu buida de None
            matriu = [[' ' for _ in range(self.valor_n())] for _ in range(self.valor_n())]

            # Posem els primers k caràcters del bloc en la matriu buida (atenció, la matriu comença per 0 però les posicions
            # dels forats comencem per 1). 
            lletra = 0

            # Obtinc les posicions dels forats de cada rotació/gir
            for rotacio in self._forats_rotacions: 

                # Obtinc la fila 'i' i la columna 'j'
                for i,j in rotacio: 

                    if lletra < len(block): 
                        matriu[i-1][j-1] = block[lletra]
                        lletra += 1


            # Recorrem la matriu per retornar el missatge codificat
            bloc_codificat = ""

            for fila in matriu: 
                bloc_codificat += "".join(fila)

            missatge_codificat += bloc_codificat


        # Retornem el missatge codificat
        return missatge_codificat
                

    


    def decodifica(self, missatge): 

        # decodifiquem el missatge
        # si es itera per cada fila
        # sigui una llista de n*n caracters, comencem a escriure per cada n posicio
        
        # si es itera per cada columna
        # anar girant i posant els caracters


        # Nosaltres iterarem per cada fila.
        # Creem una llista buida de None de mida n*n per anar guardant el missatge original.
        '''missatge_orig = ""


        for forats in self._forats_rotacions:
            for forat in forats:
                i,j = forat
                missatge_orig += missatge[(i-1)*self.valor_n() + j-1]
        
        return missatge_orig'''


        # Mitjançant blocs: 

                # codifiquem el 'missatge'

        block_size = self.valor_n() * self.valor_n()
        blocks = [missatge[i:i+block_size] for i in range(0, len(missatge), block_size)]       # Dividim el missatge en un bloc de n^2 caràcters
        missatge_original = ''

        # Obtenim cada missatge de blocks
        for block in blocks: 

            # Reomplim el bloc abans d'encriptar si i només si no es completa amb caràcters del text
            block = block + ' ' * (block_size - len(block)) if len(block) < block_size else block


            # Creem una matriu buida de None
            matriu = [[' ' for _ in range(self.valor_n())] for _ in range(self.valor_n())]

            # Posem els primers k caràcters del bloc en la matriu buida (atenció, la matriu comença per 0 però les posicions
            # dels forats comencem per 1). 
            idx = 0

            # Obtinc la fila 'i' i la columna 'j'
            for i in range(self._n): 
                for j in range(self._n): 
                    matriu[i][j] = block[idx]
                    idx += 1

            bloc_original = ''

            # Obtinc les posicions dels forats de cada rotació/gir
            for rotacio in self._forats_rotacions: 
                for i,j in rotacio: 
                    bloc_original += matriu[i-1][j-1]

            missatge_original += bloc_original


        # Retornem el missatge original (descodificat)
        return missatge_original
    




    def valid(self, missatge): 

        '''
        missatge: llegeixo una línia de text: Missatge xifrat
        '''

        # Ha de retornar un booleà
        return ((len(missatge) % (self.valor_n() * self.valor_n())) == 0)