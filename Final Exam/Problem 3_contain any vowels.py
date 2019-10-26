Problem 3
10/10 points (graded)
Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. If s = "a" then print_without_vowels will print the empty string

def print_without_vowels(s):
    new = ""
    for i in range(0, len(s)):
        if s[i].lower() == 'a' or s[i].lower() == 'e' or s[i].lower() == 'i' or s[i].lower() == 'o' or s[i].lower() == 'u':
            new += ""
        else:
            new += s[i]
    print(new)
print_without_vowels("This is great!")
