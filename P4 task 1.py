number=input() #as characters
x=len(number)
revnumber=reversed(number)
if x<15 or x>16 :
    print("INVALID")
else:
    sum=0
    second_digit=False
    for digit in revnumber: # conver the revnumber to digits??
        digit=int(digit) 
        if second_digit ==True:
            digit*=2
            digit=digit // 10+ digit %10
        sum+=digit
        second_digit= False  
        
    if sum%10==0:
        if number[0:1]=='4':
            print("Visa")
        elif number[0:2] in ['51', '52', '53', '54', '55']:
            print("MasterCard")
        elif number[0:2] in ['34','37']:
            print("American Express")
        else:
            print("UNKNOWN CARD")    

        