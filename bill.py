def calculate_tip(bill_org, tip_percent):
    tip_amt = bill_org * tip_percent * .01
    return tip_amt

def calculate_bill(bill_org, tip_amt):
    bill_tot = bill_org + tip_amt
    return bill_tot

def calculate_split(bill_tot, num_people):
    cost_each = bill_tot / num_people
    return cost_each


bill_org = float(raw_input("Enter the amount of your bill. "))

tip_percent = int(raw_input("What percentage would you like to tip? "))

split_yn = raw_input("Would you like to split the bill? Yes or no? ")

tip_amt = calculate_tip(bill_org, tip_percent)

bill_tot = calculate_bill(bill_org, tip_amt)


def main(split_yn):
    tip_amt = calculate_tip(bill_org, tip_percent)
    if split_yn == "yes" :
        num_people = int(raw_input("How many ways do you want to split the check?"))
        calculate_bill(bill_org, tip_amt)
        print "Your bill is $%r each." % (calculate_split(bill_tot, num_people))
    else:
        print "Your total bill is $%r." % (calculate_bill(bill_org, tip_amt))


main(split_yn) 

#print calculate_split(bill_total, num_people)
#num_people = int(raw_input("How many ways do you want to split the bill? "))
#tip_amt = calculate_tip(bill_org, tip_percent)
#bill_total = calculate_bill(bill_org, tip_amt)

# def main():
#     if choice == 1:
#         bill_amount = float(raw_input("Enter bill amount. "))
#         tip_percentage = float(raw_input("What percentage would you like to tip? "))
#         tip = calculate_tip(bill_amount, tip_percentage)
#         print "Your tip amount is ", tip_amount
#         calculate_bill(bill_total, tip_amount)
#         print "Your total bill is ", bill_total
#     else:
#         print "else"    
