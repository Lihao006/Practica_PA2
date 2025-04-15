from pytokr  import item, items
from arbre_binari_amb_nodes import ArbreBinari
# from arbre_binari import ArbreBinari

class Patro(ArbreBinari):
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self,v=None,esq=None,dre=None):
        super().__init__(v, esq, dre)

    def llegeix(preordre):

        # llegeix la entrada dels valors de l'arbre binari en preordre (nombres enters i -1 per a nodes buits)

        pass


    def escriu(self): 

        # cridem el mètode 'escriu' de 'Patro' que imprimeix l'arbre binari en preordre (valors dels nodes i -1 per a nodes buits) 
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