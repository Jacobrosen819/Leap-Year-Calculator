intro = "Welcome to the leap year Calculator\n"
print(intro)
leapyear = True
def leap_year_calc():
  test= input("What year are you checking? ")
  year = int(test)
  if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    prompt = str(year) + " Is a leap year"
    print (prompt)
    return leapyear == True
  else:
    prompt = str(year) + " Isn't a leap year"
    print (prompt)
    return leapyear == True
def leap_year_list():
  leap_years = []
  for i in range(4001):
    if i >= 1752: #this was the 1st leap year in th Gregorian calender
      if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
        leap_years.append(i)
    else:
      pass
  print(leap_years)
  return leap_years

while leapyear:
  question = input("Do you want to know if a year is a leap year(type 'y'), \nor see a list of leap years(type 'l') or exit (type 'e'? ").lower()
  if question == 'y':
    leap_year_calc()
  elif question == 'l':
    leap_year_list()
  else:
    leapyear == False

#leap_year_calc()
#leap_year_list()