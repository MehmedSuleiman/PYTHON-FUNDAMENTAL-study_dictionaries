#SoftUni just got a new fancy parking lot.
# It even has online parking validation, except the online service doesn't work.
# It can only receive users' data, but it doesn't know what to do with it.
# Good thing you're on the dev team and know how to fix it, right?
#Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
#The program receives 2 types of commands:
#•	"register {username} {license_plate_number}":
#o	The system only supports one car per user at the moment, so if a user
# tries to register another license plate using the same username, the system should print:
#"ERROR: already registered with plate number {license_plate_number}"
#o	If the check above passes successfully, the user should be registered, so the system should print:
# "{username} registered {license_plate_number} successfully"
#•	"unregister {username}":
#o	If the user is not present in the database, the system should print:
#"ERROR: user {username} not found"
#o	If the check above passes successfully, the system should print:
#"{username} unregistered successfully"
#After you execute all of the commands, print all the
# currently registered users and their license plates in the format:
#•	"{username} => {license_plate_number}"
#Input
#•	First line: n - number of commands - integer
#•	Next n lines: commands in one of the two possible formats:
#o	Register: "register {username} {license_plate_number}"
#o	Unregister: "unregister {username}"
#The input will always be valid, and you do not need to check it explicitly.

n = int(input())

cars= {}

for i in range(n):
    data = input().split()
    if data[0] == "register":
        if data[1] not in cars:
            cars[data[1]] = data[2]
            print(f"{data[1]} registered {data[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {cars[data[1]]}")

    elif data[0] == "unregister":
        if data[1] not in cars:
            print(f"ERROR: user {data[1]} not found")
        else:
            cars.pop(data[1])
            print(f"{data[1]} unregistered successfully")

for key, value in cars.items():
    print(f"{key} => {value}")