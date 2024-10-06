# Credit Card Validator version .1
# This is the world's worst credit card number validator. It checks to see if the number is 16 digits long and that is it.  

# anything that starts with a pound sign (hashtag if you are under 30) is a comment. The computer ignores these.

# Let's tell the world whose awful credit card validator this is.
print ("Caleb Polley Modified This Credit Card Validator")

# Let's get the card number from the user
card_number = input("Enter your 16-digit credit card number: ")

# Check if card number is 16 digits long

# len means 'length', and the '==' is testing one thing against the other. A single equal sign would set one thing equal to the other (not what we want to do). 
# card_number.isdigit() is checking if this is numbers instead of someone typing 'cheeseburger' for their credit card number.

if len(card_number) == 16 and card_number.isdigit():     
    print ("Card is valid.")
    card_number = input("Type 'enter'e to finish")
else:
    print ("Invalid card number. It must be 16 digits long.") 
    card_number = input("Type 'enter' to finish")

def run_tests():

    assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'

    assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'

    assert not is_credit_card_valid("134"), '134 should not pass but did'

    assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'

    assert not is_credit_card_valid("000000000000"), 'This is a bad test and we will get an error message'

run_tests() 

