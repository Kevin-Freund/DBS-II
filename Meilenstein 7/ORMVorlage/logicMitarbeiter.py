from dbConnect import sessionLoader
from mapper import Niederlassung
from checker import handleInputInteger

def getMitarbeiter(p_nlnr):
    """ Definition der Funktion getMitarbeiter
    Die Funktion ruft alle Mitarbeiter mit der übergebenen Niederlassungsnummer ab und gibt
    sie tabellarisch aus.
    Der Benutzer wird aufgefordert eine Mitarbeiternummer einzugeben.

    .param  p_nlnr - Niederlassungsnummer
    :return eingabe_mitnr - Mitarbeiternummer, die vom Benutzer eingegebn wurde
    :rtype  int
    """
    session = sessionLoader()
    # Abfrage der Niederlassung für die übergebene Niederlassungsnummer
    niederlassung = session.query(Niederlassung).get(p_nlnr)

    # Abbruch, falls die Niederlassung nicht vorhanden ist
    if isinstance(niederlassung, type(None)):
        print(f'Niederlassung mit der NlNr: {p_nlnr} existiert nicht in der Datenbank.')
        session.close()
        return 0
    
    if len(niederlassung.ListeMitarbeiter) > 0:
        # Definition der Liste für die Mitarbeiternummern aus der Niederlassung,  1. Element 0
        liste_mit = [0]    
        for mit in niederlassung.ListeMitarbeiter:
            print(f' {mit.MitId} - {mit.Name} - {mit.Vorname}')  # Ausgabe der Daten
            liste_mit.append(int(mit.MitId))                     # Anhängen der Mitarbeiternummer an die Liste
        print()
        
        # Absicherung, dass die eingegebene Mitarbeiternummer einem Mitarbeiter aus der Niederlassung entspricht
        # die Eingabeaufforderung wird so oft wiederholt, bis ein Element aus der Liste der Mitarbeiternummern
        # eingegeben wird. Das erste Element der Liste ist 0. HandleInputInteger() liefert im Falle der fehlenden Eingabe
        # 0 zurück. Damit kann die Eingabe durch "Enter" als Eingabe beendet werden.
        eingabe_mitnr = -1
        while eingabe_mitnr not in liste_mit:
            eingabe_mitnr = handleInputInteger('Mitarbeiternummer eingeben')
        # Ende der Absicherung
    else:
        print('Es gibt keine Mitarbeiter in dieser Niederlassung')
        eingabe_mitnr = 0
    session.close()
    return int(eingabe_mitnr)

