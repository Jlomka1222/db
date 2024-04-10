from loguru import logger
import time


def create_users(cursor):

    logger.info("Creating user")
    time.sleep(0.5)
    fullname = input("Input fullname: ")
    age = int(input("Input age: "))
    contactinfo = input("Input contact information(phone number): ")
    email = input("Input email: ")
    cursor.execute("INSERT INTO Users (FullName, Age, ContactInfo, Email) VALUES (%s, %s, %s, %s)",
                  (fullname, age, contactinfo, email))


def read_users(cursor):
    logger.info("Reading all users")
    time.sleep(0.5)
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_users(cursor):
    logger.info("Updating user")
    time.sleep(0.5)
    id_user = int(input("Input user id to change information: "))
    fullname = input("Input fullname to update: ")
    age = int(input("Input age to update: "))
    contactinfo = input("Input contact information(phone number) to update: ")
    email = input("Input email to update: ")
    cursor.execute("UPDATE Users "
                   "SET FullName = %s, Age = %s, ContactInfo = %s, Email = %s "
                   "WHERE UserID = %s;",
                   (fullname, age, contactinfo, email, id_user))


def delete_users(cursor):
    logger.info("Delete user")
    time.sleep(0.5)
    id_user = input("Input id to delete: ")
    cursor.execute("DELETE FROM Users "
                   "WHERE UserID = %s;", (id_user,))

