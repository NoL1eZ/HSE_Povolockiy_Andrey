import json
import pprint
import csv
import re


def traders():
    with open('traders.txt', 'r') as file:
        traders_inn = file.read()
    with open('traders.json', 'r') as file:
        data = json.load(file)

    traders_list = []

    for trader in data:
        if trader['inn'] in traders_inn:
            traders_list.append(trader)

    with open('traders.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for i in traders_list:
            writer.writerow([i['inn'], i['ogrn'], i['address']])


email_exprission = re.compile(r'\b[a-zA-Z0-9._%+-]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
inn_org_exprission = re.compile(r'\b\d{10}\b')
inn_person_exprission = re.compile(r'\b\d{12}\b')


def email_from_efrsb(file):
    with open(file, "r") as f:
        message = json.load(f)

    results_dict = {}

    for i in message:
        emails = re.findall(email_exprission, i['msg_text'])
        for email in emails:
            search = results_dict.get(i['publisher_inn'])
            if search and email.lower() not in search:
                results_dict[i['publisher_inn']].append(email)
            else:
                new_item = {i['publisher_inn']: [email]}
                results_dict.update(new_item)

    inverted_dict = {}

    for inn, emails in results_dict.items():
        for email in emails:
            search = inverted_dict.get(email)
            if search and inn not in search:
                inverted_dict[email].append(inn)
            else:
                new_item = {email: [inn]}
                inverted_dict.update(new_item)

    with open('emails.json', "w") as f:
        json.dump(results_dict, f)
    print("stop")


email_from_efrsb("1000_efrsb_messages.json")