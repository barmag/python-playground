c1 = 'hello world!'
c2 = 'Unique word'

def max_char_length():
    '''
    Get the maximum number of unique characters
    '''
    return abs(ord('A') - ord('z'))

def is_larger_than_charset(word):
    return len(word) > max_char_length()

def dummy_is_unique(word):
    '''
    Brute force implementation O(n squared)
    Can be reduced to O(n log(n)) if string is sorted
    '''
    if is_larger_than_charset(word):
        return False
    currentIndex = 0
    for c in word:
        for i in range(0, len(word)):
            if i != currentIndex and c == word[i]:
                return False
        currentIndex = currentIndex + 1
    return True

def dummy_is_unique_with_sorting(word):
    '''
    O(n log n)
    '''
    if(is_larger_than_charset(word)):
        return False
    
    sorted_word = sorted(word)

    for c in range(0, len(sorted_word)-1):
        if sorted_word[c] == sorted_word[c+1]:
            return False

    return True

assert max_char_length() == 57
assert dummy_is_unique(c1) == False
assert dummy_is_unique(c2) == True

assert dummy_is_unique_with_sorting(c1) == False
assert dummy_is_unique_with_sorting(c2) == True
print("success!")