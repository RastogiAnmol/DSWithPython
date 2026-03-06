def isPalindrome(s: str) -> bool:
    return s == s[::-1]

def validPalindrome(s: str) -> bool:
    for i in range(len(s)):
        string = s[0:i] + s[i+1:]
        if isPalindrome(string):
            return True
    return False

print(validPalindrome("abaabac"))