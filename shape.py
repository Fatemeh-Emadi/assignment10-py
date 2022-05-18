from math import pi

class shape:
    def __init__(self,mohit=0,masahat=0):
        self.mohit=mohit
        self.masahat=masahat
    def show(self):
         print("Mohit:",self.mohit)
         print("Masahat:",self.masahat)
    
class circle(shape):
     def __init__(self,radius):
         self.r=radius

     def mohit(self):
         self.mohit=pi*self.r*2
     def masahat(self):
         self.masahat=pi*self.r*self.r         

class rectangle(shape):
    def __init__(self,width,height):
         self.w=width
         self.h=height
    def mohit(self):
        self.mohit=2*(self.h+self.w)
    def masahat(self):
        self.masahat=self.h*self.w
        
print("Rectangle")
rect=rectangle(2,4)
rect.mohit()
rect.masahat()
rect.show()
print("Circle")
cir=circle(6)
cir.mohit()
cir.masahat()
cir.show()

    
      

        