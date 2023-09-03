def Insertion_sort(array):
    for i in range (1,len(array)):
        j=i
        while j>0 and array[j-1]>array[j]:
            array[j-1],array[j]= array[j],array[j-1]
            j=j-1


arr = [12, 11, 13, 5, 6]
Insertion_sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])           