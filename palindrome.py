def isPalindrome(s):
    l = len(s)
    for i in xrange(l/2):
        if (s[i] != s[l-i-1]):
            return False
    
    return True

str = raw_input("Enter a string to see if it's a palindrome: ")

if (isPalindrome(str)):
    print("I'm a palindrome!")
else:
    print("Nope!")
