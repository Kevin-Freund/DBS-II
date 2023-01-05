from logicDatenzugriff import getNiederlassung, getMitarbeiter, getAuftrag

nlnr = getNiederlassung()            # Niederlassung aus Niederlassungsliste auswählen
while nlnr > 0:
    print()
    mitnr = getMitarbeiter(nlnr)     # Mitarbeiter aus Mitarbeiterliste auswählen
    while mitnr > 0:
        print()
        getAuftrag(mitnr)            # Aufträge des Mitarbeiters anzeigen
        mitnr = getMitarbeiter(nlnr) # neuen Mitarbeiter aus Mitarbeiterliste auswählen
    nlnr = getNiederlassung()        # neue Niederlassung aus Niederlassungsliste auswählen
