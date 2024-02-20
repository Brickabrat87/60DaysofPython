#Create a program that checks if a given string is a valid email address.

email_address = 'brittany.mcnair@cotiviticom'

at_location = []
period_location = []

for i in range(0, len(email_address)):
    if email_address[i] == '@' :
        at_location.append(i)
    elif email_address[i] == '.':
        period_location.append(i)

if len(at_location) == 0 or len(period_location) == 0:
    print("invalid email")
elif max(at_location) > max(period_location):
    print('invalid_email')
elif max(at_location) < max(period_location):
    print('valid_email')


