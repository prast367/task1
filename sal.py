import  joblib

model = joblib.load('sal.pki')

x = model.predict([[ float(input("Enter experience: ") ) ]] )

print("Salary", x)