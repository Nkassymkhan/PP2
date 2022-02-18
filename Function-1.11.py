def palindrome(string):
    if list(reversed(string)) == list(string):
        return True
    else: 
        return False

string = input()
print(palindrome(string))