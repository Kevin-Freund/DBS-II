from dbConnect import sessionLoader
from mapper import Montage
from mapper import Auftrag
from checker import handleInputInteger

def getMontage(p_aufnr):
    """ Definition der Funktion getMitarbeiter
    Die Funktion ruft alle Mitarbeiter mit der übergebenen Niederlassungsnummer ab und gibt
    sie tabellarisch aus.
    Der Benutzer wird aufgefordert eine Mitarbeiternummer einzugeben.

    .param  p_nlnr - Niederlassungsnummer
    :return eingabe_mitnr - Mitarbeiternummer, die vom Benutzer eingegebn wurde
    :rtype  int
    """
    session = sessionLoader()
    # Abfrage des Auftrags für die übergebene Auftragsnummer
    auftrag = session.query(Auftrag).get(p_aufnr)

    # Abbruch, falls der Auftrag nicht vorhanden ist
    if isinstance(auftrag, type(None)):
        print(f'Auftrag mit der AufNr: {p_aufnr} existiert nicht in der Datenbank.')
        session.close()
        return 0
    
    if len(auftrag.ListeMontage) > 0:
        # Definition der Liste für die Mitarbeiternummern aus der Niederlassung,  1. Element 0
        liste_mon = [0]    
        for mon in auftrag.ListeMontage:
            print(f' {mon.EtID} - {mon.Anzahl}')  # Ausgabe der Daten
            # liste_mon.append(int(mon.EtID))                     # Anhängen der Mitarbeiternummer an die Liste
        print()
        
        # Absicherung, dass die eingegebene Mitarbeiternummer einem Mitarbeiter aus der Niederlassung entspricht
        # die Eingabeaufforderung wird so oft wiederholt, bis ein Element aus der Liste der Mitarbeiternummern
        # eingegeben wird. Das erste Element der Liste ist 0. HandleInputInteger() liefert im Falle der fehlenden Eingabe
        # 0 zurück. Damit kann die Eingabe durch "Enter" als Eingabe beendet werden.
        eingabe_aufnr = -1
        while eingabe_aufnr not in liste_mon:
            eingabe_aufnr = handleInputInteger('Auftragnummer eingeben')
        # Ende der Absicherung
    else:
        print('Es gibt keine Mitarbeiter in dieser Niederlassung')
        eingabe_aufnr = 0
    session.close()


    return int(eingabe_aufnr)

