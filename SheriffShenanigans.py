import time

print("---------------------------------------------------------")
time.sleep(2)
print("Before we start,")
time.sleep(1)
name = input("Enter your name: ")
time.sleep(2)
print("Enjoy playing my first Python Program!")
time.sleep(3)
print("Loading... (not really loading i just want to:)")
time.sleep(4)
print("---------------------------------------------------------")

def case_description1():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("*Crime Description:*")
    time.sleep(2)
    print("*A valuable diamond necklace was stolen from a high-end*")
    print("*jewelry store during business hours. The security camera footage is unclear,*") 
    print("*and there were several people in the store at the time.*")
    time.sleep(1)
    print("*Suspects:*")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was at the library reading a book.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was at the gym working out.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was at a friend's house.")
    time.sleep(1)
    print("4. 'suspect4' - States he was at the cinema watching a movie.")
    option = input("These are the crime case details, Sheriff " +name+ ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " +name+ ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Produces a library receipt, but it has no timestamp.")
            case_description1()
        elif option == "suspect2":
            print("suspect2: Provides a gym entry record,") 
            print("but it only shows his arrival time.")
            case_description1()
        elif option == "suspect3":
            print("suspect3: Has a text message conversation with her friend,")
            print("but no direct alibi.")
            case_description1()
        elif option == "suspect4":
            print("suspect4: Shows a movie ticket stub,")
            print("but it could have been bought for someone else.")
            time.sleep(2)
            print("You caught the criminal Sheriff " +name+ "! Good job.")
            main()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description1()

def case_description2():
    suspects = ["suspect1", "suspect2",  "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A luxury car was found vandalized in a quiet residential neighborhood.")
    print("The incident occurred late at night,")
    print("and several people were seen in the area around that time.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Says she was shopping at the mall.")
    time.sleep(1)
    print("2. 'suspect2' - Claims he was at home cooking dinner.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was visiting her grandmother.")
    time.sleep(1)
    print("4. 'suspect4' - States he was jogging in the park.")
    option = input("These are the crime case details, Sheriff " +name+ ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " +name+ ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Provides shopping receipts, but they are from earlier in the day.")
            time.sleep(2)
            print("You caught the criminal Sheriff " +name+ "! Good job.")
            main()
        elif option == "suspect2":  
            print("suspect2: Shows a half-cooked meal as evidence.")
            case_description2()
        elif option == "suspect3":
            print("suspect3: Has a call log with her grandmother, but it's inconclusive.")
            case_description2()
        elif option == "suspect4":
            print("suspect4: Wears jogging attire but has no witness to confirm his run.")
            case_description2()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description2()

