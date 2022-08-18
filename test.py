#thislist = ["apple", "banana", "cherry"]
#tropical = ["mango", "pineapple", "kiwi", "papaya"]
#thislist.extend(tropical)
#print("\n", str(thislist), "\n")

#x = thislist.__len__()
    
#for i in range(0, thislist.__len__()):
#    print(thislist[i])

import pandas as pd

d = [ ["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]

df = pd.DataFrame(d, columns = ['Name','Age','Percent'])
print(df)