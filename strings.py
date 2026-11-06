# 16. Customer Phone Number Cleaner
# Scenario: Customer phone numbers arrive with spaces, hyphens and sometimes Nigeria's +234 country code.
# Your task: Write normalize_phone(raw) that removes spaces/hyphens and converts a valid +234XXXXXXXXXX into
# 0XXXXXXXXXX. Reject anything not exactly 11 digits starting with 0 after normalization.
# Example: "+234 803-123-4567" -> "08031234567"
# Requirement: Accept only digits and the optional leading + sign in the country code.



# Solution
def normalize_phone(raw):
    raw = raw.strip()
    if raw.startswith("+234"):
        rest = raw[4:]
        if not all(ch.isdigit() or ch in " -" for ch in rest):
            return "Invalid phone number"
        digits = "".join(ch for ch in rest if ch.isdigit())
        normalized = "0" + digits
    else:
        if not all(ch.isdigit() or ch in " -" for ch in raw):
            return "Invalid phone number"
        normalized = "".join(ch for ch in raw if ch.isdigit())
    if len(normalized) == 11 and normalized.startswith("0"):
        return normalized
    return "Invalid phone number"
print(normalize_phone("+234 803-123-4567"))
print(normalize_phone("08031234567"))
print(normalize_phone("12345"))

#  strip() removes outer whitespace. startswith() checks country code. isdigit() validates digits.
# A comprehension keeps digits only. The final checks require exactly 11 characters and a leading 0.




# 17. Complaint Keyword Detector
# Scenario: An online store receives customer complaints as free text. Common escalation terms are "refund",
# "broken" and "fraud".
# Your task: Build contains_escalation(text) that detects these words case-insensitively as whole words, not parts of
# larger words.
# Example: "My item is BROKEN" -> True; "unbroken seal" -> False
# Requirement: Consider punctuation and word boundaries.

# solution
import re

def contains_escalation(text):
    pattern = r"\b(refund|broken|fraud)\b"
    return re.search(pattern,text,flags=re.IGNORECASE) is not None

print(contains_escalation("My item is BROKEN"))
print(contains_escalation("unbroken seal"))
print(contains_escalation("Please request a refund!"))



# 18. Invoice Reference Generator
# Scenario: A shop needs invoice references built from customer initials, a date string YYYYMMDD and a four-digit
# invoice number.
# Your task: Write invoice_ref(full_name, date, number) producing INITIALS-DATE-NNNN; remove extra spaces and
# convert initials to uppercase.
# Example: ("Ada Obi", "20261104", 27) -> "AO-20261104-0027"
# Requirement: Require at least one nonempty name and a number from 0 to 9999.


# Solution
def invoice_ref(full_name, date, number):
    names = full_name.split()
    if not names:
        raise ValueError("name is required")
    if len(date) != 8 or not date.isdigit():
        raise ValueError("date must be YYYYMMDD")
    if not isinstance(number, int) or not 0 <= number <= 9999:
        raise ValueError("number must be from 0 to 9999")
    initials = "".join(part[0] for part in names).upper()
    return f"{initials}-{date}-{number:04d}"
print(invoice_ref("Ada Obi", "20261104", 27))
print(invoice_ref("  bola   eze ", "20261105", 7))
print(invoice_ref("Ife", "20260101", 0))

#  split() removes extra spacing and creates name parts. part[0] selects each initial. join-like
# comprehension combines initials. :04d formats an integer with four digits, adding leading zeros.

