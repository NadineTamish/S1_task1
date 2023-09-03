def binary_search(array,start,end,target):
    if start>=end:
        middle=(start+end)//2


        if array[middle]==target:
            return middle
        elif array[middle]>target:
            return binary_search (array,start,middle-1,target)
        else:
            return binary_search(array,middle+1,end,target)
        
    else:
        return False   


    
     
        

