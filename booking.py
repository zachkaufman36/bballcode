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
cost_dict = {}
for key in range(1,366):
    airline_calendar[key] = None
    hotel_calendar[key] = None


# create airline class
class Airline():

    def __init__(self, name):
        self.name = name
        self.first_class = [" "]*3
        self.business = [" "]*7
    
    def booking(self, airline_choice, date, airline_calendar):
        if airline_calendar[date] == None:
            airline_calendar[date] = (self.first_class, self.business)
        else:
            pass
        if " " not in airline_calendar[date][0] and " " not in airline_calendar[date][1]:
            print("We have no seats available, we appologize")
        else:
            if airline_choice == "first class":
                for seat in range(len(airline_calendar[date][0])):
                    if airline_calendar[date][0][seat] != " ":
                        print("No seat here")
                        
                    else:
                        airline_calendar[date][0][seat] = self.name
                        break

            elif airline_choice == "business":
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

    def booking(self, hotel_choice, begin_date, end_date, hotel_calendar):
        for date in range(begin_date, end_date+1):
            if hotel_calendar[date] == None:
                hotel_calendar[date] = (self.penthouse, self.regular)
            else:
                pass

        if " " not in hotel_calendar[date][0] and " " not in hotel_calendar[date][1]:
            print("We have no rooms available, we appologize")
        else:
            if hotel_choice == "penthouse":
                for room in range(len(hotel_calendar[date][0])):
                    if hotel_calendar[date][0][room] != " ":
                        print("No room here")
                        
                    else:
                        hotel_calendar[date][0][room] = self.name
                        break

            elif hotel_choice == "regular":
                for room in range(len(hotel_calendar[date][1])):
                    if hotel_calendar[date][1][room] != " ":
                        print("No room here")

                    else:
                        hotel_calendar[date][1][room] = self.name
                        break

class Cost():

    def __init__(self):
        self.fc_cost = 1000
        self.b_cost = 500
        self.p_cost = 1000
        self.r_cost = 500
        self.total_cost = 0

    def price(self, airline_choice, hotel_choice, begin_date, end_date, name, cost_dict):
        if airline_choice == "first class":
            self.total_cost += self.fc_cost
            cost_dict[name] = self.total_cost
            
        elif airline_choice == "business":
            self.total_cost += self.b_cost
            cost_dict[name] = self.total_cost
            
        if hotel_choice == "penthouse":
            self.days_stayed = end_date - begin_date + 1
            self.total_cost += self.p_cost * self.days_stayed
            cost_dict[name] = self.total_cost
            
        elif hotel_choice == "regular":
            self.days_stayed = end_date - begin_date + 1
            self.total_cost += self.r_cost * self.days_stayed
            cost_dict[name] = self.total_cost
            

if __name__ == "__main__":
    while True == True:
        name = input("What is your name? ") 
        date = int(input("What day would you like to fly? 1-365: "))  
        airline_choice = input("Where would you like to sit? ")
        airline = Airline(name)
        hotel = Hotel(name)
        print(airline.booking(airline_choice, date, airline_calendar))
        for key in range(1,366):
            if airline_calendar[key] != None:
                print(f"{key}: {airline_calendar[key]}")
        begin_date = int(input("Please enter a begin date for your hotel stay: "))
        end_date = int(input("Please enter an end date for your hotel stay: "))
        hotel_choice = input("Where would you like to stay? ")
        print(hotel.booking(hotel_choice, begin_date, end_date, hotel_calendar))
        for key in range(1,366):
            if hotel_calendar[key] != None:
                print(f"{key}: {hotel_calendar[key]}")
        if " " not in airline.first_class and " " not in airline.business and " " not in hotel.penthouse and " " not in hotel.regular:
            print("There is nothing available for that day that you requested, please choose a different day")
            continue
        cost = Cost()
        cost.price(airline_choice, hotel_choice, begin_date, end_date, name, cost_dict)
        print(cost_dict)
        finish = input("Would you like to continue? ")
        if finish == "yes":
            continue
        else:
            break
        
