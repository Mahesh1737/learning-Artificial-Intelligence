import pandas as pd
import re

# text = "The phone number is 123-456-7890 and the email is john.doe@example.com"

# phone_pattern = r'\d{3}-\d{3}-\d{4}'
# email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# phone_match = re.search(phone_pattern, text)
# email_match = re.search(email_pattern, text)    

# print("Phone Number:", phone_match.group() if phone_match else "Not found")
# print("Email:", email_match.group() if email_match else "Not found")    




# *Combination of both search and match

text = "Python is great. Python is powerful. PYTHON is popular."

#re.search() finds first match
# first_match = re.search(r'Python', text)
# print(f"First match: {first_match.group()} at position {first_match.start()}-{first_match.end()}")

#re.match() matches from beginning of string
# match_from_start = re.match(r'Python', text)
# print(f"Match from start: {match_from_start.group() if match_from_start else 'No match'}")

#re.findall() finds all matches
# all_matches = re.findall(r'Python', text)
# print(f"All matches: {all_matches}")

#Case-insensitive search
# all_matches_ci = re.findall(r'python', text, re.IGNORECASE)
# print(f"Case-insensitive matches: {all_matches_ci}")

#re.finditer() returns iterator of match objects
# for match in re.finditer(r'Python', text):
#     print(f"Found {match.group()} at {match.start()}-{match.end()}")

# #Groups in patterns
# phone_text = "Call me at 123-456-7890 or 987-654-3210"
# phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
# for match in re.finditer(phone_pattern, phone_text):
#     print(f"Full number: {match.group(0)}")
#     print(f"Area code: {match.group(1)}")
#     print(f"Exchange: {match.group(2)}")
#     print(f"Number: {match.group(3)}")


