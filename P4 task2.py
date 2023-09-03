def check_balance(x):
    count=0
    for i in x:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        
        if count < 0:
            return False
    return count == 0
x=input()
if check_balance(x):
    print("YES")
else:
    print("NO")