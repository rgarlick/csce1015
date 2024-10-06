# let's go get some software that someone else wrote

import luhn  

# a function that uses the 'luhn' code - it takes a 'card_number' and returns 'true' or 'false' if the card is valid.

def is_credit_card_valid(card_number):    

    return luhn.verify(card_number)

# Let's tell the world whose awful credit card validator this is.

print ("Davesh Yadav Credit Card Validator")

# Let's get the card number from the user

card_number = input("Enter your 16-digit credit card number: ")

# Validate the credit card number using the Luhn algorithm

if is_credit_card_valid(card_number):           # we are calling the function above and sending it the card_number to validate

    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")

def     run_tests():
    
    assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'
    
    assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'
    
    assert not is_credit_card_valid("134"), '134 should not pass but did'
    
    assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'
    
    assert not is_credit_card_valid("000000000000"), 'This is a bad test and we will get an error message'

run_tests() 

