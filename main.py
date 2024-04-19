import whois
import time
import os
import csv
from datetime import datetime

# Welcome message for the user.
welcome_message = "Welcome to GoDomainChecker!\n\nFind your perfect domain name instantly. Check availability by typing or importing from a text file.\n\nLet's get started!\n"

# Menu options presented to the user.
menu_options = "\nGoDomainChecker Menu:\n\n1. Check availability of a single domain\n\n2. Check domains from the 'listdomainshere.txt' text file\n\n3. Exit\n"

# Display the welcome message and menu options.
print(welcome_message + menu_options)

# Prompt the user to choose an option.
utype = int(input("Please enter the number corresponding to your choice: "))

# Generate a unique filename for each CSV file.
filename = datetime.now().microsecond
csvfilename = f"Domain Status Data {filename}.csv"

# Define the headers for the CSV file.
csv_headers = ["Domain Name", "Status"]

# Create a new CSV file if it doesn't exist and write the headers.
if not os.path.exists(csvfilename):
    with open(csvfilename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_headers)

# Function to check the availability of a domain.
def CheckDomain(askonedomain):
    try:
        whoischeck = whois.whois(askonedomain)
        if whoischeck is None:
            return True  # Domain is available.
        else:
            return False  # Domain is unavailable.
    except Exception as e:
        return True  # Domain is available.

# Handle user input based on their choice.
if utype == 1:
    print("You selected option 1: Check availability of a single domain")
    askonedomain = input("Please enter your domain name here: ")
    if CheckDomain(askonedomain):
        print(f"{askonedomain} is available!")
        with open(csvfilename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([askonedomain, "Available"])
    else:
        print(f"{askonedomain} is unavailable!")
        with open(csvfilename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([askonedomain, "Unavailable"])
elif utype == 2:
    print("You selected option 2: Check domains from the 'listdomainshere.txt' text file")
    if os.path.exists("listdomainshere.txt"):
        print("File found!")
        domainfilepath = "listdomainshere.txt"
        with open(domainfilepath, "r") as file:
            for line in file:
                linedomain = line.strip()
                if CheckDomain(linedomain):
                    print(f"{linedomain} is available!")
                    with open(csvfilename, "a", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([linedomain, "Available"])
                else:
                    print(f"{linedomain} is unavailable!")
                    with open(csvfilename, "a", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([linedomain, "Unavailable"])
    else:
        print("The text file doesn't exist, so we created it. Please input the domain names.")
        with open("listdomainshere.txt", "w") as f:
            pass
elif utype == 3:
    print("Exiting GoDomainChecker. Goodbye!")
    time.sleep(3)
    exit()
else:
    print("Invalid choice. Please enter a valid option (1, 2, or 3).")