# simple salary calculator

name = input("Enter employee name: ")

while True:
    try:
        basic_salary = float(input("Enter basic salary: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for the basic salary.")


# allowances
hra = basic_salary * 0.20  # 20% hra
da = basic_salary * 0.10   # 10% da

# deductions
tax = basic_salary * 0.05  # 5% tax
pf = basic_salary * 0.12   # 12% pf

# net salary calculate
net_salary = basic_salary + hra + da - tax - pf

# print salary slip
print("\n--- Salary Slip ---")
print("Name:", name)
print("Basic Salary:", basic_salary)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Tax (5%):", tax)
print("PF (12%):", pf)
print("Net Salary:", net_salary)
print("-------------------")
