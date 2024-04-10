from loguru import logger
import time


def create_organizer(cursor):
    logger.info("Creating organizer")
    time.sleep(0.5)
    ilicense = int(input("Input licence: "))
    name = input("Input name of organizer: ")
    contact_info = input("Input contact information(email): ")
    cursor.execute("INSERT INTO Organizer (License, Name, ContactInfo) "
                   "VALUES (%s, %s, %s)",
                   (ilicense, name, contact_info))


def read_organizer(cursor):
    cursor.execute("SELECT * FROM Organizer")
    time.sleep(0.5)
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_organizer(cursor):
    logger.info("Updating program")
    time.sleep(0.5)
    new_license = input("Enter new license: ")
    new_name = input("Enter new name: ")
    new_contact_info = input("Enter new contact info: ")
    organizer_id = input("Enter organizer ID to update: ")

    cursor.execute("UPDATE Organizer SET License = %s, Name = %s, ContactInfo = %s WHERE OrganizerID = %s",
                   (new_license, new_name, new_contact_info, organizer_id))


def delete_organizer(cursor):
    logger.info("Delete organizer")
    time.sleep(0.5)
    organizer_id_to_delete = input("Enter organizer ID to delete: ")
    cursor.execute("DELETE FROM Organizer WHERE OrganizerID = %s", (organizer_id_to_delete,))
