import pickle

f = open(r"e:\classroom\ds\mar21\loan\lr_model.pkl","rb")
model = pickle.load(f)

# take input from user
amount = int  (input("Enter Loan Amount         : "))
income = int  (input("Enter Applicant Income    : "))
cincome = int (input("Enter Co.Applicant Income : "))
term  = int   (input("Enter Loan Term           : "))
cr  =   int   (input("Enter Credit History(0/1) : "))

X_test = [[amount,income,cincome,term,cr]]

y = model.predict(X_test)

if  y[0] == 1:
   print("Yessssss")
else:
   print("Noooooooooo")



