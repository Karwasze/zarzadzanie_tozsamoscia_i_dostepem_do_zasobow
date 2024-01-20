#!/usr/bin/env python3
import random

def generate_password():
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    SPECIAL_CHARS = "!@#$%^&*[]+=-"
    result_table = []
    for i in range(32):
        """
        Minimizing the chance of occurence of a dictionary word.
        the password should contain about 50% of letters, 20% of numbers 
        and 30% of special characters.
        """
        chosen_list = random.randint(0,10)
        if chosen_list >= 0 and chosen_list < 6:
            result_table.append(random.choice(LETTERS))
        elif chosen_list >= 6 and chosen_list < 8:
            result_table.append(random.choice(NUMBERS))    
        else:
            result_table.append(random.choice(SPECIAL_CHARS))
    return ''.join(result_table)

print(generate_password())
    
