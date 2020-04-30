import pickle

f = open('lr_model.pickle','rb')
model = pickle.load(f)   # unpickle model 

gre = int(input("Enter GRE   : "))
tof = int(input("Enter Toefl : "))
cgpa = float(input("Enter CGPA : "))

result = model.predict([[gre,tof,cgpa]])
print(result[0] * 100)
