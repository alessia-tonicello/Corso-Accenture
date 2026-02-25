numero = int("ciao")

"""
ValueError è una classe di eccezioni e ci dice il tipo di errore

Eccezioni fatali: interrompono esecuzione software

Stackoverflow: stack fiinsce spazio a disposizione --> eccezione dal compilatore stackoverflow
Come si gestisce questo?

Altri errori:
- Nullpointer execption: quanso si prova a far qualcosa su una variabile tipo null
- Illegal argument exception: esempio A=3 e B=due --> sommiamo due cose non compatibili 

Gli errori vengono lanciati e a seconda del linguaggio abbiamo info su info lanciata (=classe sollevata)
e poi il messaggio. 
Poi abbiamo anche il Traceback, chiamato Stacktrace, che vede file per file quali sono le righe dei files
che scatenano il corto circuito nella nostra eccezione. 

Fallire con successo:
dire al programma di fare una cosa, ma se dovesse per caso avere un'eccezione non ti fermare, anzi,
prendi l'eccezione e catturala (Blocco tryexcept) 
--> io ho un blocco di codice che potrebbe essere instabile, e posso dire che questa cosa potrebbe 
indurre ad errori, quindi il blocco rischioso me lo metti in un blocco più grande 
che è il blocco try (= significa prova a eseguire il codice).

try:
    numero = int("ciao")
    print(numero)
except:
    print("error, il numero non è un numero")

except --> quando incontri errore stampa l'errore!
try: zona di rischio
except: intercetta qualsiasi errore

try:
    numero = int("ciao")
    print(numero)
except:
    print("error, il numero non è un numero")
    
--> prova ad eseguire il codice, se incontri ValueError stampalo, non mettere tutto l'errore grande rosso


ZerpDivisionError
appare perché non lo abbiamo gestito ancora, noi possiamo gestire più eccezioni.

try:
    numero = int("ciao")
    print(numero)
except ValueError:
    print("error, il numero non è un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero")



Finally: significa qualsiasi cosa succeda io vengo eseguito!

try:
    numero = int("ciao")
    print(numero)
except ValueError:
    print("error, il numero non è un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero")
finally:
    print("qualsiasi cosa succeda io vengo eseguito!")


Else
viene eseguito solo se non vengono trovate eccezioni

try:
    numero = int("ciao")
    print(numero)
except ValueError:
    print("error, il numero non è un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero")
else:
    print("divisione eseguita con successo!")
finally:
    print("qualsiasi cosa succeda io vengo eseguito!")
    
"""
