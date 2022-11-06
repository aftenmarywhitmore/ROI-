class ROI_calculator():
    def __init__(self, value):
        self.value = {}

    def income(self):
        rental_income = int(input("Enter monthly rental income:"))
        self.value["rental income"] = rental_income
        laundry = int(input("Enter monthly laundry:"))
        self.value["laundry"] = laundry
        storage = int(input("Enter monthly storage:"))
        self.value["storage"] = storage
        misc = int(input("Enter other monthly income:"))
        self.value["misc"] = misc
    
        total_income = rental_income + laundry + storage + misc
        print(f"Total Income: {total_income}")
        

    def expenses(self):
        tax = int(input("Enter monthly taxes:"))
        self.value["tax"] = tax
        insurance = int(input("Enter monthly insurance cost:"))
        self.value["insurance"] = insurance
        utilities = int(input("Enter monthly utility costs:"))
        self.value["utilities"] = utilities
        HOA = int(input("Enter monthly HOA fee amount:"))
        self.value["HOA"] = HOA
        lawn_care = int(input("Enter monthly lawn care costs:"))
        self.value["lawn care"] = lawn_care
        vacancy = int(input("Enter monthly vacancy costs:"))
        self.value["vacancy"] = vacancy 
        repairs = int(input("Enter approximate monthly repairs cost:"))
        self.value["repairs"] = repairs
        cap_ex = int(input("Enter monthly capital expenditures cost:"))
        self.value["capital expenditures"] = cap_ex
        prop_mgmt = int(input("Enter monthly property management costs:"))
        self.value["property management"] = prop_mgmt
        mortgage = int(input("Enter monthly mortgage amount:"))
        self.value["mortgage"] = mortgage

        total_expenses = tax + insurance + utilities + HOA + lawn_care + vacancy + repairs + cap_ex + prop_mgmt + mortgage
        print(f"Total Expenses: {total_expenses}")

    def cash_flow(self):
        total_income = int(input("Enter total income:"))
        self.value["total income"] = total_income
        total_expenses = int(input("Enter total expenses:"))
        self.value["total expenses"] = total_expenses

        total_cash_flow = total_income + total_expenses 
        print(f"Total Cash Flow: {total_cash_flow}")

    def investment(self):
        down_pmt = int(input("Enter down payment amount:"))
        self.value["down payment"] = down_pmt
        closing = int(input("Enter closing costs:"))
        self.value["closing costs"] = closing
        rehab = int(input("Enter rehab budget:"))
        self.value["rehab budget"] = rehab
        other = int(input("Enter other miscellaneous costs:"))
        self.value["miscellaneous/other"] = other

        total_investment = down_pmt + closing + rehab + other
        print(f"Total Investment: {total_investment}")

    def ROI(self): 
        cash_flow = int(input("Enter cash flow:"))
        self.value["total cash flow"] = cash_flow
        tot_inv = int(input("Enter total investment:"))
        self.value["total investments"] = tot_inv

        total_ROI = cash_flow / tot_inv
        print(f"Total Return on Investment: {total_ROI}")
       
def findReturnOnInvestment():
    roi = ROI_calculator({})
    
    print("Welcome to the Return On Investment (ROI) calculator. Please follow these steps to calculate the ROI on any property!")
    print("\n")
    roi.income()
    print("\n")
    roi.expenses()
    print("\n")
    roi.cash_flow()
    print("\n")
    roi.investment()
    print("\n")
    roi.ROI()
    
    while True:
        response = input("\nWould you like to find the ROI on another property? (Enter 'yes' to continue, or 'no' to quit) ")
        
        if response.lower() == 'yes':
            ROI_calculator()
            break
            
        elif response.lower() == 'no':
            print("I'm Aften Whitmore and I hope your day is an Af10 out of 10! Peace.")
            break
        
        else:
            response
            print('Type a valid command.')
            

findReturnOnInvestment()
    