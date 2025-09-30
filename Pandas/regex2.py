import re

text = "The date is 12/31/2023 and another date is 01/15/2024"


# Basic substitution
new_text= re.sub(r'\d{2}/\d{2}/\d{4}', 'DATE', text)
print(new_text)

# # Using groups in replacement
date_pattern = r'(\d{2})/(\d{2})/(\d{4})'
formatted_text = re.sub(date_pattern, r'\3-11-12', text) #YYYY-MM-DD
print(formatted_text)

# # Using a function for replacement
def format_date(match):
    month, day, year = match.groups()
    return f"{year}-{month}-{day}"
formatted_with_func = re.sub(date_pattern, format_date, text)
print(formatted_with_func)

# #Count replacements
text_with_count = re.sub(r'\d{2}/\d{2}/\d{4}', 'DATE', text, count=1) # replace only first
print(text_with_count)

# #re.subn() returns tuple with count
result, count = re.subn(r'\d{2}/\d{2}/\d{4}', 'DATE', text)
print(f"Result: {result}, Replacements: {count}")