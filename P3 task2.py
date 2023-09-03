def sorting_strings(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("They are Anagrams")
    else:
        print("They aren't Anagrams")    



s1=input("Enter 1st string:")
s2=input("Enter 2nd string:")     
sorting_strings(s1,s2)  