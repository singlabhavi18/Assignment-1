Gross_income = float(input("Enter the gross income: "))
Dependents = int(input("Enter the number of dependents: "))
Standard_deduction = 10000
Dependent_deduction = 3000
Taxable_income = Gross_income - Standard_deduction - (Dependent_deduction * Dependents)
if Taxable_income > 0:
    Tax = (Taxable_income * 20)/100
    print("Your income tax is", Tax)
else:
    print("You're not earning enough to pay tax.")