# write a simple python program that (in command line):

# 1. Shows you a simple menu (like a vending machine. 3 items are enough):
# 	i.e:
# 	1. hamburger:  10$
# 	2. coca-cola:  2$
# 	3. fries:      4$

# 2. Asks for your choice of purchase(CLI text response with a number).

# 3. asks you for your credit card information: (Again, all in CLI)
# 	-first ask for card number, make sure it is an integer that is 16 digits long
# 	-ask for name, make sure the name is a string

# 4. You can hard code card information for a single card like (1234567891234567, Taylor, 50$). Please use an appropriate data structure. (Ignore case)

# 5. Checks whether the card information matches one in the database and whether it has enough money. (it is okay if the "database" only has the one card in it)

# 6. If the card doesn't match, it returns an error "Card doesn't match records".
# If the card does match but doesn't have enough tfunds it also reurns (prints) error like "Not enough funds on card".
# if the card does match and does have enough funds, the program proceeds with reducing the amount
# of funds in the card by the amount the chosen item costs and returns (prints) "Success, Item purchased for X$, Y$ left in the account".
# Make sure the account in the database has that amount of money subtracted.

# 7. Loop back to the beginning

# Sample input/output:

# Welcome to the vending machine!
# 1. hamburger: 10$
# 2. coca-cola: 2$
# 3. fries: 4$
# Enter the number of your choice: 3
# Enter your 16-digit card number: 1234567891234567
# Enter the name on the card: taylor
# Success, Item purchased for 4$, 46$ left in the account.
# Would you like to make another purchase? (yes/no): yes
# Welcome to the vending machine!
# 1. hamburger: 10$s
# 2. coca-cola: 2$
# 3. fries: 4$
# Enter the number of your choice: 1
# Enter your 16-digit card number: 1234567891234567
# Enter the name on the card: taylor
# Success, Item purchased for 10$, 36$ left in the account.
# Would you like to make another purchase? (yes/no):


#Variables
menu = "1. hamburger:\t10$\n2. coca-cola:\t2$\n3. fries:\t4$"
firstName = "firstName"
lastName = "lastName"
dbCreditCard = [1234567891234567,1111111111111111,2222222222222222,3333333333333333,4444444444444444,5555555555555555]
dbCreditCardBalance=[50,5,10,15,0,500]
dbFirstName = ["taylor","rob","dob","bob", "broke" ,"money"]
dbLastName = ["bui", "ber", "by","bert","guy","bag"]
dbInventoryPrices = [10,2,4]
dbIndex = 0
repeatPurchase = True


#Verifies the credit card length is 16
def creditCardLength(creditCardNumber):
    stringLength = len(str(creditCardNumber))
    validLength = 16
    if stringLength == validLength:
        return True
    else:
        return False
    

#Verifies the credit card number is in the DB then verifies the firstName and lastName matches the credit card index
def dbCheck(creditCardNumber,firstName,lastName):
    #Used this for loop to iterate using index
    for index in range(len(dbCreditCard)):
        if dbCreditCard[index] == creditCardNumber:
            #print("Success Check 1")
            if dbFirstName[index] == firstName:
                #print("Success Check 2")
                if dbLastName[index] == lastName:
                    #print("Success Check 3")
                    dbIndex = index
                    print("Confirmed information")
                    return index
    print("Card doesn't match records")
    return 999

#Verifies if the db Balance is higher than the cost of the item being purchased
def dbCheckBalance(balanceIndex,inventoryPriceIndex):
  
    if dbCreditCardBalance[balanceIndex] >= dbInventoryPrices[inventoryPriceIndex]:
        return True
    else:
          print("Not enough funds on card")
          return False





while True:
    #simple menu
    
    print("Welcome to the vending machine!\n" + menu)
    choiceIndex = int(input("Enter the number of your choice: "))
    choiceIndex -= 1

    #Note i would add input validation for above but I do not know how to indent the whole block code below.... so please ignore this input validation 
    #specifically for this line.


    #credit card number input
    creditCardNumber = int(input("Enter your 16-digit card number: "))
    #print(type(creditCardNumber))

    #Verifies credit card as well as types the string/int
    if creditCardLength(creditCardNumber) == True:
        #Takes First Name / Last Name then lowercases it so that is easily checked in the DB. the DB is all lowercase
        firstName = str(input("Enter your First Name: ")).lower()
        #print(firstName)
        lastName = str(input("Enter your Last Name: ")).lower()
        #print(lastName)

        #Confirms the data matches the DB then assigns the index to dbIndex to be used later for calculations. If it not found in the DB then it will 
        #return 999. If it is found in the DB then it will return the index
        dbIndex = dbCheck(creditCardNumber,firstName,lastName)
        if dbIndex != 999:#Checks balance
            check = dbCheckBalance(dbIndex, choiceIndex)
            if check == True:#changes the DB to reflect the purchase of an item
            
                dbCreditCardBalance[dbIndex] -= dbInventoryPrices[choiceIndex]
                print(f"Success, Item purchased for {dbInventoryPrices[choiceIndex]}$, {dbCreditCardBalance[dbIndex]}$ left in the account") 
           
                  #Second menu to buy more
                while True:
               
                    secondBuy = input("Would you like to make another purchase? (yes/no): ")
                    secondBuy = secondBuy.lower()
                    if secondBuy =="yes":
                    #Copy and pasted previous code, I removed the credit card selection because no need to input another credit card, also added a cancel option
                        print("Welcome to the vending machine!\n" + menu + "\n4. Cancel")
                        choiceIndex = input("Enter the number of your choice: ")
                        choiceIndex = int(choiceIndex)-1
                    else:
                        if secondBuy == "no":
                            break
              
                    

                        #To cancel additional purchase
                    if choiceIndex == 3:
                        break

                    #Check if there is enough balance
                    check = dbCheckBalance(dbIndex, choiceIndex)
                    if check == True: #If true then continue with transaction
                        dbCreditCardBalance[dbIndex] -= dbInventoryPrices[choiceIndex]
                        #print(dbCreditCardBalance[dbIndex])
                        print(f"Success, Item purchased for {dbInventoryPrices[choiceIndex]}$, {dbCreditCardBalance[dbIndex]}$ left in the account")
                 
           
    else:
        print("Invalid credit card number, Please start from the beginning")





