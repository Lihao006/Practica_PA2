from pytokr  import item, items

from contenidor  import Missatges, Reixetes, Patrons
from reixeta     import Reixeta
from patro       import Patro


# Lectura missatges inicials
missatges = Missatges()                     # Creem una instància de la classe Missatges (subclasse de Contenidor)

mi = int(item())                            # Nombre de missatges inicials
for _ in range(mi):
    ident    = item()                       # Llegeix l'identificador del missatge
    missatge = input()                      # Llegeix el missatge complet
    missatges.afegeix(ident,missatge)       # Afegim un nou missatge al contenidor 'missatges' amb l'identificador 'ident'

    
# Lectura reixetes inicials: Se'ns garanteix que aquestes són correctes i vàlides
# (no cal comprovar-ho)
reixetes = Reixetes()                       # Creem una instància de la classe Reixetes (subclasse de Contenidor)

ri = int(item())                            # Nombre de reixetes inicials
for ident in range(1,ri+1):                 # Assignar a cada reixeta un identificador 
    r = Reixeta()                           # Crear una nova instància de la classe Reixeta() per a cada iteració
    r.llegeix()                             # Llegeix la entrada de dimensions (n,k) i les posicions dels forats de la reixeta
    reixetes.afegeix(ident,r)               # Afegim la reixeta 'r' al contenidor 'reixetes' amb l'identificador 'ident' 

    
# Lectura patrons inicials
patrons = Patrons()                         # Creem una instància de la classe Patrons (subclasse de Contenidor)

pi = int(item())                            # Nombre de patrons inicials
for ident in range(1,pi+1):                 # Assignar a cada patró un identificador
    p = Patro()                             # Crear una nova instància de la classe Patro() per a cada iteració 
    p.llegeix()                             # Llegeix la entrada dels valors de l'arbre binari en preordre (nombres enters i -1 per a nodes buits)
    patrons.afegeix(ident,p)                # Afegim el patró 'p' al contenidor 'patrons' amb l'identificador 'ident' 



    
# Ja hem inicialitzat les missatges, reixetes i patrons inicials...

