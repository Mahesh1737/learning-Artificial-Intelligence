import re
import pandas as pd

# The unstructured text data from the image
text_data = [
    "Contact John Smith at (555) 123-4567 or email john.smith@company.com. Address: 123 Main St, New York, NY 10001",
    "Jane Doe can be reached at 555.987.6543 or jane_doe@email.org. Lives at 456 Oak Avenue, Los Angeles, CA 90210",
    "Call Bob Johnson: +1-555-111-2222, email: bob@website.net, 789 Pine Road, Chicago, IL 60601",
    "Alice Brown - Phone: 5551234567, alice.brown@domain.com, 321 Elm Street, Houston, TX 77001"
]

# List to hold the dictionaries of extracted data
extracted_records = []

# Define regex patterns for each task
phone_pattern = re.compile(r"(\+?1-?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
name_pattern = re.compile(r"([A-Z][a-z]+ [A-Z][a-z]+)")
address_pattern = re.compile(r"(\d+[\w\s\.,]+(?:[A-Z]{2}\s\d{5}))")
state_pattern = re.compile(r"([A-Z]{2})\s\d{5}")

# Loop through each string in the text data to extract information
print("--- Starting Extraction for Each Task ---")
for i, entry in enumerate(text_data):
    print(f"\n--- Processing Entry {i+1} ---")
    
    # Task 1: Extract phone number
    phone = re.search(phone_pattern, entry)
    phone_result = phone.group(0) if phone else None
    print(f"Task 1 (Phone Number): {phone_result}")

    # Task 2: Extract email address
    email = re.search(email_pattern, entry)
    email_result = email.group(0) if email else None
    print(f"Task 2 (Email Address): {email_result}")

    # Task 3: Extract name
    name = re.search(name_pattern, entry)
    name_result = name.group(1) if name else None
    print(f"Task 3 (Name): {name_result}")

    # Task 4: Extract complete address
    address = re.search(address_pattern, entry)
    address_result = address.group(1).strip() if address else None
    print(f"Task 4 (Complete Address): {address_result}")

    # Task 5: Extract state abbreviation
    state = re.search(state_pattern, entry)
    state_result = state.group(1) if state else None
    print(f"Task 5 (State): {state_result}")
    
    # --- Storing the extracted data in a dictionary ---
    record = {
        "Name": name_result,
        "Phone": phone_result,
        "Email": email_result,
        "Address": address_result,
        "State": state_result
    }
    extracted_records.append(record)

# Task 6: Create a structured DataFrame from the extracted information
df = pd.DataFrame(extracted_records)

# Display the final DataFrame
print("\n\n--- Task 6: Final Structured DataFrame ---")
print(df)