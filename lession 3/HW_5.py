import json
import pprint
import csv
import re


def traders:
    with open('traders.txt', 'r') as file:
        traders_inn = file.read()
    with open('traders.json', 'r') as file:
        data = json.load(file)

    traders = []

    for trader in data:
        if trader['inn'] in traders_inn:
            traders.append(trader)

    with open('traders.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for i in traders:
            writer.writerow([i['inn'], i['ogrn'], i['address']])


email_exprission = re.compile(r'\b[a-zA-Z0-9._%+-]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
inn_org_exprission = re.compile(r'\b\d{10}\b')
inn_person_exprission = re.compile(r'\b\d{12}\b')


def email_from_efrsb(file):
    with open(file, "r") as f:
        message = json.load(f)
    results = {}

    for i in message:
        emails = re.findall(email_pattern, i['msg_text'])
        for email in emails:
            email = email.lower()
            searched = results.get(i['publisher_inn'])
            if searched and email not in searched:
                results[i['publisher_inn']].append(email)
            elif not searched:
                new_item = {i['publisher_inn']: [email]}
                results.update(new_item)
    inverted = {}
    for inn, emails in results.items():
        for email in emails:
            searched = inverted.get(email)
            if searched and inn not in searched:
                inverted[email].append(inn)
            elif not searched:
                new_item = {email: [inn]}
                inverted.update(new_item)

    with open('emails.json', "w") as f:
        json.dump(results, f)
    print("stop")


email_from_efrsb("1000_efrsb_messages.json")