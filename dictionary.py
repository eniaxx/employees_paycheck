#thislist = ["apple", "banana", "cherry"]
#tropical = ["mango", "pineapple", "kiwi", "papaya"]
#thislist.extend(tropical)
#print("\n", str(thislist), "\n")

#x = thislist.__len__()
    
#for i in range(0, thislist.__len__()):
#    print(thislist[i])

from asyncio.windows_events import NULL
import pandas as pd

dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

employee = {'E01' : dictionary, 'E02' : dictionary, '03' : dictionary, '04' : dictionary, '05' : NULL, '06' : NULL}

d = [ ["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]

df = pd.DataFrame(employee) #, columns = ['','Age','Percent'])
print(df)

#print(d)