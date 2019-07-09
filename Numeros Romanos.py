#Roman Numbers

from collections import OrderedDict

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for v in roman.keys():
            x, y = divmod(num, v)
            yield roman[v] * x
            num -= (v * x)
            if num <= 0:
                break
            
    return "".join([a for a in roman_num(num)])
while True:
    num = int(input("What number do you want to convert? "))
    if num == 0:
        print ("----------------------------------------")
        print("0 Does not exist in roman numerals")
    print ("----------------------------------------")
    print (write_roman(num))
    print ("----------------------------------------")
  
