#!/usr/bin/env python

import csv

ages = []
with open("data.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        current_age = row[2]
        if not current_age == "AGE":
            if current_age not in ages:
                ages.append(current_age)
                
print("La personne la plus agée de la liste est: " + max(ages))
print("La personne la plus jeune de la liste est: " + min(ages))
