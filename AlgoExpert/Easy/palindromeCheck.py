# def isPalindrome(string):
#     reversedString = ""
#     for str in reversed(string):
#         reversedString += str
#     return reversedString == string


# def isPalindrome(string):
#     reversedChars = []
#     for str in reversed(string):
#         reversedChars.append(str)
#     return "".join(reversedChars) == string

# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)

def isPalindrome(string):
    leftidx = 0
    rightIdx = len(string) - 1
    while leftidx < rightIdx:
        if string[leftidx] != string[rightIdx]:
            return False
        leftidx += 1
        rightIdx -= 1

    return True


print(isPalindrome("abbma"))
