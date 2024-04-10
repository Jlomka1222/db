from connection import *
from menu import *
from cruds.user import *
from cruds.ticket import *
from cruds.program import *
from cruds.artist import *
from cruds.concert import *
from cruds.organaizer import *
from cruds.attendance import *
from cruds.participation import *
import time


table_operations = {
    (1, 1): create_users,
    (1, 2): read_users,
    (1, 3): update_users,
    (1, 4): delete_users,
    (2, 1): create_tickets,
    (2, 2): read_tickets,
    (2, 3): update_tickets,
    (2, 4): delete_tickets,
    (3, 1): create_program,
    (3, 2): read_program,
    (3, 3): update_program,
    (3, 4): delete_program,
    (4, 1): create_artist,
    (4, 2): read_artist,
    (4, 3): update_artist,
    (4, 4): delete_artist,
    (5, 1): create_concert,
    (5, 2): read_concert,
    (5, 3): update_concert,
    (5, 4): delete_concert,
    (6, 1): create_organizer,
    (6, 2): read_organizer,
    (6, 3): update_organizer,
    (6, 4): delete_organizer,
    (7, 1): create_attendance,
    (7, 2): read_attendance,
    (7, 3): update_attendance,
    (7, 4): delete_attendance,
    (8, 1): create_participation,
    (8, 2): read_participation,
    (8, 3): update_participation,
    (8, 4): delete_participation,
}


db_connection = DatabaseConnection()
conn = db_connection.create_connection()
cursor = conn.cursor()
time.sleep(0.5)
while True:
    print("\nWelcome!")
    contwork = input("Do u want to work?\n").lower()
    if contwork == "y" or contwork == "yes":

        table = menu()
        oper = operation()

        chosen_operation = table_operations.get((table, oper))

        if chosen_operation:
            chosen_operation(cursor)
        else:
            print("Invalid choice of table or operation.")
    else:
        isSure = input("Are u sure?").lower()
        if isSure == "y" or isSure == "yes":
            break


cursor.close()
db_connection.close_connection()
