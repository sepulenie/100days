import os

print ('Current path - ', os.getcwd())
b = "/usr/"
print("Changing path...")
os.chdir(b)
print (os.getcwd())

print("Currnet user - ", os.getlogin())
print(os.getcwdu())