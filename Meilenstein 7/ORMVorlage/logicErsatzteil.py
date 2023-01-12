from dbConnect import sessionLoader
from mapper import Ersatzteil
from checker import handleInputInteger
from sqlalchemy import exc, or_


def getErsatzteil():

    session = sessionLoader()
    # Abruf der Mitarbeiterdaten zur übergebenen Mitarbeiternummer
    ersatzteil = session.query(Ersatzteil).all()
    eingabe_EtID = 0

    if len(ersatzteil)>0:
        # Defintion und Initialisierung der Liste der Niederlassungsnummern, 1. Element 0
        liste_et = [0]
        for et in ersatzteil:
            print(f' {et.EtID}  -  {et.EtBezeichnung} - {et.EtPreis} - {et.EtAnzahl} - {et.EtHersteller}')     # Ausgabe der Daten
            liste_et.append(et.EtID)            # Anhängen der Niederlassugnsnummer an die Liste
        print()  
    else:
        print('Keine Ersatzteile in der DB.')
        eingabe_EtID = 0
    session.close()
    return eingabe_EtID


def getAufErsatzteil():

    session = sessionLoader()
    # Abruf der Mitarbeiterdaten zur übergebenen Mitarbeiternummer
    ersatzteil = session.query(Ersatzteil).all()

    if len(ersatzteil)>0:
        # Defintion und Initialisierung der Liste der Niederlassungsnummern, 1. Element 0
        liste_et = [0]
        for et in ersatzteil:
            print(f' {et.EtID}  -  {et.EtBezeichnung} - {et.EtAnzahl}')     # Ausgabe der Daten
            liste_et.append(et.EtID)            # Anhängen der Niederlassugnsnummer an die Liste
        print() 
        eingabe_EtID = -1


    else:
        print('Keine Ersatzteile in der DB.')
        eingabe_EtID = 0
    session.close()
    return eingabe_EtID
