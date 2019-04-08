def isAnagram(s1,s2):
    str1 = s1.replace(" ", "")
    str2 = s2.replace(" ", "")
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    if (str1 == str2):
        return True

    return False

s1 = raw_input("Enter the first word: ")
s2 = raw_input("Enter the second word: ")

if (isAnagram(s1, s2)):
    print("Yes they are anagrams!")
else:
    print("Nope fuck you")

