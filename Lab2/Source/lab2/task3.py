#Airline Booking system
#5 classes : Bookingcls, seat, person, passenger,flight


#Booking Class consists of economy and business
class BookingCls:
    #init Constructor
    def __init__(self, y, z):
        self.economy_class = y
        self.business_class = z

    def get_Economy_class(self):
        print("Class:" + str(self.economy_class))

    def get_business_class(self):
        print("Class:" + str(self.business_class))

#Flight Class Consists of flight name and number
class Flight:
    #init constructor
    def __init__(self, i, j):
        self.flight_number = i
        self.flight_name = j
    #private data member for flight number
    def __get_flight_number(self):
        print("FlightNumber:" + str(self.flight_number))

    def get_flight_name(self):
        print("FlightName:" + str(self.flight_name))

#class for seat no and letter
class Seat:
    def __init__(self, no, lt):                      ###INIT CONSTRUCTOR
        self.seat_number = no
        self.seat_letter = lt

    def get_seat_number(self):
        print("SeatNumber:" + str(self.seat_number))

    def get_seat_letter(self):
        print("SeatLetter:" + str(self.seat_letter))
#person class shows his details in it including name,age and ticket

class Person:
    count = 0
    #init constructor
    def __init__(self, a, b, c, d):
        self.person_first_name = a
        self.person_last_name = b
        self.__person_age = c
        self.person_ticket_ID = d

        Person.count += 1
    #fname
    def get_person_first_name(self):
        print("FirstName:" + str(self.person_first_name))
    #lname
    def get_person_last_name(self):
        print("LastName:" + str(self.person_last_name))
    #Age
    def get_person_age(self):
        print("Age:" + str(self.__person_age))
    #Ticket
    def get_person_ticket_ID(self):
        print("TicketID:" + str(self.person_ticket_ID))
        print()


person1 = Person("Rakesh", "Reddy", "24", "123456789")
person2 = Person("Lokesh", "Reddy", "26", "98765432")

#person1 calling defined functions
person1.get_person_first_name()
person1.get_person_age()
person1.get_person_ticket_ID()

#person2 calling defined functions
person2.get_person_first_name()
person2.get_person_age()
person2.get_person_ticket_ID()


#MultiInheritence

# creating one class for the passenger inheriting person,seat,flight and Booking classes ####
#Passenger Cls defines all details
#using 4 primary classes
class Passenger(Person, Seat, BookingCls, Flight):
    #init constructor
    def __init__(self, a, b, c, d, i,j, no, lt, y, z):
        Person.__init__(self, a, b, c, d)
        Flight.__init__(self, i, j)
        Seat.__init__(self, no, lt)
        # super class constructor calling
        BookingCls.__init__(self, y, z)


### Person3 OBJECT###
person3 = Passenger("Raj", "Chakravarthy", "60", "56784385753","12346","AirIndia", "21", "F", "economy",
                    "business")
person3.get_person_first_name()
person3.get_person_last_name()
person3.get_person_age()
person3.get_seat_number()
person3.get_seat_letter()
person3.get_flight_name()
##flight no is private..so i cant access it
#person3.get_flight_number()
person3.get_Economy_class()
