# Minh Tri Doan Vo
# CSC 110
# 11/22/2023

def main():
    custData = "1053l6#Lopez,  Lupe Luisa #(206)555-1845#$1,346.75"
    custData = custData.split("#")
    customerNumber         = fixCustNum(custData[0])
    lastName, firstName    = fixCustName(custData[1])
    areaCode, phoneNumber  = fixCustPhone(custData[2])
    customerBalance        = fixCustBalance(custData[3])
    print("Customer number\t:",   customerNumber)
    print("Customer last name\t:",  lastName)
    print("Customer first name\t:", firstName)
    print("Customer area code\t:", areaCode)
    print("Customer phone\t\t:", phoneNumber)
    print("Customer balance\t:", customerBalance)

def fixCustNum(custNum):
    if "l" in custNum:
        custNum = custNum.replace("l", "1")
    elif "O" in custNum:
        custNum = custNum.replace("O", "0")
    return int(custNum)

def fixCustName(custName):
    custName      = custName.strip().replace("  ", " ")
    commaPosition = custName.find(",")
    lastName      = custName[: commaPosition]
    firstName     = custName[commaPosition + 2:]
    return lastName, firstName

def fixCustPhone(custPhone):
    custPhone = custPhone.strip().replace("(", "")\
                .replace(")", " "). replace("-", "")
    aCode     = custPhone[:4]
    phoneNum  = custPhone[5:]
    return aCode, phoneNum

def fixCustBalance(custBalance):
    custBalance = custBalance.replace("$", "").replace(",", "")
    if custBalance == "":
        custBalance = 0.0
    return custBalance

main()