instruccio = item()                 # llegim la comanda a processar
while instruccio != 'fi':           # continuem processant instruccions fins que 'instruccio' sigui 'fi'
    
    if   instruccio == 'nou_missatge' or instruccio == 'nm':                        
        ident    = item()                                                           # llegeixo una línia de text: Identificador
        print("#",instruccio," ",ident,sep='')                                      # imprimim la instrucció i l'identificador
        missatge = input()                                                          # llegeixo una línia de text: Missatge
        
        
        if missatges.existeix(ident):                                               # verifiquem si existeix un missatge amb l'identificador 'ident' al contenidor 'missatges'
            print("error: ja existeix un missatge amb aquest identificador")        # si ja existeix

        else:
            missatges.afegeix(ident,missatge)                                       # si no existeix, agreguem el missatge i el seu identificador
            num = missatges.mida()                                                  # obtenim el nombre total de missatges al contenidor 'missatges'
            print(num)                                                              # imprimim el nombre total de missatges 



    elif instruccio == 'nova_reixeta' or instruccio == 'nr':                        
        print("#",instruccio,sep='')                                               
        r = Reixeta()                                                               
        status = r.llegeix()                        # llegim les dimensions (n,k) i les posicions dels forats de la reixeta i retorna un estat
       
       
        if status == 1:                             # si la reixeta és vàlida
            num = reixetes.mida()                   # obtenim el nombre actual de reixetes al contenidor 'reixetes'
            reixetes.afegeix(num+1,r)               # afegim la reixeta 'r' amb l'identificador 'num+1'
            print(num+1)                            # imprimim el nou identificador 

        else:                                                                                       # si la reixeta no és vàlida
            if status == -1:                                                                        
                print("error: la reixeta amb els seus girs no cobreix totes les posicions")             
            elif status == -2:
                print("error: dimensions incorrectes de la reixeta")



    elif instruccio == 'nou_patro' or instruccio == 'np':
        print("#",instruccio,sep='')                                    
        p = Patro()                                                     
        p.llegeix()
        num = patrons.mida()                        # obtenim el nombre actual de patrons al contenidor 'patrons'
        patrons.afegeix(num+1,p)        
        print(num+1)
        


    elif instruccio == 'esborra_missatge' or instruccio == 'em':
        ident    = item()                                               # llegeixo una línia de text: Identificador
        print("#",instruccio," ",ident,sep='')


        if not missatges.existeix(ident):
            print("error: el missatge no existeix")
        
        else:
            missatges.esborra_missatge(ident)                           # cridem el mètode 'esborra_missatge' de 'Missatges' per eliminar el missatge amb l'identificador 'ident'
            num = missatges.mida()
            print(num)



    elif instruccio == 'llista_missatges' or instruccio == 'lm':
        print("#",instruccio,sep='')
        
        for k,v in missatges.itera():                                   # iterem sobre els elements del contenidor 'missatges'
            print(k)                                                    # imprimim l'identificador (k) del missatge (una cadena)
            print('"',v,'"',sep='')                                     # imprimim el contingut del missatge (v) entre cometes
            


    elif instruccio == 'llista_reixetes' or instruccio == 'lr':         
        print("#",instruccio,sep='')

        for ident,r in reixetes.itera():                                    # iterem sobre els elements del contenidor 'reixetes' 
            print('Reixeta ',ident,':',sep='')                              # imprimim l'identificador (ident)
            r.escriu()                                                      # mostrem les dimensions (n,k) i les posicions dels forats per a la reixeta i els seus girs
        


    elif instruccio == 'llista_patrons' or instruccio == 'lp':
        print("#",instruccio,sep='')

        for ident,p in patrons.itera():
            print('Patró ',ident,':',sep='')
            p.escriu()                                                      # cridem el mètode 'escriu' de 'Patro' que imprimeix l'arbre binari en preordre (valors dels nodes i -1 per a nodes buits)               
        


    elif instruccio == 'codifica_amb_reixeta' or instruccio == 'cr':
        idreix   = int(item())                                              # identificador de la reixeta
        print("#",instruccio," ",idreix,sep='')     
        missatge = input()                                                  # llegeixo una línia de text: Missatge (a codificar)
        
        
        if not reixetes.existeix(idreix):                                   # no existeix la reixeta amb l'identificador 'idreix' al contenidor 'reixetes'
            print("error: la reixeta no existeix")
        
        else:                                                               # si existeix
            r = reixetes.valor(idreix)                                      # obtenim l'objecte Reixeta
            m = r.codifica(missatge)                                        # codifiquem el 'missatge'
            print('"',m,'"',sep='')                                         # imprimim el missatge codificat entre cometes
            


    elif instruccio == 'codifica_amb_reixeta_guardat' or instruccio == 'crg':
        ident    = item()                                           # llegim l'identificador del missatge emmagatzemat que es vol codificar
        idreix   = int(item())                                      # llegim l'identificador de la reixeta a utilitzar
        print("#",instruccio," ",ident," ",idreix,sep='')           # imprimim la instrucció, l'identificador del missatge i l'identificador de la reixeta
      
      
        if not missatges.existeix(ident):                           # si no existeix l'identificador 'ident' al contenidor missatges
            print("error: el missatge no existeix")
   
        else:                                                       # si el missatge existeix
            if not reixetes.existeix(idreix):                       # si no existeix la reixeta amb l'identificador 'idreix' al contenidor 'reixetes'
                print("error: la reixeta no existeix")
         
            else:                                                   # si la reixeta existeix
                m  = missatges.valor(ident)                         # obtenim el missatge associat a ident
                r  = reixetes.valor(idreix)                         # obtenim l'objecte 'Reixeta' associat a 'idreix'
                mx = r.codifica(m)                                  # codifiquem el missatge 'm' utilitzant el mètode 'codifica' de la reixeta r
                print('"',mx,'"',sep='')                            # imprimim el missatge codificat entre cometes
            


    elif instruccio == 'decodifica_amb_reixeta' or instruccio == 'dr':
        idreix   = int(item())                                      # llegim l'identificador de la reixeta a utilitzar
        print("#",instruccio," ",idreix,sep='')                     # imprimim la instrucció i l'identificador de la reixeta
        missatge = input()                                          # llegeixo una línia de text: Missatge xifrat
        
        
        if not reixetes.existeix(idreix):                           # si no existeix la reixeta amb l'identificador 'idreix' al contenidor 'reixetes'
            print("error: la reixeta no existeix")
        
        else:                                                       # si la reixeta existeix
            r = reixetes.valor(idreix)                              # obtenim l'objecte 'Reixeta' associat a 'idreix'
            if not r.valid(missatge):                               # comprovem si és vàlid la mida del missatge és adequeada per a la reixeta
                print("error: la mida del missatge és inadeqüada per a la reixeta")

            else:                                                   # si és vàlid
                m = r.decodifica(missatge)                          # decodifiquem el missatge xifrat utilitzant el mètode 'decodifica' de la reixeta 'r'
                print('"',m,'"',sep='')                             # imprimim el missatge decodificat entre cometes
            


    elif instruccio == 'codifica_amb_patro' or instruccio == 'cp':
        idpat   = int(item())                                       # llegim l'identificador del patró (arbre binari) a utilitzar
        b       = int(item())                                       # llegim un enter (b) que indica la mida dels blocs en què es dividirà el missatge per a la codificació
        print("#",instruccio," ",idpat," ",b,sep='')                # imprimim la instrucció, l'identificador del patró i la mida del bloc
        missatge = input()                                          # llegeixo una línia de text: Missatge (a codificar)
      
      
        if not patrons.existeix(idpat):                             # si no existeix el patró amb l'identificar 'idpat' al contenidor 'patrons'
            print("error: el patró no existeix")
        
        else:                                                       # si el patró existeix
            p = patrons.valor(idpat)                                # obtenim l'objecte 'Patro' associat a 'idpat'
            m = p.codifica(missatge,b)                              # codifiquem el missatge fent servir el mètode 'codifica' del patró 'p', dividint-lo en blocs de mida 'b'
            print('"',m,'"',sep='')                                 # imprimim el missatge codificat entre cometes
            


    elif instruccio == 'codifica_amb_patro_guardat' or instruccio == 'cpg':
        ident   = item()   
        idpat   = int(item())
        b       = int(item())
        print("#",instruccio," ",ident," ",idpat," ",b,sep='')
        
        
        if not missatges.existeix(ident):
            print("error: el missatge no existeix")
        
        else:
            if not patrons.existeix(idpat):
                print("error: el patró no existeix")
            
            else:
                m  = missatges.valor(ident)
                p  = patrons.valor(idpat)
                mx = p.codifica(m,b)
                print('"',mx,'"',sep='')
                


    elif instruccio == 'decodifica_amb_patro' or instruccio == 'dp':       
        idpat   = int(item())
        b       = int(item())
        print("#",instruccio," ",idpat," ",b,sep='')
        missatge = input()                                      # llegeixo una línia de text: Missatge xifrat
       
       
        if not patrons.existeix(idpat):
            print("error: el patró no existeix")
        
        else:
            p = patrons.valor(idpat)
            m = p.decodifica(missatge,b)                        # decodifiquem el 'missatge' utilitzant el mètode 'decodifica' del patró 'p', dividint-lo 
                                                                # en blocs de mida 'b' 
            print('"',m,'"',sep='')



    instruccio = item()