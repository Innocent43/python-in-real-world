# 4 | Recursion
# 10. Warehouse Box Counter
# Scenario: A warehouse stores goods in nested boxes. A box contains either individual items represented by
# numbers or smaller boxes represented by lists.
# Your task: Write recursive count_items(box) that sums all item counts regardless of nesting.
# Example: count_items([4, [2, 3], [1, [5]]]) -> 15
# Requirement: Use recursion; do not flatten with an external library.

# Solution
def count_items(box):
    total = 0
    for item in box:
        if isinstance(item, list):
            total += count_items(item)
        else:
            total += item
    return total
print(count_items([4, [2, 3], [1, [5]]]))
print(count_items([]))
print(count_items([2, [3, [4]]]))



# 11. Savings Growth by Month
# Scenario: A student saves NGN 5,000 in month 1 and increases the monthly deposit by NGN 1,000 each month.
# Your task: Write recursive total_savings(months) that returns the total deposits for n months. Define a base case for
# 0 months.
# Example: total_savings(4) -> 26000
# Requirement: Reject negative months; no loops in the recursive calculation.


def total_savings(months):
    if months < 0:
        raise ValueError("months cannot be negative")
    if months == 0:
        return 0
    deposit_this_month = 5_000 + (months - 1) * 1_000
    return deposit_this_month + total_savings(months - 1)
print(total_savings(4))
print(total_savings(1))
print(total_savings(0))



# 2. Nested Folder File Count
# Scenario: An office represents its folders as nested dictionaries. Each folder has a "files" list and a "subfolders" list.
# Your task: Write recursive count_files(folder) to count files in the folder and all descendants.
# Example: {"files":["a.pdf"],"subfolders":[{"files":["b.csv","c.txt"],"subfolders":[]}]} -> 3
# Requirement: Test both an empty folder and multiple nesting levels.

# Solution
def count_files(folder):
    current_count = len(folder.get("files", []))
    for subfolder in folder.get("subfolders", []):
        current_count += count_files(subfolder)
    return current_count
folder = {
    "files": ["a.pdf"],
    "subfolders": [
        {"files": ["b.csv", "c.txt"], "subfolders": []}
    ]
}
print(count_files(folder))
print(count_files({"files": [], "subfolders": []}))

print(count_files({"files": ["x"], "subfolders": [
    {"files": ["y"], "subfolders": [{"files": ["z"], "subfolders": []}]}
]} ))

# len() counts the files in the current folder. dict.get(key, default) safely returns an empty list if
# a key is missing. The recursive call counts each child folder; totals are added upward.