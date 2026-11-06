# 2 | Functions
# 04. Food Delivery Fee Estimator
# Scenario: A food business serves multiple customers. Delivery costs NGN 500 plus NGN 150 per kilometre. Orders
# of at least NGN 15,000 get free delivery.
# Your task: Write calculate_delivery(order_amount, distance_km) returning the delivery fee; call it for at least three
# test orders.


def calculate_delivery(order_amount, distance_km):
    if order_amount >= 15_000:
        return 0
    return 500 + 150 * distance_km
print(calculate_delivery(12_000, 4))
print(calculate_delivery(15_000, 4))
print(calculate_delivery(8_000, 2))



# 05. Payroll Deduction Calculator
# Scenario: A small company deducts 5% pension and 2% health insurance from basic monthly salary.
# Your task: Write net_salary(basic_salary, bonus=0) to return the net amount after deductions on basic salary only;
# test with and without a bonus.
# Example: net_salary(100000, 10000) -> 103000.0
# Requirement: Use parameters, a default argument and a return value.

# Solution
def net_salary(basic_salary, bonus=0):
    pension = basic_salary * 0.05
    insurance = basic_salary * 0.02
    return basic_salary - pension - insurance + bonus
print(net_salary(100_000, 10_000))
print(net_salary(100_000))
print(net_salary(50_000, 0))




# 6. School Result Formatter
# Scenario: A tutor wants consistent student reports for different subjects.
# Your task: Create grade(score) returning A (70-100), B (60-69), C (50-59), D (45-49), E (40-44), or F (0-39). Create
# report(name, subject, score) using grade() and returning a formatted string.
# Example: report("Ada", "Python", 74) -> Ada | Python | 74 | A
# Requirement: For invalid scores, return a clear error message.

# Solution
def grade(score):
    if not 0 <= score <= 100:
        return "Invalid score"
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    return "F"

def report(name, subject, score):
    result = grade(score)
    if result == "Invalid score":
        return "Error: score must be from 0 to 100"
    return f"{name} | {subject} | {score} | {result}"
print(report("Ada", "Python", 74))
print(report("Bola", "Math", 39))
print(report("Ife", "English", 101))