from itertools import permutations


def permut(string):
    return list(permutations(string)) 


string = input()
print(permut(string))