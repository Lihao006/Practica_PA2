from pytokr  import item, items
from arbre_binari_amb_nodes import ArbreBinari
# from arbre_binari import ArbreBinari

class Patro(ArbreBinari):
    # A completar pel grup d'estudiants com a part de la pràctica

    def llegeix(self):

        # Construeix l'arbre binari de l'objecte Patro a partir d'una seqüència en preordre
        # self: Instància de la classe Patro (per exemple, p a program.py)
        
        def llegeix_node():

            # Llegeix el següent valor de la seqüència en preordre amb item() 
            valor = int(item())

            # Cas base: si el valor és -1, retornem None per indicar un node buit
            if valor == -1: 
                return None
            
            # Cas recursiu: creem un node amb el valor com a _element i processem els fills esquerre i dret recursivament, seguint l'ordre preordre
            return self._Node(valor, llegeix_node(), llegeix_node())


        # després de cridar p = Patro(), self._root = None, però quan fem p.llegeix(), self._root es configura amb els nodes segons el preordre donat 
        self._root = llegeix_node()



    def escriu(self): 

        # cridem el mètode 'escriu' de 'Patro' que imprimeix l'arbre binari en preordre (valors dels nodes i -1 per a nodes buits) 
        
        # Cas base: si l'arbre binari és buit... 
        if self.buit():
            print(-1, end=' ')

        else:
            print(self.valor_arrel(), end=' ')
            self.fill_esq().escriu()
            self.fill_dre().escriu()



    def codifica(self, missatge, b): 

        # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', 
        # dividint-lo en blocs de mida 'b'

        pass 


    def decodifica(self, missatge, b):

        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
        # en blocs de mida 'b' 

        pass