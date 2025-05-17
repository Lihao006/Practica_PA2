from pytokr  import item, items
from arbre_binari_amb_nodes import ArbreBinari
# from arbre_binari import ArbreBinari

class Patro(ArbreBinari):
    # A completar pel grup d'estudiants com a part de la pràctica


    def llegeix(self):

        # Construeix l'arbre binari de l'objecte Patro a partir d'una seqüència en preordre
        # self: Instància de la classe Patro (per exemple, p a program.py)
        
        # Llegeix el següent valor de la seqüència en preordre amb item() 
        x = int(item())

        if x != -1: 
            l = Patro()
            l.llegeix()                      # obtenim el fill esquerre
            r = Patro()
            r.llegeix()                      # obtenim el fill dret             
            # modifiquem aquest patro amb l'arrel 'x', fill esquerre 'l' i fill dret 'r'
            self.modificar_valor_arrel(x)
            self.modificar_fill_esq(l)
            self.modificar_fill_dre(r)
            # no cal fer un cas else, ja que si x == -1, ja tenim definit un Patro buit i no caldrà fer res



    def escriu(self): 
        
        # ** Cas base **: si l'arbre binari és buit, imprimim ()
        if self.buit(): 
            print("()", end="")

        # ** Cas recursiu **
        else: 
            print("(", end="")                         # imprimim (
            print(self.valor_arrel(), end="")           # imprimim l'arrel
            self.fill_esq().escriu()                    # imprimim el fill esquerre de l'arrel
            self.fill_dre().escriu()                    # imprimim el fill dret de l'arrel
            print(")", end="")                         # imprimim )



    def codifica(self, missatge, b): 

        # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', 
        # dividint-lo en blocs de mida 'b'


        # no destructiva
        # recursiu
        # chr(32 + (ord(c)+d-32)%95)


        # Hem de transformar el missatge en un arbre binari (hem d'utilitzar la idea del Heap, és a dir, 
        # els fills d'un arrel és 2k (fill_esq) i 2k+1 (fill_dre)). Posarem un None a la primera posició. 


        blocks = [missatge[i:i+b] for i in range(0, len(missatge), b)]       # Dividim el missatge en un bloc de b caràcters
        missatge_codificat = ''

        # Obtenim cada missatge de blocks
        for block in blocks: 


            # Pas 1: El missatge es transforma en un arbre binari de caràcters el més complet possible
            arbre_missatge = self._trans_missatge_arbre(block)          # transformem el missatge en un arbre binari

            # Pas 2: Un cop copiat el missatge a l'arbre, s'obté un segon arbre, aquesta vegada d'enters, amb la mateixa 
            # estructura que el primer. Aquest segon arbre es construeix replicant el patró totalment o parcialment 
            # tantes vegades com sigui necessari, utilitzant fragments tan grans com sigui possible, començant per 
            # l'arrel. A aquest segon arbre l'anomenem mosaic. 

            arbre_mosaic = self._mosaic(arbre_missatge)             # obtenim el mosaic de l'arbre missatge


            # Pas 3: Substituïm cada caràcter de l’arbre-missatge pel resultat de sumar-li circularment 
            # l’enter situat en la seva posició corresponent al mosaic. El text encriptat s’obté desfent la 
            # transformació del pas 1 a partir d’aquest tercer arbre.
            bloc_codificat = self._suma_circular(arbre_missatge, arbre_mosaic)



        # Retornem el missatge codificat
        return missatge_codificat


    # ------------------------------------------------------------------------------------------------------------------

    # ***********************************************
    # ** Funcions privats per al mètode codifica() **
    # ***********************************************


    # Función privat per transformar el missatge en un arbre binari
    def _trans_missatge_arbre(self, missatge): 

        # ** Cas base ** 
        if not missatge: 
            return ArbreBinari()


        caracters = [None] + list(missatge)         # llista on la primera posició és None, per tal de poder aplicar la idea del Heap
                                                    # 2k ==> fill esquerre i 2k+1 ==> fill dret


        # Funció auxiliar que ens permet crear l'arbre binari
        def f(index, n): 

            if index >= n: 
                return ArbreBinari()

            left = f(2*index, n)
            right = f((2*index) + 1, n)
            return ArbreBinari(caracters[index], left, right)

        return f(1, len(caracters))




    # Funció privat que copiar l'arbre binari que hem obtingut de la transformació del missatge
    def _copia(self):

        # ** Cas base **
        if self.buit(): 
            return ArbreBinari()
        

        # ** Cas recursiu **
        else: 

            left = self.fill_esq()._copia()
            right = self.fill_dre()._copia()
            return ArbreBinari(self.valor_arrel(), left, right)



    # Funció privat per posar el patró en l'arbre binari que conté el missatge
    def _mosaic(self, arbre_missatge): 

        mosaic = arbre_missatge._copia()              # copiem l'arbre binari que conté el missatge que volem codificar
        
        pass



    # Funció privat per fer la suma circular
    def _suma_circular(self, arbre_missatge, arbre_mosaic): 

        # Obtenim 
        pass









    # ------------------------------------------------------------------------------------------------------------------








    def decodifica(self, missatge, b):

        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
        # en blocs de mida 'b' 
        # chr(32 + (ord(c)-d+63)%95)

        pass