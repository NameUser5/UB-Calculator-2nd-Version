title = "The UNBREAKABLE Calculator Ver. 2:"
title = title.upper()

print(title)

print("\nWelcome! Feast your eyes upon our newly improved wonder, the Calcu-maton 5000! Enter two numbers below and prepare to be amazed!~ \n")

start = str(input("Do you want to use the Calcu-maton 5000? \n <YES>    <NO> \n")).upper()
if start == "YES":
  num1_ask = True
#   calc_run = True
  while num1_ask == True:
    # num1 = ""
    try:
      num1 = float(input("Enter your first number: ")) 
      valid_num1 = True
    except ValueError:
      print("Nice try, fellow.")
      valid_num1 = False
    if valid_num1 == True:
      num1_ask = False
      calc_run = True
else:
    num1_ask = False
    calc_run = False
    num2_ask = False

    print("Goodbye.")



# num1 = ()

# for n in num1:
#     if num1_ask == True:
#     # num1 = ""
#         try:
#           num1 = float(input("Enter your first number: ")) 
#           valid_num1 = True
#           if valid_num1 == True:
#             calc_run = True
#         except ValueError:
#           print("Nice try, fellow.")
#           valid_num1 = False



while calc_run == True:

  operations = ["+","-","*","/"]

  def add(num1,num2):
    total = num1 + num2
    return total
  def subtract(num1,num2):
    total = num1 - num2
    return total
  def multiply(num1,num2):
    total = num1 * num2
    return total
  def divide(num1,num2):
    total = num1 / num2
    return total
  
  while calc_run == True:
    operation = str(input("Enter your operation: "))
    '''operations = ["+","-","*","/"]'''
    for o in operations:
      if operation in operations:
        valid_opp = True
        num2_ask = True
      else:
        valid_opp = False

      while valid_opp == False:
        operation = str(input("Try again. Enter an appropriate symbol. "))
        
        if operation in operations:
          valid_opp = True
          num2_ask = True
  
              #   while num2_ask == True:
          if num2_ask == True:
            try:
              num2 = float(input("Enter your second number: ")) 
              valid_num2 = True
              num2_ask = False
            except ValueError:
              print("Egads! What are you doing? Try again.")
              valid_num2 = False
              while valid_num2 == False:
                  
                  try:
                    num2 = float(input("Enter your second number: ")) 
                    valid_num2 = True
                    num2_ask = False
                  except ValueError:
                    print("Egads! What are you doing? Try again.")
                    valid_num2 = False
                    continue
    
#   get_result = True

            for o in operations:
              if operation == "+":
                result = add(num1,num2)
              elif operation == "-":
                result = subtract(num1,num2)
              elif operation == "*":
                result = multiply(num1,num2)
              elif operation == "/":
                if num2 != 0:
                  result = divide(num1,num2)
                else: 
                  result = "Undefined. You cannot divide by zero"
          print(f"\nYour total is: {result}.\n")
          keep_play = str(input("Do you want to continue using the Calcu-maton 5000? \n <YES>    <NO> \n")).upper()
          if keep_play == "YES":
            calc1_run = True
            num1 = result
          else:
            calc_run = False
        continue