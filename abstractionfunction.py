class Employee:
    __firstName:str="vinay"
    __lastName:str="Kumar"
    def fullName(self):
        return self.__nameFormat(self.__firstName,self.__lastName)
    def __nameFormat(self,fName:str,lName:str):
        return f"{fName}{lName}"
emp=Employee()
emp.__firstName="ANU"
print(emp.fullName())
#print(emp.__firstName("vinay","kumar"))
