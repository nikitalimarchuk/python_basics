proceeds = int(input("Enter company proceeds: "))
costs = int(input("Enter company costs: "))

difference = proceeds - costs

if difference < 0:
    print(f"Company is lesionable - costs more then proceeds")
else:
    print("Company is profitable - proceeds more then costs")
    print(
        f"Profitability of proceeds is: "
        f"{difference} / {proceeds} = {difference / proceeds}"
    )
    employees = int(input("Enter number of employees: "))
    print(
        f"Profit per each employee is: "
          f"{difference} / {employees} = {difference / employees}"
    )
