#Function to check if input is a Palindrome

def checkPalindrome(inputString):

    if len(inputString) % 2 == 0:
        center = len(inputString)/2
        left = inputString[0:center]
        right = inputString[center:len(inputString)]
        rightrev = ''.join(reversed(right))
        print left
        print rightrev
        if left == rightrev:
            return True
        else:
            return False

    if len(inputString) % 2 == 1:
        leftcenter = (len(inputString)-1)/2
        rightcenter = (len(inputString)+1)/2
        left = inputString[0:leftcenter]
        right = inputString[rightcenter:len(inputString)]
        rightrev = ''.join(reversed(right))
        print left
        print rightrev
        if left == rightrev:
            return True
        else:
            return False
    

inputString = "aaaaaaaa"

print checkPalindrome(inputString)