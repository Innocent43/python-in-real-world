# 10 | Inheritance
# 28. Transport Fare System
# Scenario: A logistics company calculates prices for bikes and vans differently.
# Your task: Create a Vehicle base class with plate_number and distance_km, and a fare() method. Create Bike and
# Van subclasses: bike = NGN 300 + NGN 100/km; van = NGN 1,000 + NGN 250/km. Override fare().
# Example: Bike("BK1",10).fare() -> 1300; Van("VN1",10).fare() -> 3500
# Requirement: Use super() to initialize common attributes.


# Solution
class Vehicle:
    def __init__(self, plate_number, distance_km):
        self.plate_number = plate_number
        self.distance_km = distance_km
    def fare(self):
        raise NotImplementedError("Subclass must calculate fare")
class Bike(Vehicle):
    def __init__(self, plate_number, distance_km):
        super().__init__(plate_number, distance_km)
    def fare(self):
        return 300 + 100 * self.distance_km
class Van(Vehicle):
    def __init__(self, plate_number, distance_km):
        super().__init__(plate_number, distance_km)
    def fare(self):
        return 1000 + 250 * self.distance_km
print(Bike("BK1", 10).fare())
print(Van("VN1", 10).fare())


# Vehicle is the parent class. Bike and Van inherit its common attributes. super().__init__()
# calls the parent constructor. Each child overrides fare() with its own formula.



# 29. Employee Salary System
# Scenario: A business hires full-time employees and freelancers.
# Your task: Create Employee(name) with calculate_pay(). Subclass FullTimeEmployee(name, monthly_salary) and
# Freelancer(name, hourly_rate, hours). Each subclass implements its own calculate_pay().
# Example: FullTimeEmployee("Ada",150000) -> 150000; Freelancer("Bola",5000,12) -> 60000
# Requirement: Demonstrate polymorphism by iterating through a mixed list of employees.



# Solution
class Employee:
    def __init__(self, name):
        self.name = name
    def calculate_pay(self):
        raise NotImplementedError("Subclass must implement calculate_pay")
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    def calculate_pay(self):
        return self.monthly_salary
class Freelancer(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours
    def calculate_pay(self):
        return self.hourly_rate * self.hours
staff = [FullTimeEmployee("Ada", 150_000), Freelancer("Bola", 5_000, 12)]
for employee in staff:
    print(employee.name, employee.calculate_pay())

#  Both child classes inherit name. Each defines calculate_pay() differently. The same method
# call works for both object types: this is polymorphism. The loop does not need to know the employee's specific
# subclass.



# 30. School Notification System
# Scenario: A school sends notices by email or SMS, but each message channel formats output differently.
# Your task: Create Notification(recipient, message) with send(). Implement EmailNotification and SMSNotification
# overriding send() to return an appropriate formatted string.
# Example: SMSNotification("08031234567","Exam tomorrow").send() -> SMS to 08031234567: Exam tomorrow
# Requirement: Keep common data in the parent constructor; demonstrate method overriding

# Solution
class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message
    def send(self):
        raise NotImplementedError("Subclass must format notification")
class EmailNotification(Notification):
    def send(self):
        return f"Email to {self.recipient}: {self.message}"
class SMSNotification(Notification):
    def send(self):
        return f"SMS to {self.recipient}: {self.message}"
notices = [
    EmailNotification("student@example.com", "Exam tomorrow"),
    SMSNotification("08031234567", "Exam tomorrow")
]
for notice in notices:
    print(notice.send())

#  Notification stores shared recipient and message. EmailNotification and SMSNotification
# inherit those attributes and override send(). The loop calls send() on each type and gets its own format.
