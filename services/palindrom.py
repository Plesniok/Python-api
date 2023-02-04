def is_palindrom(word):
    idx = 0
    while idx <= len(word) - idx - 1 - (len(word)//2):
        if word[idx] != word[len(word) - idx - 1]:
            return False
        idx += 1
    return True    

