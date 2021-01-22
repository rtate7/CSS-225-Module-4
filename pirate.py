# Edited for debugging by Robert Tate on 1/22/21
#
# Asks a user for their password and tells the to go away
# if they provide the pirate password "Arrr!"

greeting = input("Hello, possible pirate! What's the password? ")
if greeting == "Arrr!":
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
