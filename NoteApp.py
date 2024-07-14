notes = {}

def add_note():
    print("Enter the title for your note:")
    title = input()
    #print("Enter the date time for your note(optional): DD/MM/YY")
    #date_time = int(input())
    print("Note description:")
    note = input()
    notes[title] = note
    print("Note succesfully added!")

def view_notes():
    print("Do you want to:")
    print("1. View a specific note")
    print("2. View all notes")
    answer = input()
        
    if answer == "1":
        print("Choose the note you want to view:")
        for key in notes.keys():
            print(key)
        choice = input()
        if choice in notes:
            print(f"{choice}:\n{notes[choice]}")
        else:
            print("Note doen't exist")
    elif answer == "2":
        for key, value in notes.items():
            print(f"{key}:\n{value}")
    else:
        print("Please enter a valid answer")

def delete_notes():
    print("Choose note to be deleted:")
    for key in notes.keys():
        print(key)
    choice = input()
    if choice in notes:
        del notes[choice]
        print("Note succesfully deleted!")
    else:
        ("The note you want to delete doesn't exist")

def edit_notes():
    print("Choose the note you want to edit:")
    for key in notes.keys():
        print(key)
    choice = input()
    if choice in notes:
        print(f"{choice}: {notes[choice]}")
        del notes[choice]
        print("Edit title:")
        title = input()
        print("(Tip: instead of re-writing everything,\ncopy paste the previous note description and edit as you want)")
        print("Edit note:")
        note = input()
        notes[title] = note
        print("Note succesfully edited!")
    else:
        ("The note you want to edit doesn't exist")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Add note")
        print("2. View note")
        print("3. Delete note")
        print("4. Edit note")
        print("5. Exit")
        choice = input()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            edit_notes()
        elif choice == "5":
            break
        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()