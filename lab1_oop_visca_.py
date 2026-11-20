

class Greeter:
    def greet(self):
        print("Hello! Welcome to OOP!")


person = Greeter()
person.greet()


# ============================================================
# PART 2 & 3: Classes, Objects, and Methods - Car
# ============================================================

class Car:
    wheels = 4  # Class attribute shared by all cars

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = 0  # Each car starts with 0 kilometers driven

    def drive(self, km):
        if km > 0:
            self.km += km
            print(f"The car drove {km} km.")
        else:
            print("Invalid distance!")

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


# Create three Car objects
car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)

print("\n--- PART 2 & 3: CAR TESTS ---")
print("Car 1:", car1)
print("Car 2:", car2)
print("Car 3:", car3)
print("Wheels:", Car.wheels)

car1.drive(10)
car1.drive(5)
car2.drive(20)
car3.drive(-5)

print("Car 1 distance:", car1.km, "km")
print("Car 1 age:", car1.age(2026), "years old")
print("Car 2 distance:", car2.km, "km")
print("Car 2 age:", car2.age(2026), "years old")
print("Car 3 distance:", car3.km, "km")
print("Car 3 age:", car3.age(2026), "years old")


# ============================================================
# PART 4: Mini Project - Library Book
# ============================================================

class Book:
    counter = 0  # Counts how many Book objects have been created

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False  # False means the book is available
        Book.counter += 1

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'"{self.title}" successfully borrowed!')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f'"{self.title}" successfully returned!')
        else:
            print(f'"{self.title}" was not borrowed.')

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"


# Create some Book objects and test the methods
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Little Prince", "Antoine de Saint-Exupery")
book3 = Book("Charlotte's Web", "E.B. White")

print("\n--- PART 4: LIBRARY BOOK TESTS ---")
print(book1)
print(book2)
print(book3)
print("Total books created:", Book.counter)

book1.borrow()
print(book1)

book1.borrow()  # Try borrowing it again
book1.return_book()
print(book1)

book1.return_book()  # Try returning it when it is already available

print("Book object representation:", repr(book2))
