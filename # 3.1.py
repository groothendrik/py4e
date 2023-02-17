# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
# The maths on this one was a bit tricky to figure out, but read it a few times before going to the next program. It's vitally important to understand it.
# I tried using hrs = float(input("...")) to use less variables, but no success. I tried switching around, but no success either. I'm sure there's a more elegant way to write this.


hrs = input("Enter Hours:")
h = float(hrs)
rate = input('What is your pay rate?')
r = float(rate)

if h <= 40:
    print(h * r)
    
if h > 40:
    extra_hours = h - 40
    extra_rate  = r * 1.5
    pay = r * 40 + (extra_rate * extra_hours)
    print(pay)