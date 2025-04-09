#Assignment 1: Designin my Own Class! 🏗️
class Estate:
    #Represents a real estate property with basic attributes.
    def __init__(self, name, location, size_sqm, price_usd):
        #Constructor to initialize an Estate object.
        self.name = name
        self.location = location
        self.size_sqm = size_sqm
        self.price_usd = price_usd
        self.is_available = True  
# Initially, the estate is assumed to be available

    def display_details(self):
        #Prints the basic details of the estate.
        print(f"Estate Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Size: {self.size_sqm} sq.m")
        print(f"Price: ${self.price_usd:,.2f}")
        print(f"Availability: {'Available' if self.is_available else 'Not Available'}")

    def mark_as_sold(self):
        #Marks the estate as sold (not available).
        if self.is_available:
            self.is_available = False
            print(f"{self.name} has been sold.")
        else:
            print(f"{self.name} is already marked as sold.")

    def get_price_per_sqm(self):
        #Calculates and returns the price per square meter.
        if self.size_sqm > 0:
            return self.price_usd / self.size_sqm
        else:
            return 0

# Inheritance Layer - Creating specialized types of estates
class ResidentialEstate(Estate):
    #Represents a residential estate, inheriting from the Estate class.
    def __init__(self, name, location, size_sqm, price_usd, bedrooms, bathrooms):
        #Constructor for ResidentialEstate.
        super().__init__(name, location, size_sqm, price_usd)
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def display_details(self):
        #Overrides the display_details method of the parent class to include residential-specific details.
        super().display_details()
        print(f"Bedrooms: {self.bedrooms}")
        print(f"Bathrooms: {self.bathrooms}")

    def calculate_mortgage(self, interest_rate, loan_term_years):
        #Calculates an estimated monthly mortgage payment.
        monthly_interest_rate = interest_rate / 12
        num_payments = loan_term_years * 12
        if monthly_interest_rate > 0:
            monthly_payment = (self.price_usd * monthly_interest_rate *
                               (1 + monthly_interest_rate)**num_payments) / \
                              ((1 + monthly_interest_rate)**num_payments - 1)
            return monthly_payment
        elif num_payments > 0:
            return self.price_usd / num_payments
        else:
            return 0

class CommercialEstate(Estate):
    #Represents a commercial estate, inheriting from the Estate class.
    def __init__(self, name, location, size_sqm, price_usd, business_type, parking_spaces):
        super().__init__(name, location, size_sqm, price_usd)
        self.business_type = business_type
        self.parking_spaces = parking_spaces

    def display_details(self):
        #Overrides the display_details method to include commercial-specific details.
        super().display_details()
        print(f"Suitable Business Type: {self.business_type}")
        print(f"Parking Spaces: {self.parking_spaces}")

    def calculate_rental_yield(self, annual_rental_income):
        #Calculates the annual rental yield as a percentage.
        if self.price_usd > 0:
            return (annual_rental_income / self.price_usd) * 100
        else:
            return 0

# Creating instances of the classes
estate1 = Estate("Green Valley Plot", "Kiambu", 500, 150000)
residential1 = ResidentialEstate("The Ridge Apartments", "Westlands", 120, 250000, 3, 2)
commercial1 = CommercialEstate("Prime Business Center", "Nairobi CBD", 1000, 1000000, "Office Space", 50)

# Demonstrating the methods and attributes
print("--- Basic Estate Details ---")
estate1.display_details()
print("\n--- Residential Estate Details ---")
residential1.display_details()
monthly_mortgage = residential1.calculate_mortgage(0.06, 30)
print(f"Estimated Monthly Mortgage: ${monthly_mortgage:,.2f}")
residential1.mark_as_sold()
print("\n--- Commercial Estate Details ---")
commercial1.display_details()
rental_yield = commercial1.calculate_rental_yield(80000)
print(f"Annual Rental Yield: {rental_yield:.2f}%")
print(f"Price per sq.m for {commercial1.name}: ${commercial1.get_price_per_sqm():.2f}")


#Assignment 2
class Animal:
    #A base class defining a common interface for animal actions.
    def __init__(self, name):
        #Constructor for the Animal class.
        self.name = name
    def move(self):
        #A general move action for animals. This will be overridden by subclasses.
    
        print(f"{self} is moving.")

class Cat(Animal):
    #A class representing a cat, inheriting from Animal.
    #Overrides the move() method to define cat-specific movement.
    def __init__(self, name):
        #Constructor for the Cat class.
        super().__init__(name)

    def move(self):
        #Overrides the move() method to print how a cat moves.
    
        print(f"{self.name} walks")

class Parrot(Animal):
    #A class representing a parrot, inheriting from Animal.
    #Overrides the move() method to define parrot-specific movement.
    def __init__(self, name):
        #Constructor for the Parrot class.
        super().__init__(name)

    def move(self):
        #Overrides the move() method to print how a parrot moves.
        print(f"{self.name} flies")

class Fish(Animal):
    #A class representing a fish, inheriting from Animal.
    #Overrides the move() method to define fish-specific movement.
    def __init__(self, name):
        #Constructor for the Fish class.
        super().__init__(name)
    def move(self):
        #Overrides the move() method to print how a fish moves.
        print(f"{self.name} swimms")
# Create instances of different animal types
my_cat = Cat("Harie")
my_parrot = Parrot("Polaris")
my_fish = Fish("Salmon")
# Demonstrate polymorphism: calling the same method on different objects results in different behaviors based on the object's class.
my_cat.move()
my_parrot.move()
my_fish.move()