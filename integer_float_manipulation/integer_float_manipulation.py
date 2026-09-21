#1.creating six variables for storing different values

gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = 400.5
salary_tax = 0.2 #20%
donation = 0.1 #10%

#2.calculating net salary after the expenses
#the tax is calculated on gross salary in real world ,its on same principle

tax = gross_salary*salary_tax #tax variable for storing calculated taxed money on gross salary
net_salary = gross_salary-tax #subtracting tax from gross salary to get net salary
net_salary = net_salary-health_insurance-rent-food #subtracting fixed expenses from the net salary
donate = net_salary*donation #calculating 10% donation on net salary
net_salary = net_salary-donate #subtracting donation from net salary

#printing remaining  net salary after the expenses  upto desired decimal

print(f"Net salary : ",net_salary)
print(f"Net salary :",f"{net_salary:.3f}") #up to 3 decimal


#amount of money given in donation

print(f"Donation given to poor :",donate)
print(f"Donation given to poor :",f"{donate:.2f}")#up to 2 decimal
