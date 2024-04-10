from loguru import logger
import time


def create_program(cursor):
    logger.info("Creating program")
    time.sleep(0.5)
    genre = input("Enter genre: ")
    duration = input("Enter duration (in HH:MM:SS format): ")
    description = input("Enter description: ")
    age_category = input("Enter age category: ")
    cursor.execute("INSERT INTO Program (Genre, Duration, Description, AgeCategory) VALUES (%s, %s, %s, %s)",
                   (genre, duration, description, age_category))


def read_program(cursor):
    logger.info("Reading all programs")
    cursor.execute("SELECT * FROM Program")
    time.sleep(0.5)
    records = cursor.fetchall()
    for record in records:
        print(record)


def update_program(cursor):
    logger.info("Updating program")
    time.sleep(0.5)
    program_id = input("Enter ProgramID to update: ")
    new_genre = input("Enter new genre: ")
    new_duration = input("Enter new duration (in HH:MM:SS format): ")
    new_description = input("Enter new description: ")
    new_age_category = input("Enter new age category: ")
    cursor.execute(
        "UPDATE Program SET Genre = %s, Duration = %s, Description = %s, AgeCategory = %s WHERE ProgramID = %s",
        (new_genre, new_duration, new_description, new_age_category, program_id))


def delete_program(cursor):
    logger.info("Delete program")
    time.sleep(0.5)
    program_id_to_delete = input("Enter ProgramID to delete: ")
    cursor.execute("DELETE FROM Program WHERE ProgramID = %s", (program_id_to_delete,))
