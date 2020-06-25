from __future__ import print_function
import random
import copy
import smtplib
from email.mime.text import MIMEText

# Function: check lists for collisions
def checkForCollisions(list1, list2):
    """
    Given 2 lists, check to make sure no item in list1
    is in the same index in list2

    Inputs:
    - list1: a 1D list
    - list2: a 1D list

    Returns:
    - True if lists have no collisions
    - False if there is at least one collision
    """
    hasNoCollision = True

    if len(list1) != len(list2):
        print("Error: the lists have different lengths")
        return False

    for i, j in zip(list1, list2):
        if i == j:
            hasNoCollision = False

    return hasNoCollision

# Function: send the emails
def sendSecretSantaAssignments(names, emails, assignments):
    """
    For each name, send them an email with their assigned
    Kris Kringle and the email body text.

    Inputs:
    - names: names of the people
    - emails: email of each person
    - assignments: person each name has for a secret sants

    Returns:
    - None

    Effects:
    - Sends an email to each person in the names list 
    """
    # Start the mail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)

    # Text for email
    openText = "Seasons Greetings, people!\n\n"
    openText += "Since we're not all in the same place this year, we've enlisted the help of technology to pick Kris Kringles for us! "
    openText += "Everyone has been assigned their Kris Kringle via email. Guaranteed no one has themselves. \n\n"

    closeText = "This year, you are allowed to spend $25 on your Kris Kringle's present. Another email will go out asking for each person to suggest "
    closeText += "some items for their Kris Kringle to get for them. \n\n"

    # Check to make sure all lists are same length
    if len(names) != len(emails) or len(names) != len(assignments) or len(emails) != len(assignments):
        print("Error: at least one list has the wrong number of items in it.")
        return False 

    # For each person
    for name, email, kringle in zip(names, emails, assignments):
        # structure the email
        kringleText = name+", your Kris Kringle is: " + kringle+"\n\n"
        subjectText = "Kris Kringle Assignment for " + name

        text = openText+kringleText+closeText+'\n'
        # send the email
        msg = MIMEText(text)
        msg['Subject'] = subjectText
        msg['From'] = myEmail 
        msg['To'] = email

        server.sendmail(myEmail, [email], msg.as_string())



# Function: main
def main():
    # People
    santas = [] # list of people
    secrets = copy.deepcopy(santas)
    emails = [] # list of emails

    noOneHasSelf = False

    while not noOneHasSelf:
        # shuffle secrets
        random.shuffle(secrets)
        # check secrets and santas
        noOneHasSelf = checkForCollisions(santas, secrets)

    # while testing, print
    for santa, secret in zip(santas, secrets):
        with open("Kringle-"+santa+'.txt', "w+") as f:
            f.write(santa+" has "+ secret+ " as a Kris Kringle.\n")
    # send out emails
    sendSecretSantaAssignments(santas, emails, secrets)

if __name__ == "__main__":
    main()
