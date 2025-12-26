def show_details(name, *skills, **info):
    print("Name:", name)

    print("Skills:")
    for skill in skills:
        print("-", skill)

    print("Additional Info:")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
show_details(
    "Pranit",
    "Python", "JavaScript",
    age=20,
    city="Ratnagiri"
)
