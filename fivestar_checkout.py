#New costs $3, Classic costs $2, Vinyl costs $1.5, Games cost $4.

print("\n" "To calculate the tab please answer the following prompts." "\n")

New = int(input("Enter the number of New DVDs to rent: "))
Classic = int(input("Enter the number of Classic DVDs: "))
Vinyl = int(input("Enter the number of Vinyl Records: "))
Games = int(input("Enter the number of Video Games: "))
Nights = int(input("Enter the number of Nights Renting: "))

New_Cost = New * 3
Classic_Cost = Classic * 2
Vinyl_Cost = Vinyl * 1.5
Games_Cost = Games * 4

Total = (New_Cost + Classic_Cost + Vinyl_Cost + Games_Cost) * Nights

print("\n" "The total price is:", "$" + str(Total))