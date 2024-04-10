from loguru import logger
import time


def create_participation(cursor):
    logger.info("Creating participation")
    time.sleep(0.5)
    artist_id = input("Enter ArtistID: ")
    concert_id = input("Enter ConcertID: ")
    participation_status = input("Enter ParticipationStatus: ")
    cursor.execute("INSERT INTO Participation (ArtistID, ConcertID, ParticipationStatus) VALUES (%s, %s, %s)",
                   (artist_id, concert_id, participation_status))


def read_participation(cursor):
    logger.info("Reading all participation")
    time.sleep(0.5)
    cursor.execute("SELECT * FROM Participation")
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_participation(cursor):
    logger.info("Updating participation")
    time.sleep(0.5)
    artist_id = input("Enter ArtistID to update: ")
    concert_id = input("Enter ConcertID to update: ")
    new_participation_status = input("Enter new ParticipationStatus: ")
    cursor.execute("UPDATE Participation SET ParticipationStatus = %s WHERE ArtistID = %s AND ConcertID = %s",
                   (new_participation_status, artist_id, concert_id))


def delete_participation(cursor):
    logger.info("Delete participation")
    time.sleep(0.5)
    artist_id_to_delete = input("Enter ArtistID to delete: ")
    cursor.execute("DELETE FROM Participation WHERE ArtistID = %s",
                   (artist_id_to_delete, ))

