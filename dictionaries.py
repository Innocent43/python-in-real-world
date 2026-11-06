# 19. Supermarket Basket Checkout
# Scenario: Prices are stored in a dictionary, and a customer basket maps products to quantities.
# Your task: Write checkout(prices, basket) returning the total and a list of missing product names. Do not charge for
# items with missing prices.
# Example: prices={"rice":3000,"oil":2000}; basket={"rice":2,"salt":1} -> (6000,["salt"])
# Requirement: Reject negative quantities.


# Solution
def checkout(prices, basket):
    total = 0
    missing = []
    for product, quantity in basket.items():
        if quantity < 0:
            raise ValueError(f"negative quantity for {product}")
        if product not in prices:
            missing.append(product)
        else:
            total += prices[product] * quantity
    return total, missing
prices = {"rice": 3000, "oil": 2000}
print(checkout(prices, {"rice": 2, "salt": 1}))
print(checkout(prices, {"oil": 3}))
print(checkout(prices, {"rice": 0}))



# 20. Class Attendance Register
# Scenario: A teacher has an attendance dictionary mapping student names to counts of days present.
# Your task: Write mark_present(attendance, name) to increment an existing student or add a new one; write
# top_attendee(attendance) returning the name with the highest count.
# Example: {"Ada":4,"Bola":2} after mark_present(...,"Bola") -> {"Ada":4,"Bola":3}
# Requirement: For ties, use alphabetical order; handle an empty register.


# Solution
def mark_present(attendance, name):
    attendance[name] = attendance.get(name, 0) + 1
def top_attendee(attendance):
    if not attendance:
        return None
    highest = max(attendance.values())
    winners = [name for name, count in attendance.items() if count == highest]
    return sorted(winners)[0]
attendance = {"Ada": 4, "Bola": 2}
mark_present(attendance, "Bola")
print(attendance)
print(top_attendee(attendance))
print(top_attendee({}))

#  get(name, 0) returns the existing count or zero for a new student. max() finds the highest
# count. sorted() orders tied names alphabetically; [0] selects the first. Empty register returns None.


# 21. Election Poll Summary
# Scenario: A student union counts votes as a list of candidate names, possibly with mixed capitalization and spaces.
# Your task: Build a frequency dictionary, print the vote count for each candidate, and find the winner or announce a
# tie.
# Example: ["Ada", "bola", "ADA", "Bola", "Ada"] -> {"ada":3,"bola":2}; winner: ada
# Requirement: Normalize names using strip() and lower().



# Solution
votes = ["Ada", "bola", "ADA", "Bola", "Ada"]
counts = {}
for candidate in votes:
    normalized = candidate.strip().lower()
    if normalized:
        counts[normalized] = counts.get(normalized, 0) + 1
print(counts)
if not counts:
    print("No votes")
else:
    highest = max(counts.values())
    winners = sorted(name for name, count in counts.items() if count == highest)
    if len(winners) == 1:
        print("Winner:", winners[0])
    else:
        print("Tie:", ", ".join(winners))


# strip() removes spaces around names; lower() makes capitalization consistent. A dictionary
# stores each candidate's frequency. len(winners) distinguishes a single winner from a tie.