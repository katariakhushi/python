''''
Welcome to Rich Hard.....

'''
import os
import pickle
class Customer:#customers blueprint
    id=0
    company=''
    modelno=0
    name=''
    def getAutoId(self):#generateid
        autoid=1
        file=open('customer.dat','rb')
        while True:
            try:
                customer=pickle.load(file)
                autoid=customer.id
            except EOFError:
                break
        file.close()
        return int(autoid);
    def updatedata(self):
        self.id=input("\tEnter Id : ")
        self.modelno=input("\tEnter model no : ")
        self.name=input("\tEnter Customer's Name : ")
    def inputdata(self):#input
        self.id=self.getAutoId()+1
        print("\tCustomer Id : " + str(self.id))
        self.modelno=input("\tEnter model no : ")
        self.company=input("\tEnter Company : ")
        self.name=input("\tEnter Customer Name : ")
    def getid(self):
        return self.id
    def getmodelno(self):
        return  self.modelno
    def getcompany(self):
        return self.company
    def getname(self):
        return self.name

class Mobile:
    modelno=0
    name=''
    company=''
    customerid=''
    def inputdata(self):
        self.modelno=input("enter Model_No. : ")
        self.company=input("enter Company Name : ")      
    def display(self):
        print("Customer's id : "+str(self.customerid))
        print("Model_No. : "+str(self.modelno))
        print("Customer's Name : "+str(self.name))
        print("Company : "+str(self.company))      
    def getcustomeroid(self):
        return self.customerid
    def getmodelno(self):
        return self.modelno
    def getname(self):
        return self.name
    def getcompany(self):
        return self.company

def AddMobile():
    file=open('mobile.dat','ab')
    mobile=Mobile()
    mobile.inputdata()
    pickle.dump(mobile,file)
    file.close()

def DisplayMobile():
    file=open('Mobile.dat','rb')
    while True:
        try:
            mobile=pickle.load(file)
            mobile.display()
        except EOFError:
            break
    file.close()



def DeleteMobile():
    file=open('mobile.dat','rb')
    temp=open('temp.dat','ab')
    r=0
    modelno=input("Enter Model No. to Delete Record : ")
    while True:
        try:
            mobile=pickle.load(file)
            if(mobile.getmodelno()==modelno):
                pickle.dump(mobile, temp)
                r=1
        except EOFError:            
            break
    file.close()
    temp.close()
    if r==0:
        print("Record doestnot exist")

    os.remove('mobile.dat')
    os.rename('temp.dat','mobile.dat')

def SearchMobile():
    file=open('mobile.dat','rb')
    flag=0
    modelno=input("Enter Model No. to Search Record : ")
    while True:
        try:
            mobile=pickle.load(file)
            if(mobile.getmodelno()==modelno):
                flag=1
                mobile.display()
        except EOFError:            
            break        
    file.close()

    if flag==0:
        print("Mobile Not Found")
    
    
def UpdateMobile():
    file=open('mobile.dat','rb')
    temp=open('temp.dat','ab')
    modelno=input("Enter Model No. to Update Record : ")
    while True:
        try:
            mobile=pickle.load(file)
            if(mobile.getmodelno()=="101"):
                book.inputdata()
            pickle.dump(mobile, temp)
        except EOFError:            
            break
    file.close()
    temp.close()

    os.remove('mobile.dat')
    os.rename('temp.dat','mobile.dat')


def AddCustomer():
    file=open('customer.dat','ab')
    customer=Customer()
    customer.inputdata()
    pickle.dump(customer,file)
    file.close()

def DisplayCustomer():
    file=open('customer.dat','rb')

    line="\t"
    for i in range(80):
        line=line+"-"
        
    print(line)    
    print("\t| Customer ID\t\t| Name\t\t| Company\t\t| Model no")
    print(line)
    while True:
        try:
            s=pickle.load(file)
            print("\t| "+str(s.getid()) + "\t\t\t| " + str(s.getname()) + "\t\t| " + str(s.getcompany()) + "\t\t| " + str(s.getmodelno()))
            print(line)
        except EOFError:
            break
    file.close()

