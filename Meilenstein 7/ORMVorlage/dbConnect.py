
from queue import Empty
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

def sessionLoader():
    """ Definition der Funktion sessionLoader
    Die Funktion erstellt eine neue DB-Session und gibt diese zurück.

    :return session Die DB-Session
    """
    # Datenbankverbindung
    singletonEngine = SingletonEngine()
      
    # Session zur Datenbank erzeugen, falls noch nicht vorhanden
    Session = sessionmaker(bind=singletonEngine.engine)
    session = Session()
    return session

class SingletonEngine(object):
    """Erstellen der Engine für den Datenbankzugriff als Singleton-Klasse"""    
    engine = Empty
    
    # Defintion der Datenbank-Verbindung
    # user   = Datenbankuser     - bitte eintragen
    # pw     = Datenbankpasswort - bitte eintragen
    # dbname = Datenbankname     - bitte eintragen
    connection_url = URL.create(
        "mssql+pyodbc",
        username="user",
        password="pw",
        host="141.56.2.45",
        port=1433,
        database="dbname-Name",
        query={"driver": "ODBC Driver 17 for SQL Server"}
    )
    
    # Aufruf der Klassenmethode __new__ 
    # Erzeugen des Objektes wird mittels __new__ (cls = class)
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonEngine, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.engine = create_engine(self.connection_url, echo=False)





