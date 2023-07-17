import datetime


def main():
    # Display programmer name, lab details, and current date and time
    print("Programmer: Michael")
    print("Lab 16.1 June 19,2023 @" + datetime.datetime.now().strftime("%H:%M:%S"))

    full_name = input("\nEnter your full name: ")

    names = full_name.split()

    initials = ""

    for name in names:
        initial = name[0].upper()

        initials += initial + "."

    print("The initials of the name you entered, " + full_name + ", are:")
    print(initials)


main()