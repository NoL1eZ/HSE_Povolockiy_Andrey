import re

email_pattern = re.compile(r'\b[a-zA-Z0-9._%+-]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
inn_org_pattern = re.compile(r'\b\d{10}\b')
inn_person_pattern = re.compile(r'\b\d{12}\b')

with open('1000_efrsb_messages.json', 'r') as file:
    traders_inn = file.read()