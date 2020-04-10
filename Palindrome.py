def palindrome(str):
    temp=str
    reverse=str[::-1]
    if(temp==reverse):
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome("malayalam")
