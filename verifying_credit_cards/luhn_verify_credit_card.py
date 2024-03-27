import re

def get_credit_number():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        user_input = input("Enter your 16-digit credit card number (without spaces): ")
        masked_number = "*" * len(user_input)  # Create a string with asterisks

        # Input format check using a regular expression:
        if re.match(r"^[\d-]{19}$", user_input):  # Validate 16 digits and 3 hyphens
            return user_input.replace("-", "")  # Remove hyphens for validation
        
        else:
            attempts += 1
            print(f"""Invalid format. Please enter only digits and hyphens. 
                  Your input appears as: {masked_number}""")
            if attempts < max_attempts:
                print(f"You have {max_attempts - attempts} attempts remaining.")
                
    # Too many invalid attempts:
    print("Maximum attempts reached.")
    return ""  # Return an empty string to indicate failure

    

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit)* 2
        if number >= 10:
            number = (number// 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():
    card_number = get_credit_number()
    translated_card_number = str(card_number).translate(card_number)

    if verify_card_number(translated_card_number):
        print('The credit card number is VALID.')
    else:
        print('The credit card number is INVALID.')


if __name__ == '__main__':
    main()