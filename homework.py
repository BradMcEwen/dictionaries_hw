# ============= Question 1 ===============

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Brushetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 2.59, "Water": 0.00, "Cocktails": 10.99}
for food in ["Main Course"]:
    print(food)


updated_menu = restaurant_menu.copy()
updated_menu["Main Course"]["Steak"] = 17.99
print(updated_menu)

restaurant_menu["Starters"].pop("Brushetta")



for menu, course in restaurant_menu.items():
    print(f" {menu}: ")
    for item, price in course.items():
        print(f" - {item}: {price}")

#=============== Question 2 ===============


def open_new_ticket(tickets, counter):
    print("Your ticket is being created, your ticket number is: " + str(counter) )
    name = input("Please enter your name to assign the ticket to you: ").lower().strip()
    if name.isalpha() == True:
        print("Your name has been stored successfully!")
    else:
        print("Enter a valid name with only letters!!")

    issue = input('Enter a valid issue: ("Login problem, "Payment issue", "Lost Ticket: ")').title().strip()
    if issue == "Login problem" or issue == "Payment issue" or issue == "Lost Ticket":
        print("You have successfully added an issue to your ticket")
    else:
        print("Please enter a valid response!")

    status = input('Enter status: ("open", "closed")').lower()
    if status == "open" or status == "closed":
        print("Your status has been stored successfully!")
    else:
        print("Please enter a valid response")

    tickets[counter] = {"Customers": name, "Issue": issue, "Status": status}


def update_status(tickets):
    print("Lets change the status of your ticket!")
    status = input("Enter your ticket number to update the ticket: ").title()
    if status in tickets:
        if tickets[status]["Status"] == "open":
            tickets[status]["Status"] = "closed"
            print("Your status has been changed!")
        elif tickets[status]["Status"] == "closed":
            tickets[status]["Status"] = "open"
            print("Your status has been changed!")
    else:
        print("That ticket number does not exist.")
    

def display_ticket(tickets):
    display = input('Enter which ticket you would like to view: ("all", "open", "closed")')
    if display == "all":
        print(tickets)

    elif display == "open":
        for key in tickets:
            if tickets[key]["Status"] == "open":
                print(f"Here are the open tickets: {key} {tickets[key]["Customer"]}")
    

    elif display == "closed":
        for key in tickets:
            if tickets[key]["Status"] == "closed":
                print(f"Here are the closed tickets: {key} {tickets[key]["customer"]}")

    else:
        print("You entered an invalid response!")

def track_service_tickets():
    service_tickets = {
        "21": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
        "22": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

    id_ticket_num_counter = 3
    print("Welcome to the Service Tickets App!")


    while True:
        action = input("""Please select an option from the menu:
                       
        Menu:
            "open" = to open a new ticket
            "update" = to update the status of an existing ticket
            "display" = to display all tickets filter by status
            "exit" = to exit the program
            """).lower()
                       
        if action == "open":
            open_new_ticket(service_tickets, str(id_ticket_num_counter))
            id_ticket_num_counter += 1
            print(service_tickets)

        elif action == "update":
            update_status(service_tickets)

        elif action == "display":
            display_ticket(service_tickets)

        elif action == "exit":
            print("Thanks for using the service tickets app. ta-ta!")
            break

        else:
            print("Invalid response!")
    print(service_tickets)
track_service_tickets()