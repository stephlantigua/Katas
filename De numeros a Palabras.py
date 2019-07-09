#Numerals to words

def int_to_en(num):
    s = { 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', \
          14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', \
          70:'seventy', 80:'eighty', 90:'ninety' }
    f = 1000
    g = f * 1000

    if (num < 20):
        return s[num]

    if (num < 100):
        if num % 10 == 0:
            return s[num]
        else:
            return s[num // 10 * 10] + ' ' + s[num % 10]

    if (num < f):
        if num % 100 == 0:
            return s[num // 100] + ' hundred'
        else:
            return s[num // 100] + ' hundred ' + int_to_en(num % 100)

    if (num < g):
        if num % f == 0:
            return int_to_en(num // f) + ' thousand'
        else:
            return int_to_en(num // f) + ' thousand ' + int_to_en(num % f)

while True:
    num = int(input("-Please enter an integer between 1 and 9999: "))
    print("------------------------------------------------")
    print("-", int_to_en(num))
    print("------------------------------------------------")
    
