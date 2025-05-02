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

        # Cas Base
        if x == -1: 
            return ArbreBinari()                    # retornem l'Arbre buit

        # Cas recursiu 
        else: 
            l = self.llegeix()                      # obtenim el fill esquerre
            r = self.llegeix()                      # obtenim el fill dret
            return ArbreBinari(x,l,r)               # construïm l'arbre amb l'arrel 'x', fill esquerre 'l' i fill dret 'r'



    def escriu(self): 
        
        # Cas base: si l'arbre binari és buit, imprimim ()
        if self.buit(): 
            print(f"()", end="")

        else: 
            print(f"(", end="")                         # imprimim (
            print(self.valor_arrel(), end="")           # imprimim l'arrel
            self.fill_esq().escriu()                    # imprimim el fill esquerre de l'arrel
            self.fill_dre().escriu()                    # imprimim el fill dret de l'arrel
            print(f")", end="")                     # imprimim )


    def codifica(self, missatge, b): 

        # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', 
        # dividint-lo en blocs de mida 'b'
        # el missatge es posa en un arbre binari, utilizant un heap. (un None en la posicio zero)
        # els fills de cada caracter es (dret) 2k i (esq) 2k+1
        # no destructiva
        # recursiu
        # chr(32 + (ord(c)+d-32)%95)
        llista_missatge = [None] + list(missatge)
        arbre_missatge = ArbreBinari()
        arbre_missatge.modi



        pass 


    def decodifica(self, missatge, b):

        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
        # en blocs de mida 'b' 
        # chr(32 + (ord(c)-d+63)%95)

        pass