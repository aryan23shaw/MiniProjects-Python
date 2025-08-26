import csv

def create_csv():
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["EmpID", "Name", "Mobile"])
        writer.writerows([
            [101, "Alice", "1234567890"],
            [102, "Bob", "9876543210"]
        ])

def update_csv(empid, new_mobile):
    rows = []
    found = False
    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if row[0] == str(empid):
            row[2] = new_mobile
            found = True
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    if found:
        print("Record updated.")
    else:
        print("EmpID not found.")

create_csv()
update_csv(101, "1122334455")
