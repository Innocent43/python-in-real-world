# 09 | Classes and methods
# 25. Digital Wallet
# Scenario: A fintech simulator lets customers deposit and withdraw funds.
# Your task: Create Wallet(owner, balance=0) with deposit(amount), withdraw(amount) and get_balance() methods.
# Reject nonpositive amounts and withdrawals exceeding balance.
# Example: Wallet("Ada",10000); deposit(5000); withdraw(3000) -> 12000
# Requirement: Methods should update instance state safely.


# Solution
class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        self.balance += amount
        return "Deposit successful"
    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return "Withdrawal successful"
    def get_balance(self):
        return self.balance
wallet = Wallet("Ada", 10_000)
print(wallet.deposit(5_000))
print(wallet.withdraw(3_000))
print(wallet.get_balance())



# 26. Restaurant Table Reservations
# Scenario: A restaurant has tables with fixed seat capacities and a booking status.
# Your task: Create RestaurantTable(number, capacity) with reserve(party_size), cancel() and status() methods.
# Reject bookings larger than capacity and double reservations.
# Example: Table(4, 6).reserve(5) -> success; reserve(2) -> already reserved
# Requirement: Cancellation should make the table available again.


# Solution
class RestaurantTable:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.reserved = False
    def reserve(self, party_size):
        if self.reserved:
            return "Already reserved"
        if party_size <= 0:
            return "Party size must be positive"
        if party_size > self.capacity:
            return "Party exceeds capacity"
        self.reserved = True
        return "Reservation successful"
    def cancel(self):
        self.reserved = False
        return "Reservation cancelled"
    def status(self):
        return "Reserved" if self.reserved else "Available"
table = RestaurantTable(4, 6)
print(table.reserve(5))
print(table.reserve(2))
print(table.status())
print(table.cancel())
print(table.status())

# How it works / syntax: reserved is a Boolean state: True or False. reserve() checks current state and capacity
# before changing it. The conditional expression in status() chooses a string. cancel() makes the table available again



# 27. Student Course Enrollment
# Scenario: A training center caps each course at 3 students.
# Your task: Create Course(title, capacity=3) with enroll(name), remove(name) and roster() methods. Prevent
# duplicates and full-class enrollment.
# Example: enroll("Ada") -> enrolled; enroll("Ada") -> already enrolled
# Requirement: Do not expose the internal list directly from roster(); return a copy


# Solution
class Course:
    def __init__(self, title, capacity=3):
        self.title = title
        self.capacity = capacity
        self._students = []
    def enroll(self, name):
        if name in self._students:
            return "Already enrolled"
        if len(self._students) >= self.capacity:
            return "Course full"
        self._students.append(name)
        return "Enrolled"
    def remove(self, name):
        if name not in self._students:
            return "Student not found"
        self._students.remove(name)
        return "Removed"
    def roster(self):
        return self._students.copy()
course = Course("Python")
print(course.enroll("Ada"))
print(course.enroll("Ada"))
print(course.enroll("Bola"))
print(course.enroll("Ife"))
print(course.enroll("Chidi"))
print(course.roster())

#  _students is an internal list by convention. len() checks current enrollment. copy() returns a
# separate list so callers cannot directly alter the course's internal roster. remove() removes one matching student.
