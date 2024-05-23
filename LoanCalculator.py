'''
Description: This program calculates the time a loan will be paid off, the final payment of the loan,
and the amount of interest overall. This program uses the amount loaned, the annual interest rate,
and the monthly payment for the calculations. If the interest is larger than the payment, the calculator
provides the minimum payment needed to pay off the loan.
'''


loan = 0
interest_rate = 0
payment = 0
months = 0

print("** Welcome to the Consumer Loan Calculator **")
loan = input("How much do you want to borrow? ").replace("$","")
loan = int(loan)
while loan < 1:
  print("You must enter a postive number!")
  loan = input("How much do you want to borrow? ").replace("$","")
  loan = int(loan)

interest_rate = float(input("What is the annual interest rate expressed as a percent? "))
while interest_rate < 1:
  print("You must enter a postive number!")
  interest_rate = float(input("What is the annual interest rate expressed as a percent? "))

payment = input("What is the monthly payment amount? ").replace("$","")
payment = int(payment)
while payment < 1:
  print("You must enter a postive number!")
  payment = input("What is the monthly payment amount? ").replace("$","")
  payment = int(payment)

interest_rate = interest_rate / 1200
interest = loan * interest_rate
sum_interest = interest
loan = loan + interest - payment


    

while loan > 1:
  if interest > payment:
    minimum_payment = interest + 1 
    print(f"You must make payments of at least ${minimum_payment:.2f}")
    print(f"Because your monthly interest is ${interest:.2f} ")
    break
  months += 1
  interest = loan * interest_rate
  loan = loan + interest - payment
  sum_interest += interest
  if loan < 1:
    final_payment = payment + loan
    months += 1
    print(f"Your debt will be paid off after {months} months,",end=" ")
    print(f"with a final payment of just ${final_payment:.2f}")
    print(f"The total amount of interest you will pay during that time is ${sum_interest:.2f}" )

print("** Don't get overwhelmed with debt! **")


'''
Sample Output #1
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $1000
What is the annual interest rate expressed as a percent? 18
What is the monthly payment amount? $50
Your debt will be paid off after 24 months, with a final payment of just $47.83
The total amount of interest you will pay during that time is $197.83
** Don't get overwhelmed with debt! **
'''

'''
Sample Output #2
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? $15000
What is the annual interest rate expressed as a percent? 10
What is the monthly payment amount? $100
You must make payments of at least $126.00
Because your monthly interest is $125.00 
** Don't get overwhelmed with debt! **
'''

'''
Sample Output #3
** Welcome to the Consumer Loan Calculator **
How much do you want to borrow? -$50
You must enter a postive number!
How much do you want to borrow? $-200
You must enter a postive number!
How much do you want to borrow? $20000
What is the annual interest rate expressed as a percent? -2.5
You must enter a postive number!
What is the annual interest rate expressed as a percent? 5
What is the monthly payment amount? $0
You must enter a postive number!
What is the monthly payment amount? $200
Your debt will be paid off after 130 months, with a final payment of just $125.79
The total amount of interest you will pay during that time is $5925.79
** Don't get overwhelmed with debt! **
'''


  
    


  
    





  
