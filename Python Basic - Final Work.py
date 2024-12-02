
# 1.
for i in range(12, 24 + 1):
    print(i)
print()

# 2.
for i in range(7, 31 + 1):
    if i % 2 != 0:
        print(i)
print()

# 3.
for x in range(-20, 10 + 1):
    if x % 2 == 0:
        print(x)

# 4.
for i in range(1, 45 + 1):
    if i % 3 == 0:
        print("Fizz", i)
    if i % 5 == 0:
        print("Buzz", i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
print()


# 5.
def calculate(arr):
    total = 0
    for arr in arr:
        total += arr
    return total


numbers = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
result = calculate(numbers)
print(result)
print()

# 6.
students = [
    {'id': 1, 'first_name': 'Itay', 'last_name': 'Trauner', 'age': 21, 'country': 'Isreal', 'city': 'Hadera'},
    {'id': 2, 'first_name': 'Daniel', 'last_name': 'Chaba', 'age': 25, 'country': 'Canada', 'city': 'Toronto'},
    {'id': 3, 'first_name': 'Maddy', 'last_name': 'Rose', 'age': 20, 'country': 'Russia', 'city': 'Moscow'}

]


def delete_property(students1, property_name):
    for student in students1:
        if property_name in student:
            del student[property_name]
    return students1


def print_student_property(students1):
    for student in students1:
        print("student Details: ")
        for key, value in student.items():
            print(f"{key}: {value}")
        print("---")


def age_student(student):
    sorted_age = sorted(student, key=lambda s: s["age"], reverse=True)
    return sorted_age


students = delete_property(students, 'country')
print_student_property(students)
sorted_students = age_student(students)
print("Sorted Students by Age:")
age_student(sorted_students)

# 7.
our_pets = [
    {
        "animal_type": "cat",
        "names": [
            "Meowzer",
            "Fluffy",
            "Kit-Cat"
        ]
    },
    {
        "animal_type": "dog",
        "names": [
            "Spot",
            "Bowser",
            "Frankie"
        ]
    }
]

def print_cat(pets):
    for pet in pets:
        if pet["animal_type"] == "cat":
            print(f"animalType: {pet["animal_type"]}")
            print(f"names: {', '.join(pet['names'])}")

def print_all_animal_type(pets , animal_type):
    found = False
    for pet in pets:
        if pet["animal_type"] == animal_type:
            found = True
            print(f"animalType: {pet['animal_type']}")
            print(f"names: {', '.join(pet['names'])}")
            break
    if not found:
        print(f"No animals of type {animal_type} found")

def add_name_to_animals(pets, animal_name):
    for pet in pets:
        if animal_name not in pet['names']:
            pet['names'].append(animal_name)

print_cat(our_pets)
print_all_animal_type(our_pets, "cat")
print_all_animal_type(our_pets, "dog")
print_all_animal_type(our_pets, "bird")
add_name_to_animals(our_pets, "Buddy")
add_name_to_animals(our_pets, "Meowzer")
print(our_pets)