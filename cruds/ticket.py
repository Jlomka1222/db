import time
from loguru import logger


def create_tickets(cursor):
    logger.info("Creating ticket")
    time.sleep(0.5)
    price = float(input("Input price of ticket:"))
    ticket_type = input("Input ticket type(VIP/Regular): ")
    seat = (input("Input seat: "))
    user_id = int(input("Input user id: "))
    cursor.execute("INSERT INTO Ticket (Price, Type, Seat, UserID) "
                   "VALUES (%s, %s, %s, %s)",
                   (price, ticket_type, seat, user_id))


def read_tickets(cursor):
    logger.info("Reading all tickets")
    time.sleep(0.5)
    cursor.execute("SELECT * FROM Ticket")
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_tickets(cursor):
    logger.info("Updating ticket")
    time.sleep(0.5)
    ticket_id = int(input("Input ticket id to change: "))
    new_price = float(input("Input new price: "))
    new_type = input("Input new type(VIP/Regular): ")
    new_seat = input("Input new seat: ")
    cursor.execute("UPDATE Ticket SET Price = %s, Type = %s, Seat = %s WHERE TicketID = %s",
                   (new_price, new_type, new_seat, ticket_id))


def delete_tickets(cursor, conn):
    logger.info("Delete ticket")
    time.sleep(0.5)
    ticket_id = int(input("Input ticket to delete: "))
    cursor.execute("DELETE FROM Ticket "
                   "WHERE TicketID = %s;", (ticket_id,))
