from dbConnect import sessionLoader
from mapper import Ersatzteil
from checker import handleInputInteger

def getErsatzteil():

    conn = getConn()
    cursor = conn.cursor()

    try:
        cursor.execute('Select EtID, - , EtBezeichnung, - , EtPreis, - , EtAnzahl, - ,EtHersteller from Ersatzteil')
    except: 
        print('Abfrage ist fehlerhaft')
        cursor.close()
        return 

    # Leere Ergebnismenge abfangen
    if cursor.rowcount == 0:
        print('Keine Ersatzteile vorhanden.')
        cursor.close()
        return 0


    print('\nErsatzteile:')
    liste_Et = [0]
    for row in cursor: 
        print(row.EtID, row.EtBezeichnung, row.EtPreis, row.EtAnzahl, row.EtHersteller)
        liste_Et.append(int(row[0]))   

    cursor.close()
    conn.close()

