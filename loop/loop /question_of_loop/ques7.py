#Example 8: Python program to check if the given string is a palindrome.
given_string=str(input("Enter the string:"))
reverse_string=""
for i in given_string:
    reverse_string=i+reverse_string
if(reverse_string == given_string):
    print("palindrome") 
else:
    print("Not a palindrome")   