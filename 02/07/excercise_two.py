# Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

user = (input("Please enter your name: "))

privileged_user = ["Tadas", "Mantas", "Sausainis"]


if user in privileged_user:
    print(f'Welcome back {user}.')
else:
    print("Welcome otherwis.")