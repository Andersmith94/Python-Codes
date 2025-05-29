#encrypt an input string of lowercase letters and prints the result.
#the other input is the distance value.

plainText = input("Enter Your Message: ")
distance = input("Enter a distance value: ")

if not distance.isdigit() or int(distance) <=0:
    print("Invalid Distance. Please enter a positive number")
else:
    distance = int(distance)
    code = ""

    for ch in plainText:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > 126:
            cipherValue -= 32
        code += chr(cipherValue)

    print("Your secret code is:", code)