def case_description3():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("An office was broken into over the weekend, and important documents were stolen.")
    print("The security system was disabled, suggesting inside knowledge.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Says she was having dinner at a restaurant.")
    time.sleep(1)
    print("2. 'suspect2' - Claims he was attending a concert.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was watching TV at home.")
    time.sleep(1)
    print("4. 'suspect4' - States he was out of town on a business trip.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Provides a restaurant receipt, but no one remembers seeing her.")
            case_description3()
        elif option == "suspect2":
            print("suspect2: Shows a concert ticket, but the venue was crowded.")
            case_description3()
        elif option == "suspect3":
            print("suspect3: Her TV was found on standby, suggesting she was not watching it at the time of the break-in.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect4":
            print("suspect4: Provides hotel receipts and travel tickets.")
            case_description3()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description3()

def case_description4():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A priceless painting was stolen from a private gallery during an exclusive event.")
    print("The thief was careful not to leave any traces behind.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Says she was walking her dog.")
    time.sleep(1)
    print("2. 'suspect2' - Claims he was at a friend's party.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was at a yoga class.")
    time.sleep(1)
    print("4. 'suspect4' - States he was at a café writing.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Has a photo of her walking her dog, but it lacks a timestamp.")
            case_description4()
        elif option == "suspect2":
            print("suspect2: No one at the party remembers seeing him there.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect3":
            print("suspect3: Shows a yoga class sign-in sheet.")
            case_description4()
        elif option == "suspect4":
            print("suspect4: Has a receipt from the café.")
            case_description4()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description4()

def case_description5():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A bank was robbed in broad daylight. The robbers were masked,")
    print("but witnesses saw four people acting suspiciously before the robbery.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was at a nearby coffee shop.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was waiting for a bus.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was in a meeting at work.")
    time.sleep(1)
    print("4. 'suspect4' - States he was visiting a friend.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Provides a coffee shop receipt, but it lacks a timestamp.")
            case_description5()
        elif option == "suspect2":
            print("suspect2: Bus records show he didn't board any bus.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect3":
            print("suspect3: Has a meeting schedule, but no one recalls her being there.")
            case_description5()
        elif option == "suspect4":
            print("suspect4: The friend doesn't remember the visit.")
            case_description5()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description5()

def case_description6():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A high-end jewelry store was robbed at night. The security system was tampered with,")
    print("indicating that the thief had prior knowledge of the system.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was out of town.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was at a bar.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was at home asleep.")
    time.sleep(1)
    print("4. 'suspect4' - States he was working late at the office.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Provides travel tickets, but the dates are inconclusive.")
            case_description6()
        elif option == "suspect2":
            print("suspect2: Has a bar receipt, but it doesn't match the timeline.")
            case_description6()
        elif option == "suspect3":
            print("suspect3: Has no proof of being at home.")
            case_description6()
        elif option == "suspect4":
            print("suspect4: Security footage shows him near the jewelry store around the time of the robbery.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description6()
            
def case_description7():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A fire broke out in a warehouse, causing significant damage. Witnesses reported seeing four individuals in the vicinity.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was at a nearby park.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was driving home.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was at a friend's house.")
    time.sleep(1)
    print("4. 'suspect4' - States he was shopping at a mall.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: No one recalls seeing her at the park.")
            case_description7()
        elif option == "suspect2":
            print("suspect2: Car records show his route, but it doesn't match the timeline.")
            case_description7()
        elif option == "suspect3":
            print("suspect3: The friend's alibi is inconclusive.")
            case_description7()
        elif option == "suspect4":
            print("suspect4: Security footage shows he was near the warehouse shortly before the fire started.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description7()

def case_description8():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A prominent businessman was found murdered in his penthouse suite. Witnesses reported seeing four individuals entering and leaving the hotel around the time of the murder.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was at the hotel bar with friends.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was attending a conference in the hotel.")
    time.sleep(1)
    print("3. 'suspect3' - Insists he was in his room watching TV.")
    time.sleep(1)
    print("4. 'suspect4' - States she was at a nearby restaurant.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Her friends' stories don't align.")
            case_description8()
        elif option == "suspect2":
            print("suspect2: Conference attendees confirm his presence, but not for the entire time.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect3":
            print("suspect3: Hotel records show he ordered room service, but the timeline is suspicious.")
            case_description8()
        elif option == "suspect4":
            print("suspect4: Restaurant receipts show she left earlier than she claimed.")
            case_description8()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description8()

def case_description9():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("The CEO of a major corporation was found poisoned in his office. Witnesses reported seeing four individuals entering the office building.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was working late in her office.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was at the gym during the incident.")
    time.sleep(1)
    print("3. 'suspect3' - Insists he was having dinner with a client.")
    time.sleep(1)
    print("4. 'suspect4' - States she was at home watching TV.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Security footage shows her leaving the office early.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect2":
            print("suspect2: Gym records show he checked in but left shortly after.")
            case_description9()
        elif option == "suspect3":
            print("suspect3: The client confirms dinner, but not the time.")
            case_description9()
        elif option == "suspect4":
            print("suspect4: Neighbors saw her car leaving the driveway during the incident.")
            case_description9()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description9()

def case_description10():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A well-known DJ was found severely beaten in an alley behind a nightclub. Witnesses saw four individuals entering the alley around the time of the assault.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Claims he was in the club the entire night.")
    time.sleep(1)
    print("2. 'suspect2' - Says she was at a different bar across town.")
    time.sleep(1)
    print("3. 'suspect3' - Insists he was in the VIP section of the club.")
    time.sleep(1)
    print("4. 'suspect4' - States she was outside the club talking on the phone.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Club staff don't recall seeing him all night.")
            case_description10()
        elif option == "suspect2":
            print("suspect2: Her bar receipt shows she left early.")
            case_description10()
        elif option == "suspect3":
            print("suspect3: The VIP section was closed that night.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect4":
            print("suspect4: Phone records show she made no calls during that time.")
            case_description10()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description10()

def main():
    case_solved = False
    print("Hello Sheriff " +name+ "! We need you to investigate some crime cases")
    time.sleep(2)
    crime_cases = ["case1", "case2", "case3", "case4", "case5", "case6", "case7", "case8", "case9", "case10"]
    choice = input()
    while choice not in crime_cases:
        print("Here are the crime cases available case1, case2, case3, case4, case5, case6, case7, case8, case9, or case10")
        time.sleep(1)
        choice = input()
        if choice == "case1":
            case_description1()
        elif choice == "case2":
            case_description2()
        elif choice == "case3":
            case_description3()
        elif choice == "case4":
            case_description4()
        elif choice == "case5":
            case_description5()
        elif choice == "case6":
            case_description6()
        elif choice == "case7":
            case_description7()
        elif choice == "case8":
            case_description8()
        elif choice == "case9":
            case_description9()
        elif choice == "case10":
            case_description10()
        else:
            print("That crime case doesn't exist Sheriff")
if __name__ == "__main__":
    main()