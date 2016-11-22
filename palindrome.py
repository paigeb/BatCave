word_to_check = input("Please enter your favorite word > ")

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
