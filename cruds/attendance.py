from loguru import logger
import time


def create_attendance(cursor):
    logger.info("Creating attendance")
    time.sleep(0.5)
    concert_id = input("Enter ConcertID: ")
    user_id = input("Enter UserID: ")
    attendance_status = input("Enter AttendanceStatus: ")
    cursor.execute("INSERT INTO Attendance (ConcertID, UserID, AttendanceStatus) VALUES (%s, %s, %s)",
                   (concert_id, user_id, attendance_status))


def read_attendance(cursor):
    logger.info("Read all attendance")
    time.sleep(0.5)
    cursor.execute("SELECT * FROM Attendance")
    time.sleep(0.5)
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_attendance(cursor):
    logger.info("Updating attendance")
    time.sleep(0.5)
    concert_id = input("Enter ConcertID to update: ")
    user_id = input("Enter UserID to update: ")
    new_attendance_status = input("Enter new AttendanceStatus: ")
    cursor.execute("UPDATE Attendance SET AttendanceStatus = %s WHERE ConcertID = %s AND UserID = %s",
                   (new_attendance_status, concert_id, user_id))


def delete_attendance(cursor):
    logger.info("Delete attendance")
    time.sleep(0.5)
    concert_id_to_delete = input("Enter ConcertID to delete: ")
    user_id_to_delete = input("Enter UserID to delete: ")
    cursor.execute("DELETE FROM Attendance WHERE ConcertID = %s",
                   (concert_id_to_delete,))
