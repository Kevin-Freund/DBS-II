from dbConn import getConn
from checker import handleInputInteger

def getNiederlassung():
    """ Definition der Funktion getNiederlassung
    Die Funktion ruft alle Niederlassungen aus der Tabelle Niederlassung ab und gibt sie tabellarisch aus.
    Der Benutzer wird aufgefordert, eine der Niederlassungsnummern einzugeben.
    
    :return eingabe_nlnr - Niederlassungsnummer, die vom Benutzer eingegeben wurde
    :rtype  int
    """
    
    conn = getConn()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT nlnr, ort from niederlassung')
    except:
        print('Abfrage ist fehlerhaft')
        cursor.close()
        return
    
    print('\nNiederlassungen:')
    liste_nlnr = [0]            # Anlegen einer Liste um die Niederlassungsnummern abzulegen
    for row in cursor:
        print(row.nlnr, ' - ', row.ort)
        liste_nlnr.append(row.nlnr)     # Hinzufügen der Niederlassungsnummer zur Liste
    cursor.close()
    conn.close()

    # Absicherung, dass die eingegebene Niederlassungsnummer auch in der Liste der Niederlassungsnummern enthalten ist
    # die Eingabeaufforderung wird so oft wiederholt, bis ein Element aus der Liste der Niederlassungsnummern
    # eingegeben wird. Das erste Element der Liste ist 0. HandleInputInteger() liefert im Falle der fehlenden Eingabe
    # 0 zurück. Damit kann die Eingabe durch "Enter" als Eingabe beendet werden.
    eingabe_nlnr = -1
    while eingabe_nlnr not in liste_nlnr:
        eingabe_nlnr = handleInputInteger('Ort eingeben (Nr)')
    # Ende der Absicherung

    return eingabe_nlnr


def getMitarbeiter(p_nlnr):
    """ Definition der Funktion getMitarbeiter
    Die Funktion ruft alle Mitarbeiter mit der übergebenen Niederlassungsnummer ab und gibt
    sie tabellarisch aus.
    Der Benutzer wird aufgefordert eine Mitarbeiternummer einzugeben.

    .param  p_nlnr - Niederlassungsnummer
    :return eingabe_mitnr - Mitarbeiternummer, die vom Benutzer eingegebn wurde
    :rtype  int
    """

    conn = getConn()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT MitID, MitName from Mitarbeiter where nlnr = ?', (p_nlnr))
    except:
        print('Abfrage ist fehlerhaft')
        cursor.close()
        return

    # Leere Ergebnismenge abfangen
    if cursor.rowcount == 0:
        print('Kein Mitarbeiter in der Niederlassung beschäftigt')
        cursor.close()
        return 0

    print('\nMitarbeiter:')
    liste_mit = [0]
    for row in cursor:
        print(row.MitID, ' - ', row.MitName)
        liste_mit.append(int(row[0]))
                         
    cursor.close()
    conn.close()

    # Absicherung, dass die eingegebene Mitarbeiternummer einem Mitarbeiter aus der Niederlassung entspricht
    # die Eingabeaufforderung wird so oft wiederholt, bis ein Element aus der Liste der Mitarbeiternummern
    # eingegeben wird. Das erste Element der Liste ist 0. HandleInputInteger() liefert im Falle der fehlenden Eingabe
    # 0 zurück. Damit kann die Eingabe durch "Enter" als Eingabe beendet werden.
    eingabe_mitnr = -1
    while eingabe_mitnr not in liste_mit:
        eingabe_mitnr = handleInputInteger('Mitarbeiternummer eingeben')
    # Ende der Absicherung
    return eingabe_mitnr


def getAuftrag(p_mitnr):
    """ Definition der Funktion getMitarbeiter
    Die Funktion ruft alle Aufträge des Mitarbeiter für die übergebene Mitarbeiternummer 
    der kommenden Kalenderwoche ab und gibt sie tabellarisch aus."""

    conn = getConn()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT MitID, MitName, MitVorname, MitJob, MitStundensatz from Mitarbeiter where MitID = ?', (p_mitnr))
    except:
        print('Abfrage ist fehlerhaft')
        cursor.close()
        return

    print('\nMitarbeiterdetaildaten:')
    liste_mit = [0]
    for row in cursor:
        print(row.MitID, ' - ', row.MitName, ' - ', row.MitVorname, ' - ', row.MitJob, ' - ', row.MitStundensatz)
        liste_mit.append(int(row[0]))

    try:
        cursor.execute('Select AufNr, MitID, KunNr, AufDat, ErlDat, Dauer, Anfahrt, Beschreibung from Auftrag where Datepart(wk, ErlDat) = Datepart(wk, GetDate()) + 1 and Year(ErlDat) = 2023 and MitID = ? order by ErlDat', (p_mitnr))  
    except: 
        print('Abfrage ist fehlerhaft')
        cursor.close()
        return 

    # Leere Ergebnismenge abfangen
    if cursor.rowcount == 0:
        print('Kein Mitarbeiter in der Niederlassung beschäftigt')
        cursor.close()
        return 0


    print('\nAufträge der nächsten Woche:')
    liste_auf = [0]
    for row in cursor: 
        print(row.AufNr, row.MitID, row.KunNr, row.AufDat, row.ErlDat, row.Dauer, row.Anfahrt, row.Beschreibung)
        liste_auf.append(int(row[0]))   

    cursor.close()
    conn.close()
    """
    :param  ??
    :return ??
    :rtype  ??
    """
