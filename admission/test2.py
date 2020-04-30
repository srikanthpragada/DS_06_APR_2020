import pandas as pd

model = pd.read_pickle("lr_model.pickle")   # unpickle model 

gre = int(input("Enter GRE   : "))
tof = int(input("Enter Toefl : "))
cgpa = float(input("Enter CGPA : "))

result = model.predict([[gre,tof,cgpa]])
print(result[0] * 100)
