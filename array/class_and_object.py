# class test :
#     def __init__(self):
#         self.a=10
#         self.b=19
        
# t1=test()        
# t2=test()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
class emp:
    def __init__(self,empid=None,empname=None,empsal=None):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
    def setempid(self,empid):
        self.empid=empid
    def setempname(self,empname):
        self.empname=empname
    def setempsal(self,empsal):
        self.empsal=empsal 
    def getempid(self):
        return self.empid
    def getempname(self):
        return self.empname
    def getempsal(self):
        return self.empsal
e1=emp()            
e2=emp(1,"shivam",20000)
e1.setempid(1)
e1.setempname("rahul")
e1.setempsal(70000)
print(e1.getempid(),e1.getempname(),e1.getempsal())
print(e2.getempid(),e2.getempname(),e2.getempsal())
