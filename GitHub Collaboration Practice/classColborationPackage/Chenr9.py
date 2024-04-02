#Name:Ruolin Chen
#email:chenr9@mail.uc.edu
#Assignment Title: 
#Course: IS 4010
#Semester/Year: Spring 2024
#Brief Description: 
#Citations:
#Anything else that's relevant: 


def romanToInt(s: str) -> int:
    roman_to_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0
    for char in s:
        value = roman_to_int_dict[char]
        result += value
        if value > prev_value:
            result -= 2 * prev_value
        prev_value = value
    return result

# Example usage
s = "III"
print(romanToInt(s))  # Output: 3





