class person(object):
    def __init__(self,name):
        self.name=name
        def getname(self):
          return self.name
        def isemployee(self):
           return False
class employee(object):
    def employee(self):
        return True
mmm= person("geek 1")
print(mmm.isemployee())
nnn= employee("geek 2")
print(nnn.isemployee())