def DeleteCustomer():
    file=open('customer.dat','rb')
    temp=open('temp.dat','ab')
    sid=input("Enter Customer Id to Delete Record : ")
    while True:
        try:
            customer=pickle.load(file)
            if(customer.getid()==sid):
                pickle.dump(customer, temp)
        except EOFError:            
            break
    file.close()
    temp.close()

    os.remove('customer.dat')
    os.rename('temp.dat','customer.dat')

def SearchCustomer():
    file=open('customer.dat','rb')
    flag=0
    sid=input("Enter Customer Id to Search Record : ")
    while True:
        try:
            customer=pickle.load(file)
            if(customer.getid()==sid):
                flag=1
                print("Id : ", customer.getid())
                print("Modelno. : ", customer.getmodelno())
                print("Company : ", customer.getcompany())
                print("Name : ", customer.getname())
        except EOFError:            
            break      
    file.close()

    if flag==0:
        print("Customer Not Found")
    
    
def UpdateCustomer():
    file=open('customer.dat','rb')
    temp=open('temp.dat','ab')
    sid=int(input("Enter Customer Id to Update Record : "))
    while True:
        try:
            customer=pickle.load(file)
            if(customer.getid()!=sid):
                customer.updatedata()
            pickle.dump(customer, temp)
        except EOFError:            
            break
    file.close()
    temp.close()

    os.remove('customer.dat')
    os.rename('temp.dat','customer.dat')




def Header():
    _=os.system('cls')

    s=""
    for i in range(120):
        s=s+"-"

    
    print()
    print(s)
    print("\t\t\t\t\t RICH HARD")
    print("\t\t\t\t\t\tDelhi")
    print("\t\t\tWork hard, be kind, and amazing things will happen. ")
    print(s)
    
def MobileMenu():
    while True:
        Header()
        print()
        print("\t\t\t\t\tMobile Menu")
        print()
        print("1. Add New Mobile")
        print("2. Delete a Mobile")
        print("3. Update Mobile Details")
        print("4. Search Mobile")
        print("5. Display All Mobiles")
        print("0. For Exit")
        print("")
        print("")
        choice=int(input("Enter Your Choice : "))
        if choice==1:
            AddMobile()
        elif choice==2:
            DeleteMobile()
        elif choice==3:
            UpdateMobile()
        elif choice==4:
            SearchMobile()
        elif choice==5:
            DisplayMobile()
        elif choice==0:
            break
        _=input("")
        
        
def CustomerMenu():
    while True:
        Header()
        print()
        print("\t\t\t\t\tCustomer's Menu")
        print()
        print("\t1. Add Customer Details")
        print("\t2. Delete Customer Details")
        print("\t3. Update Customer Details")
        print("\t4. Search Customer Details")
        print("\t5. Print Customer Details")
        print("\t0. For Exit")
        print("")
        print("")
        choice=int(input("\tEnter Your Choice : "))
        print("")
        print("")
        if choice==1:
            AddCustomer()
        elif choice==2:
            DeleteCustomer()
        elif choice==3:
            UpdateCustomer()
        elif choice==4:
            SearchCustomer()
        elif choice==5:            
            DisplayCustomer()
        elif choice==0:
            break
        print("")
        print("")
        print("")
        input("\tPress Any Key to continue....")
   
        
def MainMenu():
    while True:
        Header()
        print()
        print("\t\t\t\t\tMain Menu")
        print()
        print("\t1. Manage Mobile Records")
        print("\t2. Manage Customer Records")
        print("\t0. For Exit")
        print("")
        print("")

        choice=int(input("\tEnter Your Choice : "))
        if choice==1:
            MobileMenu()
        elif choice==2:
            CustomerMenu()
        elif choice==0:
            break
        
            
s=MainMenu()
