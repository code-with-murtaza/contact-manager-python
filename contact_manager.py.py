# Contact Manager (Python Project)
# --------------------------------
# Description:
# A Python-based contact management system that allows users to store,
# search, and manage contacts using a simple menu-driven interface.

# Author: Syed Murtaza

contacts = []   # this will store all contacts


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    print("✅ Contact added successfully!\n")


def show_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return

    print("📒 Contact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    print()


def search_contact():
    search_name = input("Enter name to search: ")

    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"🔍 Found: Name: {contact['name']}, Phone: {contact['phone']}\n")
            found = True
            break

    if not found:
        print("❌ Contact not found.\n")


while True:
    print("=== Contact Manager ===")
    print("1. Add Contact")
    print("2. Show All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("👋 Exiting Contact Manager. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.\n")
