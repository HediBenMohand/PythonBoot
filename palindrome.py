def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "lamif"
x = isPalindrome(s)
 
if x:
    print("n'est pas un palindrome")
else:
    print("est un palindrome")