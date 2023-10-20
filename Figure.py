class figure:
    def input(self):
        return self
    def perim(self):
        return 0
    def square(self):
        return 0

class point(figure):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def input(self):
        s=input().split()
        self.x=float(s[0])
        self.y=float(s[1])
        return self

def dist(A,B):
    return ((A.x-B.x)**2+(A.y-B.y)**2)**0.5

class section(figure):
    def __init__(self,A=point(),B=point(1,0)):
        self.A=A
        self.B=B
    def input(self):
        self.A.input()
        self.B.input()
        return self
    def length(self):
        return dist(self.A,self.B)
    def perim(self):
        return 2*self.length()

def dist(A,B):
    return ((A.x-B.x)**2+(A.y-B.y)**2)**0.5

class triangle(figure):
    def __init__(self,A=point(),B=point(),C=point()):
        self.A=A
        self.B=B
        self.C=C
        self.AB=section(self.A,self.B)
        self.BC=section(self.B,self.C)
        self.CA=section(self.C,self.A)
    def input(self):
        self.A.input()
        self.B.input()
        self.C.input()
        self.AB=section(self.A,self.B)
        self.BC=section(self.B,self.C)
        self.CA=section(self.C,self.A)
        return self
    def perim(self):
        return self.AB.length()+self.BC.length()+self.CA.length()
    def square(self):
        p=self.perim()/2
        return (p*(p-self.AB.length())*(p-self.BC.length())*(p-self.CA.length()))**0.5

s=input()
D=globals()
if s in D:
    f=D[s]()
else:
    f=figure()
f.input()
print(f.perim())
print(f.square())