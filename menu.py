def menu():
    print("Choose tables:\n"
          "1)Users\n"
          "2)Ticket\n"
          "3)Program\n"
          "4)Artist\n"
          "5)Concert\n"
          "6)Organizer\n"
          "7)Attendance\n"
          "8)Participation\n")
    choice = int(input())
    return choice


def operation():
    print("Choose operation:\n"
          "1)Create\n"
          "2)Read\n"
          "3)Update\n"
          "4)Delete\n")
    oper = int(input())
    return oper

