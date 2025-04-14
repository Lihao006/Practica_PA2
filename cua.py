class Cua: 

    # Node
    class _Node: 
        __slots__ = '_element', '_next'

        def __init__(self, element, next): 
            self._element = element
            self._next = next

    
    # Constructor
    def __init__(self): 
        self._cap = None
        self._cua = None
        self._mida = 0


    def buida(self): 
        return self._mida == 0
    
    def mida(self):
        return self._mida 
    
    def primer(self): 
        return (self._cap)._element
    

    def encuar(self, e): 
        nou = self._Node(e, None)
        if self.buida(): 
            self._cap = nou

        else: 
            self._cua._next = nou

        self._cua = nou
        self._mida += 1


    def desencuar(self): 
        resposta = self._cap._element
        self._cap = self._cap._next
        self._mida -= 1

        if self.buida(): 
            self._cua = None

        return resposta