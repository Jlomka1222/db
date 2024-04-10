from loguru import logger
import time


def create_concert(cursor):
    logger.info("Creating concert")
    time.sleep(0.5)
    technical_contractor = input("Enter technical contractor: ")
    construction_date = input("Enter construction date (YYYY-MM-DD): ")
    concert_date = input("Enter concert date (YYYY-MM-DD): ")
    venue = input("Enter venue: ")
    organizer_id = input("Enter organizer ID: ")
    program_id = input("Enter program ID: ")
    cursor.execute(
        "INSERT INTO Concert (TechnicalContractor, ConstructionDate, ConcertDate, Venue, OrganizerID, ProgramID) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (technical_contractor, construction_date, concert_date, venue, organizer_id, program_id))


def read_concert(cursor):
    logger.info("Reading all concerts")
    time.sleep(0.5)
    cursor.execute("SELECT * FROM Concert ORDER BY concertid ")

    records = cursor.fetchall()
    for record in records:
        print(record)


def update_concert(cursor):
    logger.info("Updating concert")
    time.sleep(0.5)
    concert_id = input("Enter ConcertID to update: ")
    new_technical_contractor = input("Enter new technical contractor: ")
    new_construction_date = input("Enter new construction date (YYYY-MM-DD): ")
    new_concert_date = input("Enter new concert date (YYYY-MM-DD): ")
    new_venue = input("Enter new venue: ")
    new_organizer_id = input("Enter new organizer ID: ")
    new_program_id = input("Enter new program ID: ")

    cursor.execute(
        "UPDATE Concert SET TechnicalContractor = %s, ConstructionDate = %s, "
        "ConcertDate = %s, Venue = %s, OrganizerID = %s, ProgramID = %s "
        "WHERE ConcertID = %s",
        (new_technical_contractor, new_construction_date, new_concert_date, new_venue, new_organizer_id, new_program_id,
         concert_id))


def delete_concert(cursor):
    logger.info("Delete concert")
    time.sleep(0.5)
    concert_id_to_delete = input("Enter ConcertID to delete: ")
    cursor.execute("DELETE FROM Concert WHERE ConcertID = %s", (concert_id_to_delete,))

