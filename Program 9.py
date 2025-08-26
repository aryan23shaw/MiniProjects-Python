import pickle

def update_marks(roll, new_marks):
    with open("students.dat", "rb+") as file:
        data = pickle.load(file)
        for student in data:
            if student['roll'] == roll:
                student['marks'] = new_marks
                print(f"Updated marks for roll {roll}.")
                break
        else:
            print("Roll number not found.")
        file.seek(0)
        pickle.dump(data, file)
