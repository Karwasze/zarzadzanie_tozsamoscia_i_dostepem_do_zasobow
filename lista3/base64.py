#!/usr/bin/env python3

def string_to_char_codes(string):
    char_codes = []
    for char in string:
        char_codes.append(ord(char))
    return char_codes

def char_codes_to_binary_repr(char_codes):
    binary_repr = []
    for char_code in char_codes:
        binary_repr.append('{0:08b}'.format(char_code))
    return binary_repr

def merge_list_to_string(input):
    return ''.join(input)

def split_into_sextets(binary_repr):
    sextets = [binary_repr[x:x+6] for x in range(0,len(binary_repr),6)]
    sextets[-1] = sextets[-1].ljust(6, '0')
    return sextets

def convert_sextets_into_chars(sextets):
    CHAR_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    chars = []
    for sextet in sextets:
        chars.append(CHAR_TABLE[int(sextet,2)])
    return chars

def add_padding(string):
    if len(string) % 4 == 1:
        return string + ("=")
    elif len(string) % 4 == 2:
        return string + ("==")
    elif len(string) % 4 == 3:
        return string + ("=")
    else:
        return string

def base64(input):
    char_codes = string_to_char_codes(input)
    binary_repr = char_codes_to_binary_repr(char_codes)
    merged_binary_repr = merge_list_to_string(binary_repr)
    sextets = split_into_sextets(merged_binary_repr)
    chars = convert_sextets_into_chars(sextets)
    merged_chars = merge_list_to_string(chars)
    result = add_padding(merged_chars)
    return result
    
        

print(base64("Many hands make light work."))
print(base64("Man"))
print(base64("Ma"))
print(base64("M"))
print(base64("light work."))
print(base64("light work"))
print(base64("light wor"))
print(base64("light wo."))
print(base64("light w"))
