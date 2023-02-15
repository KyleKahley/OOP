from datetime import date


class Student:
    def __init__(self, idnumber, name, DoB, classification):
        self.__StudentID = idnumber
        self.__Name = name
        self.__DoB = DoB
        self.__classification = classification
        self.__age = 0
        self.__registrationdate = ""

    def currentage(self):
        today = date.today()
        year = today.year
        DoB = self.__DoB.split("/")
        dob_year = int(DoB[2])
        self.__age = year - dob_year

    def registerdate(self):
        if self.__classification == "Sr":
            self.__registrationdate = "Seniors - 4/1/ thru 4/3"
        elif self.__classification == "Jr":
            self.__registrationdate = "Juniors - 4/4 thru 4/6"
        elif self.__classification == "S":
            self.__registrationdate = "Sophomores - 4/7 thru 4/9"
        elif self.__classification == "F":
            self.__registrationdate = "Freshmen = 4/10 thru 4/12"
        else:
            self.__registrationdate = "classification not found"

    def get_age(self):
        return self.__age

    def get_registrationdates(self):
        return self.__registrationdate
