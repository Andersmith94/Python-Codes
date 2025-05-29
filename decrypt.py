#decrypt

code = input("Enter the coded message: ")
distance = input("Enter the distance: ")

if not distance.isdigit() or int(distance) <=0:
    print("Invalid Distance. Please enter a positive number")
else:
    distance = int(distance)
    plainText = ""

    for ch in code:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue < 32:
            plainText = 126
        plainText += chr(cipherValue)
    print("Your decoded message is:", plainText)