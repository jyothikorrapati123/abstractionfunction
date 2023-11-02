#Single level Inheritance

class Address:
    __Address:str=""
    def addAddress (self,address):
        self.__address=address
    def getAddress(self):
            return self.__address
class Employee (Address):
            __firstName:str=""
            __lastName:str=""
            __surName:str=""
            def setName (self,fName:str,lName:str,sName:str=""):
                self.__firstName=fName
                self.__surName=sName
                self.__lastName=lName
            def __nameFormat (self):
                return f'{self.__firstName} {self.__lastName} {self.__surName}'
            def getFullName(self):
                return self.__nameFormat()
emp=Employee()
emp.setName(fName="vinay",sName="K",lName="Kumar")
emp.addAddress("bengaluru")
print(emp.getFullName())
print(emp.getAddress())

