from loguru import logger
import time


def create_artist(cursor):
    logger.info("Creating artist")
    time.sleep(0.5)

    full_name = input("Enter full name: ")
    passport_number = input("Enter passport number: ")
    country_of_origin = input("Enter country of origin: ")
    alias = input("Enter alias: ")
    cursor.execute("INSERT INTO Artist (FullName, PassportNumber, CountryOfOrigin, Alias) VALUES (%s, %s, %s, %s)",
                   (full_name, passport_number, country_of_origin, alias))


def read_artist(cursor):
    logger.info("Reading all artists")
    time.sleep(0.5)
    cursor.execute("SELECT * FROM Artist")
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_artist(cursor):
    logger.info("Updating artist")
    time.sleep(0.5)
    artist_id = input("Enter ArtistID to update: ")
    new_full_name = input("Enter new full name: ")
    new_passport_number = input("Enter new passport number: ")
    new_country_of_origin = input("Enter new country of origin: ")
    new_alias = input("Enter new alias: ")
    cursor.execute(
        "UPDATE Artist SET FullName = %s, PassportNumber = %s, CountryOfOrigin = %s, Alias = %s WHERE ArtistID = %s",
        (new_full_name, new_passport_number, new_country_of_origin, new_alias, artist_id))


def delete_artist(cursor):
    logger.info("Delete artist")
    time.sleep(0.5)
    artist_id_to_delete = input("Enter ArtistID to delete: ")
    cursor.execute("DELETE FROM Artist WHERE ArtistID = %s", (artist_id_to_delete,))
