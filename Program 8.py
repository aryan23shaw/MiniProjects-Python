import pickle

def create_binary_file():
    data = [{'roll': 1, 'name': 'Alice'}, {'roll': 2, 'name': 'Bob'}]
    with open("students.dat", "wb") as file:
        pickle.dump(data, file)

def search_roll_number(roll):
    with open("students.dat", "rb") as file:
        data = pickle.load(file)
        for student in data:
            if student['roll'] == roll:
                print("Name:", student['name'])
                return
        print("Roll number not found.")

create_binary_file()
search_roll_number(int(input("Enter roll number to search: ")))
