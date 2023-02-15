import StudentClass as s


def main():
    idnumber = 1001
    name = "Kyle"
    DoB = "12/29/2001"
    classification = "Jr"

    # idnumber = input('Student ID number:')
    # name = input('First and Last Name')
    # DoB = input('What is your Date of Birth? MM/DD/YYYY')
    # grade = input('What is your classification? F, S, Jr, or Sr')

    student1 = s.Student(idnumber, name, DoB, classification)

    student1.currentage()
    student1.registerdate()
    print(f"Student age is: {student1.get_age()}")
    print(f"Register Date: {student1.get_registrationdates()}")

    student2 = s.Student(idnumber, name, DoB, classification)
    student2.currentage()
    student2.registerdate()

    print(f"Student age is: {student2.get_age()}")
    print(f"Register Date{student2.get_registrationdates()}")


main()
