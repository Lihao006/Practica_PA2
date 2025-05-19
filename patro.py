from pytokr  import item, items
from arbre_binari_amb_nodes import ArbreBinari
# from arbre_binari import ArbreBinari

class Patro(ArbreBinari):
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self, valor=None, fill_esq=None, fill_dre=None): 
        super().__init__(valor, fill_esq, fill_dre)


    # Un getter de si mateix, per facilitar el reset en la codificació
    def patro(self):
        return self
    

    def llegeix(self):

        # Construeix l'arbre binari de l'objecte Patro a partir d'una sequencia en preordre
        # self: Instància de la classe Patro (per exemple, p a program.py)
        
        # Llegeix el següent valor de la sequencia en preordre amb item() 
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
            # no cal fer un cas else, ja que si x == -1, ja tenim definit un Patro buit i no caldra fer res



    def escriu(self):
        return self._escriu_b()



    def _escriu_b(self, primer_cop=True):

        # ** Cas base **: si l'arbre binari és buit, imprimim ()
        if self.buit(): 
                print("()", end="")
        
        else:
            # ** Cas recursiu 1 **
            print("(", end="")                         # imprimim (
            print(self.valor_arrel(), end="")          # imprimim l'arrel
            self.fill_esq()._escriu_b(False)            # imprimim el fill esquerre de l'arrel
            self.fill_dre()._escriu_b(False)            # imprimim el fill dret de l'arrel                  
            
            if primer_cop:
                print(")")                             # imprimim ) saltant de linia
            
            else:               
                print(")", end="")                     # imprimim ) sense saltar de linia




    def _funcio_DRY(self, missatge, b, instr):
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

            arbre_codificat = self._modificar(arbre_missatge, self.patro(), instr)              # obtenim el mosaic de l'arbre missatge
            llista_missatge = arbre_codificat.nivells()
            missatge_codificat += "".join(llista_missatge)        # obtenim el missatge codificat a partir de l'arbre codificat


            # Pas 3: Substituïm cada caràcter de l’arbre-missatge pel resultat de sumar-li circularment 
            # l’enter situat en la seva posició corresponent al mosaic. El text encriptat s’obté desfent la 
            # transformació del pas 1 a partir d’aquest tercer arbre.
            # bloc_codificat = self._suma_circular(arbre_missatge, arbre_mosaic)



        # Retornem el missatge codificat
        return missatge_codificat




    def codifica(self, missatge, b): 

        # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', 
        # dividint-lo en blocs de mida 'b'


        # no destructiva
        # recursiu
        # chr(32 + (ord(c)+d-32)%95)

        return self._funcio_DRY(missatge, b, "codifica")
        """
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

            arbre_codificat = self._mosaic(arbre_missatge, "codifica")             # obtenim el mosaic de l'arbre missatge
            llista_missatge = arbre_codificat.nivells()
            missatge_codificat += "".join(llista_missatge)        # obtenim el missatge codificat a partir de l'arbre codificat


            # Pas 3: Substituïm cada caràcter de l’arbre-missatge pel resultat de sumar-li circularment 
            # l’enter situat en la seva posició corresponent al mosaic. El text encriptat s’obté desfent la 
            # transformació del pas 1 a partir d’aquest tercer arbre.
            # bloc_codificat = self._suma_circular(arbre_missatge, arbre_mosaic)



        # Retornem el missatge codificat
        return missatge_codificat
        """

    # ------------------------------------------------------------------------------------------------------------------

    # ***********************************************
    # ** Funcions privats per al mètode codifica() **
    # ***********************************************


    # Función privat per transformar el missatge en un arbre binari
    def _trans_missatge_arbre(self, missatge): 

        # ** Cas base ** 
        if not missatge: 
            return Patro()


        caracters = [None] + list(missatge)         # llista on la primera posició és None, per tal de poder aplicar la idea del Heap
                                                    # 2k ==> fill esquerre i 2k+1 ==> fill dret


        # Funció auxiliar que ens permet crear l'arbre binari
        def f(index, n): 

            if index >= n: 
                return Patro()

            left = f(2*index, n)
            right = f((2*index) + 1, n)
            return Patro(caracters[index], left, right)

        return f(1, len(caracters))




    # Funció privat que copiar l'arbre binari que hem obtingut de la transformació del missatge
    def _copia(self):

        # ** Cas base **
        if self.buit(): 
            return Patro()
        

        # ** Cas recursiu **
        else: 

            left = self.fill_esq()._copia()
            right = self.fill_dre()._copia()
            return Patro(self.valor_arrel(), left, right)



    # Funció privat per posar el patró en l'arbre binari que conté el missatge
    def _mosaic(self, arbre_missatge, instr): 

        """
        mosaic = Patro()
        if arbre_missatge.buit():
            return mosaic
        elif arbre_missatge.fulla():
            mosaic._modificar_valor_arrel(self.valor_arrel())
            return mosaic
        else: # Si no esta buida ni es una fulla, llavors te fills
            if not self.fill_esq().buit():

            elif self.fill_esq().buit():
                mosaic.modificar_fill_esq()

            if self.fill_dre().buit():
                
            elif self.fill_dre().buit():
                mosaic.modificar_fill_dre()
        """
        mosaic = arbre_missatge._copia()              # copiem l'arbre binari que conté el missatge que volem codificar
        return self._modificar(mosaic, self.patro(), instr) 



    def _modificar(self, arbre, patro, instr):
        # Suposem que el mosaic no es buit
        # Anem modificant l'arbre copiat per convertir-lo en el mosaic
        # Comencant des de l'arrel de l'arbre
        # Fem una copia del patro per poder fer reset en qualsevol moment de la recursio 
        # Com que la codificacio i decodificacio fan el mateix proces, aprofitem aquesta funcio
        if instr == "codifica":
            arbre._modificar_valor_arrel(chr(32 + (ord(arbre.valor_arrel()) + self.valor_arrel() - 32) % 95))
        
        elif instr == "decodifica":
            arbre._modificar_valor_arrel(chr(32 + (ord(arbre.valor_arrel()) - self.valor_arrel() + 63) % 95))


        # Si aquest node de l'arbre te fill esquerre
        if not arbre.fill_esq().buit():
            # pero el node del patro no, llavors comencem de nou (reset) des de l'arrel del patro, 
            # evaluant en el fill esquerre d'aquest node de l'arbre.
            if self.fill_esq().buit():
                patro._modificar(arbre.fill_esq(), patro, instr)
            # si el node del patro tambe te fill esquerre, llavors perfecte, 
            # cridem recursivament la funcio per avaluar el fill esquerre de l'arbre
            # amb el fill esquerre del patro.
            elif not self.fill_esq().buit(): 
                self.fill_esq()._modificar(arbre.fill_esq(), patro, instr)


        # Analogament, si el node de l'arbre te fill dret
        if not arbre.fill_dre().buit():
            # pero el node del patro no, llavors comencem de nou (reset) des de l'arrel del patro, 
            # evaluant en el fill dret d'aquest node de l'arbre.
            if self.fill_dre().buit():
                patro._modificar(arbre.fill_dre(), patro, instr)
            # si el node del patro tambe te fill dret, llavors perfecte, 
            # cridem recursivament la funcio per avaluar el fill dret de l'arbre
            # amb el fill dret del patro.
            elif not self.fill_dre().buit():
                self.fill_dre()._modificar(arbre.fill_dre(), patro, instr)

        # Per a quan el node del l'arbre no te fills, llavors no cal fer res, ja que
        # no hi ha mes espai per posar el patro.
        return arbre




    # ------------------------------------------------------------------------------------------------------------------


    def decodifica(self, missatge, b):

        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
        # en blocs de mida 'b' 
        # chr(32 + (ord(c)-d+63)%95)

        return self._funcio_DRY(missatge, b, "decodifica")