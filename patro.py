from pytokr  import item, items
from arbre_binari_amb_nodes import ArbreBinari
# from arbre_binari import ArbreBinari

class Patro(ArbreBinari):
    # A completar pel grup d'estudiants com a part de la pràctica


    # Getter
    def valor_n(self):
        return self._n


    def llegeix(self):

        # Construeix l'arbre binari de l'objecte Patro a partir d'una seqüència en preordre
        # self: Instància de la classe Patro (per exemple, p a program.py)
        
        # Llegeix el següent valor de la seqüència en preordre amb item() 
        x = int(item())

        if x == -1: 
            l = self.llegeix()                      # obtenim el fill esquerre
            r = self.llegeix()                      # obtenim el fill dret
            return ArbreBinari(x,l,r)               # construïm l'arbre amb l'arrel 'x', fill esquerre 'l' i fill dret 'r'

        else:
            return ArbreBinari()                    # retornem l'Arbre buit



    def escriu(self): 
        
        # Cas base: si l'arbre binari és buit, imprimim ()
        if self.buit(): 
            print(f"()", end="")

        else: 
            print(f"(", end="")                         # imprimim (
            print(self.valor_arrel(), end="")           # imprimim l'arrel
            self.fill_esq().escriu()                    # imprimim el fill esquerre de l'arrel
            self.fill_dre().escriu()                    # imprimim el fill dret de l'arrel
            print(f")", end="")                         # imprimim )




    def codifica(self, missatge, b): 

        # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', 
        # dividint-lo en blocs de mida 'b'


        # no destructiva
        # recursiu
        # chr(32 + (ord(c)+d-32)%95)


        # Hem de transformar el missatge en un arbre binari (hem d'utilitzar la idea del Heap, és a dir, 
        # els fills d'un arrel és 2k (fill_esq) i 2k+1 (fill_dre)). Posarem un None a la primera posició. 

        # ** Cas base **

        blocks = [missatge[i:i+b] for i in range(0, len(missatge), b)]       # Dividim el missatge en un bloc de n^2 caràcters
        missatge_codificat = ''

        # Obtenim cada missatge de blocks
        for block in blocks: 


            # Pas 1: El missatge es transforma en un arbre binari de caràcters el més complet possible
            arbre_missatge = self._trans_missatge_arbre(block)          # transformem el missatge en un arbre binari


            # Pas 2: Copiar l'arbre binari i posar el patró a l'arbre binari
            mosaic = self._crear_mosaic(len(block))




        # Retornem el missatge codificat
        return missatge_codificat



    
    def _trans_missatge_arbre(self, missatge): 

        nodes = [None] + list(missatge)              # llista on la primera posició és None, per tal de poder aplicar la idea del Heap
                                                     # 2k ==> fill esquerre i 2k+1 ==> fill dret

        arbre = ArbreBinari()                        # creem un arbre binari buit

        if len(nodes) > 1: 

            arbre.modificar_valor_arrel(nodes[1])    # l'element a l'índex 1 de la llista 'nodes' serà l'arrel de l'arbre

            for k in range(1, len(nodes)):             

                fill_esq = 2*k
                fill_dre = 2*k + 1

                if fill_esq < len(nodes): 
                    subarbre_esq = ArbreBinari(nodes[fill_esq])
                    arbre.modificar_fill_esq(subarbre_esq)


                if fill_dre < len(nodes): 
                    subarbre_dre = ArbreBinari(nodes[fill_dre])
                    arbre.modificar_fill_dre(subarbre_dre)

            return arbre


    def _crear_mosaic(self, mida): 
        pass









    def decodifica(self, missatge, b):

        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
        # en blocs de mida 'b' 
        # chr(32 + (ord(c)-d+63)%95)

        pass