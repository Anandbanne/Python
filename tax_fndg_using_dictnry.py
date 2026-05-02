name=input("Eenter the Eplye name:")
sal=int(input("Enter the Salary:"))
desig=input("Enter the Position:")
d={"TL":10,"Manger":20,"Fresher":5,"Developer":15}
tax=sal*(d[desig]/100)
print(tax)