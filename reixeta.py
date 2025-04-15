from pytokr import item

class Reixeta():
    # A completar pel grup d'estudiants com a part de la pràctica
    def __init__(self, n=0, k=0, ):
        assert (n > 0 and k > 0) or (n == 0 or k == 0), "Error: dimensions impossibles"
        self._num_fils = n
        self._num_cols = k


    def llegeix(self):

        # llegim la entrada de dimensions (n,k) i les posicions dels forats de la reixeta

        # Aquí ha de retornar un status que pot ser: 
        # 1: la reixeta és vàlida 
        # -1: els girs de la reixeta no cobreixen totes les posicions
        # -2: les dimensions són incorrectes (k diferent de n^2/4)

        pass

    
    def escriu(self):

        # mostrem les dimensions (n,k) i les posicions dels forats per a la reixeta i els seus girs

        pass


    def codifica(self, missatge): 

        # codifiquem el 'missatge'

        pass


    def decodifica(self, missatge): 

        # decodifiquem el missatge

        pass
    

    def valid(self, missatge): 

        '''
        missatge: llegeixo una línia de text: Missatge xifrat
        '''

        # He de verificar que la mida del missatge és adeqüada per a la reixeta

        pass
