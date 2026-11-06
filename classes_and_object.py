# 08 | Classes and objects
# 22. Library Book Records
# Scenario: A library needs a separate record for each book.
# Your task: Create a Book class with title, author, isbn and is_available attributes. Instantiate three Book objects and
# print a clear description of each object.
# Example: Book("Python Basics","N. Okafor","BK001") -> available=True
# Requirement: Use __init__; give each object its own state.


# Solution
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    def describe(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - available={self.is_available}"
books = [
    Book("Python Basics", "N. Okafor", "BK001"),
    Book("Learning SQL", "A. Obi", "BK002"),
    Book("Web Design", "B. Eze", "BK003")
]
for book in books:
    print(book.describe())


# class defines a blueprint. __init__ runs when an object is created. self refers to the current
# object. Each book receives its own title, author, ISBN and availability. A method is a function defined inside a class.




# 23. Patient Appointment Details
# Scenario: A physiotherapy clinic records appointment information.
# Your task: Create an Appointment class with patient_name, date, time and therapist attributes. Instantiate two
# appointments and display their information.
# Example: Appointment("Ife", "2026-11-06", "09:00", "Dr Eze")
# Requirement: Store data as instance attributes; do not use class variables for patient-specific details.


# Solution
class Appointment:
    def __init__(self, patient_name, date, time, therapist):
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.therapist = therapist
    def display(self):
        return f"{self.patient_name} | {self.date} | {self.time} | {self.therapist}"
appointments = [
    Appointment("Ife", "2026-11-06", "09:00", "Dr Eze"),
    Appointment("Ada", "2026-11-06", "10:30", "Dr Obi")
]
for appointment in appointments:
    print(appointment.display())

# Each parameter is saved on self, so different appointment objects do not share patient
# details. The list stores objects, and the loop calls display() for each.



# 24. E-commerce Product Catalog
# Scenario: An online shop creates Product objects with name, price and stock.
# Your task: Create a Product class and instantiate products. Print the most expensive product and all products with
# stock below 5.
# Example: Product("Keyboard",12000,3) -> low stock
# Requirement: Use a list of objects and compare their attributes.


# Solution
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
products = [
    Product("Keyboard", 12_000, 3),
    Product("Mouse", 5_000, 10),
    Product("Monitor", 85_000, 2)
]
most_expensive = max(products, key=lambda product: product.price)
print("Most expensive:", most_expensive.name, most_expensive.price)
for product in products:
    if product.stock < 5:
        print("Low stock:", product.name, product.stock)



#  max() can compare objects using a key function. The lambda returns each product's price.
# The loop checks stock on every object. Dot notation accesses an object's attribute.