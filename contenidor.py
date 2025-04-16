class Contenidor:
    # A completar pel grup d'estudiants com a part de la pràctica
    
    def __init__(self): 
        self._elements = dict()         # Creem un diccionari per guardar les diferents missatges/reixetes/patrons 


    def afegeix(self, ident, instancia): 

        '''
        Pre:    'self': instància de Contenidor
                'ident': identificador de cada missatge, reixeta o patró 
                'instancia': nombre de missatges, reixetes o patrons
        '''

        # missatges.afegeix(ident, missatge): afegim un nou missatge al contenidor 'missatges' amb l'identificador 'ident'
        # reixetes.afegeix(ident, r): afegim la reixeta 'r' al contenidor 'reixetes' amb l'identificador 'ident'
        # patrons.afegeix(ident, p): afegim el patró 'p' al contenidor 'patrons' amb l'identificador 'ident' 

        self._elements[ident] = instancia



    def existeix(self, ident): 
        
        '''
        Pre:    'ident': identificador del missatge, reixeta o patró
        Retornar: ha de retornar True si existeix i False si no existeix
        '''

        # missatges.existeix(ident): verifiquem si existeix un missatge amb l'identificador 'ident' al contenidor 'missatges'
        # reixetes.existeix(idreix): verifiquem si existeix la reixeta amb l'identificador 'idreix' al contenidor 'reixetes'
        # patrons.existeix(idpat): verifiquem si existeix el patró amb l'identificar 'idpat' al contenidor 'patrons'
        
        return ident in self._elements



    def mida(self): 

        # missatges.mida(): obtenim el nombre total de missatges al contenidor 'missatges'
        # reixetes.mida(): obtenim el nombre actual de reixetes al contenidor 'reixetes'
        # patrons.mida(): obtenim el nombre actual de reixetes al contenidor 'reixetes'

        return len(self._elements)



    def itera(self): 

        # missatges.itera(): iterem sobre els elements del contenidor 'missatges'
        # reixetes.itera(): iterem sobre els elements del contenidor 'reixetes' 
        # patrons.itera(): iterem sobre els elements del contenidor 'patrons' 

        return iter(self._elements.items())



    def valor(self, ident): 

        '''
        Pre:    'ident': identificador del missatge, reixeta o patró
        '''

        # obtenim l'objecte 'Missatge' associat a 'ident'
        # obtenim l'objecte 'Reixeta' associat a 'ident'
        # obtenim l'objecte 'Patro' associat a 'ident'

        return self._elements[ident]            # No cal que comprovem si 'ident' està dins del diccionari perquè es crida 
                                                # al mètode valor després d'haver cridat al mètode 'existeix()'


 
class Missatges(Contenidor):
    # A completar pel grup d'estudiants com a part de la pràctica

    def __init__(self): 
        super().__init__()
        

    def esborra_missatge(self, ident): 

        # missatges.esborra_missatge(ident): eliminem el missatge amb l'identificador 'ident'
        if ident in self._elements: 
            del self._elements[ident]



class Reixetes(Contenidor):
    # A completar pel grup d'estudiants com a part de la pràctica
    
    def __init__(self): 
        super().__init__()




class Patrons(Contenidor):
    # A completar pel grup d'estudiants com a part de la pràctica
     
    def __init__(self): 
        super().__init__()