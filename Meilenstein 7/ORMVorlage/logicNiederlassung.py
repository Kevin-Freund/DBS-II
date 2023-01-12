from dbConnect import sessionLoader
from mapper import Niederlassung
from checker import handleInputInteger

def getNiederlassung():
    """ Definition der Funktion getNiederlassung
    Die Funktion ruft alle Niederlassungen aus der Tabelle Niederlassung ab und gibt sie tabellarisch aus.
    Der Benutzer wird aufgefordert, eine der Niederlassungsnummern einzugeben.

    :return eingabe_nlnr - Niederlassungsnummer, die vom Benutzer eingegeben wurde
    :rtype  int
    """
    session = sessionLoader()
    menge_nl = session.query(Niederlassung).all()       # Ermittlung aller Niederlassungen aus der DB
    
    print('Niederlassungen: ')
    # Wenn mehr als 0 Niederlassungen ermittelt werden konnten
    if len(menge_nl)>0:
        # Defintion und Initialisierung der Liste der Niederlassungsnummern, 1. Element 0
        liste_nlnr = [0]
        for nl in menge_nl:
            print(f' {nl.NlNr}  -  {nl.Ort}')     # Ausgabe der Daten
            liste_nlnr.append(nl.NlNr)            # Anhängen der Niederlassugnsnummer an die Liste
        print()        
    
        # Absicherung, dass die eingegebene Niederlassungsnummer auch in der Liste der Niederlassungsnummern enthalten ist
        # die Eingabeaufforderung wird so oft wiederholt, bis ein Element aus der Liste der Niederlassungsnummern
        # eingegeben wird. Das erste Element der Liste ist 0. HandleInputInteger() liefert im Falle der fehlenden Eingabe
        # 0 zurück. Damit kann die Eingabe durch "Enter" als Eingabe beendet werden.
        eingabe_nlnr = -1
        while eingabe_nlnr not in liste_nlnr:
            eingabe_nlnr = handleInputInteger('Ort eingeben (Nr)')
        # Ende der Absicherung
    else:
        print('Keine Niederlassungen in der DB.')
        eingabe_nlnr = 0
    session.close()
    return eingabe_nlnr

