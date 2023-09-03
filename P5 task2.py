def list_numbers(arary,target):
    list={}
    for i in arary:
        diff=target-i
        if diff in list and list[diff]>0:
            result = (i, diff)
            return result
        if i in list:
            list[i] += 1
        else:
           list[i] = 1
    return False

array=input()
x=input()
