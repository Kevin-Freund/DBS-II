from checker import handleInputInteger
from logicNiederlassung import getNiederlassung
from logicMitarbeiter import getMitarbeiter
from logicErsatzteil import getErsatzteil
from logicMontage import getMontage
from logicAuftrag import getAuftrag, anlegenAuftrag, planenAuftrag, ErledigungBuchen

# Aufruf der Ablauflogik
while True:
    print('')
    print('1 - Daten anzeigen')
    print('2 - Neuen Auftrag anlegen')
    print('3 - Auftrag planen')
    print('4 - Ersatzteile')
    print('5 - Erledigung buchen')
    wastun = handleInputInteger('Aktion wählen')
    print()
    
    if wastun == 1:
        nlnr = getNiederlassung()            # Niederlassung aus Niederlassungsliste auswählen
        while nlnr > 0:
            print()
            mitnr = getMitarbeiter(nlnr)     # Mitarbeiter aus Mitarbeiterliste auswählen
            while mitnr > 0:
                print()
                aufnr = getAuftrag(mitnr)   # Aufträge des Mitarbeiters anzeigen
                while aufnr > 0:
                    print()
                    getMontage(aufnr)     
                    aufnr = getAuftrag(mitnr)           
                mitnr = getMitarbeiter(nlnr) # neuen Mitarbeiter aus Mitarbeiterliste auswählen
            nlnr = getNiederlassung()        # neue Niederlassung aus Niederlassungsliste auswählen

    elif wastun == 2:
        print('Daten einfügen')
        anlegenAuftrag()
        
    elif wastun == 3:
        print('Auftrag planen')
        planenAuftrag()

    elif wastun == 4:
        print('Ersatzteile')
        getErsatzteil()   

    elif wastun == 5:
        print('Planung buchen')
        ErledigungBuchen()    
    
    else:
        break

