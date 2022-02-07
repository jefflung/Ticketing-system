#ticketing system

age=int(input("Please enter your age:"))

full_price=10

discount_price=1.50

#making decision
if(age<=5):
    ticket_price=discount_price

else:
    ticket_price=full_price

print("Your ticket price is £",ticket_price)