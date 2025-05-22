from pytokr  import item, items
from arbre_binari_amb_nodes import ArbreBinari
# from arbre_binari import ArbreBinari

class Patro(ArbreBinari):
    # A completar pel grup d'estudiants com a part de la pràctica

    # * Un getter de si mateix, per facilitar el reset en la codificació *
    def patro(self):
        return self
    
    # *** Mètode que llegeix el patró en preordre de manera que modifica el patró que abans estava buit ***
    def llegeix(self):

        '''
        Pre: rep el recorregut en preordre del patró
        Post: retorna el patró (arbre binari)
        '''

        # Construeix l'arbre binari de l'objecte Patro a partir d'una sequencia en preordre
        # self: Instància de la classe Patro (per exemple, 'p' a program.py)
        
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


    # *** Mètode per imprimir el patró ***
    def escriu(self):
        return self._escriu_b()

    # ------------------------------------------------------------------------------------------------------------------
    # ** Mètode intern que farem servir a 'escriu' **
    def _escriu_b(self, primer_cop=True):

        '''
        Pre: rep el patró (self)
        Post: imprimeix el patró
        '''

        # ** Cas base **: si el patró és buit, imprimim ()
        if self.buit(): 
                print("()", end="")
        
        # ** Cas recursiu **:
        else:
            print("(", end="")                          # imprimim (
            print(self.valor_arrel(), end="")           # imprimim l'arrel del patró
            self.fill_esq()._escriu_b(False)            # imprimim el fill esquerre de l'arrel
            self.fill_dre()._escriu_b(False)            # imprimim el fill dret de l'arrel                  
            
            if primer_cop:
                print(")")                              # imprimim ) fent un salt de línia (això passa quan estem a l'arrel (primer_cop=True))
            
            else:               
                print(")", end="")                      # imprimim ) sense salt de línia (això passa quan estem a dins del patró (primer_cop=False)
                                                        # , o sigui, o bé estem al subpatró esquerre de l'arrel o al subpatró dret de l'arrel
    # ------------------------------------------------------------------------------------------------------------------



    # *** Mètode que codifica el missatge a partir d'una mida de bloc 'b'***
    def codifica(self, missatge, b): 

        # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', 
        # dividint-lo en blocs de mida 'b'

        # no destructiva
        # recursiu
        # ** Fórmula que ens permet codificar: chr(32 + (ord(c)+d-32)%95) **

        return self._funcio_DRY(missatge, b, "codifica")



    def decodifica(self, missatge, b):

        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
        # en blocs de mida 'b' 

        # ** Fórmula que ens permet descodificar: chr(32 + (ord(c)-d+63)%95) **

        return self._funcio_DRY(missatge, b, "decodifica")



    # ------------------------------------------------------------------------------------------------------------------

    # ***************************************************************
    # ** Mètodes interns per als mètodes codifica() i decodifica() **
    # ***************************************************************

    # ** Mètode intern que ens ajudarà a codificar o a descodificar el missatge **
    def _funcio_DRY(self, missatge, b, instr):

        '''
        Pre: rep un missatge que vol codificar o descodificar (segons el paràmetre 'instr') dividit en blocs de mida b
        Post: retorna el missatge una vegada codificat o descodificat 
        '''

        blocks = [missatge[i:i+b] for i in range(0, len(missatge), b)]       # Dividim el missatge en un bloc de b caràcters
        missatge_resultant = ''         # variable on guardarem el missatge codificat o decodificat

        # Obtenim cada missatge de blocks
        for block in blocks: 


            # Pas 1: El missatge es transforma en un arbre binari de caràcters el més complet possible
            arbre_missatge = self._trans_missatge_arbre(block)          # transformem el missatge en un arbre binari
            arbre_resultant = self._modificar(arbre_missatge, self.patro(), instr)           # obtenim l'arbre codificat o decodificat
            llista_missatge = arbre_resultant.nivells()         # fem un recorregut per nivell de l'arbre binari per tal d'obtenir el missatge codificat o decodificat
            missatge_resultant += "".join(llista_missatge)        # obtenim el missatge codificat o decodificat


        # Retornem el missatge codificat o decodificat
        return missatge_resultant


    # ** Mètode intern per transformar el missatge en un arbre binari **
    def _trans_missatge_arbre(self, missatge): 

        '''
        Pre: rep un missatge (string) que vol convertir en un arbre binari que conté el missatge
        Post: retorna un arbre binari amb els caràcters del missatge com a nodes
        '''

        # Hem de transformar el missatge en un arbre binari (hem d'utilitzar la idea del Heap, és a dir, 
        # els fills d'un arrel és 2k (fill_esq) i 2k+1 (fill_dre)). Posarem un None a la primera posició. 

        # ** Cas base ** 
        if not missatge:                # ja no tenim cap caràcter a transformar (llista buida)
            return ArbreBinari()      


        caracters = [None] + list(missatge)         # llista on la primera posició és None, per tal de poder aplicar la idea del Heap
                                                    # 2k ==> fill esquerre i 2k+1 ==> fill dret


        # ** Funció auxiliar que ens permet crear l'arbre binari **
        def f(index, n): 

            if index >= n:                                            # es compleix aquesta condició <=> el caràcter no té o bé un fill esq
                return ArbreBinari()                                  # o bé un fill dret

            left = f(2*index, n)                                      # obtenim el fill esq del caràcter a la posició 'índex'
            right = f((2*index) + 1, n)                               # obtenim el fill dret del caràcter a la posició 'índex'
            return ArbreBinari(caracters[index], left, right)         # retornem una instància d'ArbreBinari() que té com a arrel el caràcter
                                                                      # i els seus fills corresponents.

        return f(1, len(caracters))     



    # ** Mètode intern per tal de modificar l'arbre missatge i modificar-lo perquè sigui directament l'arbre amb  el missatge codificat **
    def _modificar(self, arbre, patro, instr):

        '''
        self: patró que ens serveix per saber, per exemple, si el node de l'arbre té un fill esq veure si el patró també té un fill esq o no. 
              També veiem amb el fill dret. 
        arbre: arbre missatge que conté els caràcters a codificar o a descodificar
        patro: retornem tot el patró per tal de fer reset
        instr: instrucció per saber si s'ha de codificar o de descodificar
        '''

        # Anem modificant l'arbre missatge de manera que l'arbre missatge que ens retorna al final, sigui l'arbre que conté el missatge codificat
        # Comencem des de l'arrel de l'arbre missatge

        # Fem una copia del patro per poder fer reset en qualsevol moment de la recursio 
        # Com que la codificacio i decodificacio fan el mateix proces, aprofitem aquesta funcio
        
        # Si la instrucció és 'codifica', codifiquem el node actual que conté el caràcter a codificar de l'arbre missatge
        if instr == "codifica":
            arbre.modificar_valor_arrel(chr(32 + (ord(arbre.valor_arrel()) + self.valor_arrel() - 32) % 95))
        
        # Si la instrucció és 'decodifica', decodifiquem el node actual de l'arbre missatge
        elif instr == "decodifica":
            arbre.modificar_valor_arrel(chr(32 + (ord(arbre.valor_arrel()) - self.valor_arrel() + 63) % 95))



        # Una vegada codificat el node, mirem el subarbre esq i el subarbre dret i fem el mateix pas anterior (recursivament)

        # Si aquest node de l'arbre té fill esquerre...
        if not arbre.fill_esq().buit():

            # ...però el node del patró no, llavors comencem de nou (reset) des de l'arrel del patró, 
            # evaluant en el fill esquerre d'aquest node de l'arbre.
            if self.fill_esq().buit():
                patro._modificar(arbre.fill_esq(), patro, instr)

            # ...i el node del patro també té fill esquerre, llavors PERFECTE ✅, 
            # cridem recursivament la funció per avaluar el fill esquerre de l'arbre
            # amb el fill esquerre del patró.
            elif not self.fill_esq().buit(): 
                self.fill_esq()._modificar(arbre.fill_esq(), patro, instr)


        # Anàlogament, si el node de l'arbre té fill dret...
        if not arbre.fill_dre().buit():
            # ...però el node del patró no, llavors comencem de nou (reset) des de l'arrel del patró, 
            # evaluant en el fill dret d'aquest node de l'arbre.
            if self.fill_dre().buit():
                patro._modificar(arbre.fill_dre(), patro, instr)

            # ...i el node del patro també té fill dret, llavors PERFECTE ✅, 
            # cridem recursivament la funció per avaluar el fill dret de l'arbre
            # amb el fill dret del patró.
            elif not self.fill_dre().buit():
                self.fill_dre()._modificar(arbre.fill_dre(), patro, instr)

        # Per a quan el node del l'arbre no té fills, llavors no cal fer res, ja que
        # no hi ha més espai per posar el patró.
        return arbre
    
    # ------------------------------------------------------------------------------------------------------------------