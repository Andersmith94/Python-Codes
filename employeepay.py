print("\n" "To calculate your total weekly pay please answer the prompts below." "\n")

Hourly = int(input("What is your hourly pay rate: "))
Time = int(input("What is your total regular hours: "))
OT = int(input("What is your total overtime hours: "))

Regular_pay = Hourly * Time
Overtime_pay = (1.5 * Hourly) * OT
Total_pay = Regular_pay + Overtime_pay

print("\n" "Your total Weekly pay is:", "$" + str(Total_pay))