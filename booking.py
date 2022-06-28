# Create a reservation system which books airline seats or hotel rooms. 
# It charges various rates for particular sections of the plane or hotel. 
# Example, first class is going to cost more than coach. 
# Hotel rooms have penthouse suites which cost more. 
# Keep track of when rooms will be available and can be scheduled.


# current issue: create a way for the hotel to be able to book someone over multiple days

# variables
penthouse = [" "]*3
regular = [" "]*7
airline_calendar = {}
hotel_calendar = {}
for key in range(1,366):
    airline_calendar[key] = None
    hotel_calendar[key] = None


# create airline class
class Airline():

    def __init__(self, name):
        self.name = name
        self.first_class = [" "]*3
        self.business = [" "]*7
    
    def booking(self, date, airline_calendar):
        if airline_calendar[date] == None:
            airline_calendar[date] = (self.first_class, self.business)
        else:
            pass

        self.choice = input("Where would you like to sit? ")
        if " " not in airline_calendar[date][0] and " " not in airline_calendar[date][1]:
            print("We have no seats available, we appologize")
        else:
            if self.choice == "first class":
                for seat in range(len(airline_calendar[date][0])):
                    if airline_calendar[date][0][seat] != " ":
                        print("No seat here")
                        
                    else:
                        airline_calendar[date][0][seat] = self.name
                        break

            elif self.choice == "business":
                for seat in range(len(airline_calendar[date][1])):
                    if airline_calendar[date][1][seat] != " ":
                        print("No seat here")

                    else:
                        airline_calendar[date][1][seat] = self.name
                        break

    def fly_date(self, date, airline_calendar):
        airline_calendar[date] = self.first_class + self.business


            
# create hotel class
class Hotel():

    def __init__(self, name):
        self.name = name
        self.penthouse = [" "]*3
        self.regular = [" "]*7

    def booking(self, begin_date, end_date, hotel_calendar):
        for date in range(begin_date, end_date):
            if hotel_calendar[date] == None:
                hotel_calendar[date] = (self.penthouse, self.regular)
            else:
                pass

        self.choice = input("Where would you like to stay? ")
        if " " not in self.penthouse and " " not in self.regular:
            print("We have no rooms available, we appologize")
        else:
            if self.choice == "penthouse":
                for room in range(len(self.penthouse)):
                    if self.penthouse[room] != " ":
                        print("No room here")
                        
                    else:
                        self.penthouse[room] = self.name
                        return self.penthouse + self.regular

            elif self.choice == "regular":
                for room in range(len(self.regular)):
                    if self.regular[room] != " ":
                        print("No room here")

                    else:
                        self.regular[room] = self.name
                        return self.penthouse + self.regular   


if __name__ == "__main__":
    while True == True:
        name = input("What is your name? ") 
        date = int(input("What day would you like to fly? 1-365: "))  
        airline = Airline(name)
        hotel = Hotel(name, penthouse, regular)
        print(airline.booking(date, airline_calendar))
        print(airline_calendar)
        """print(hotel.booking())
        if " " not in airline.first_class and " " not in airline.business:
            print("The plane is full")
            break
        if " " not in hotel.penthouse and " " not in hotel.regular:
            print("The plane is full")
            break"""