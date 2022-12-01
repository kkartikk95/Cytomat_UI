import csv

lines = list()
memberName = input("Please enter a member's name to be deleted.")
with open('Cytomat_inventory.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == memberName:
                lines.remove(row)
with open('Cytomat_inventory.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)