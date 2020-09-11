from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("design.kv")

def dec_to_bin(n):  
    return bin(n).replace("0b", "")

def bin_to_dec(n):
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value; 

class Sc(Screen):
    def one(self,calculation):
        x=""+calculation+"1"
        self.ids.calculation.text=x
    def zero(self,calculation):
        x=""+calculation+"0"
        self.ids.calculation.text=x
    def clear(self,calculation):
        x=""
        self.ids.calculation.text=x
    
    def equal(self,calculation):
        x=""+calculation
        a=""
        b=""
        c=""
        for i in x:
            if i=='+':
                c="+"
            elif i=='-':
                c="-"
            elif i=='/':
                c="/"
            elif i=='X':
                c="X"
        a=int(x[0:int(x.index(c))])
        b=int(x[int(x.index(c))+1:len(x)])
        
        a1=(bin_to_dec(a))
        b1=(bin_to_dec(b))
        c1=0
        if c=='+':
            c1=a1+b1
        elif c=='/':
            c1=int(a1/b1)
        elif c=='X':
            c1=int(a1*b1)
        elif c=='-':
            c1=a1-b1
        x=str(dec_to_bin(c1))
        self.ids.calculation.text=x
    
    def plus(self,calculation):
        x=""+calculation+"+"
        self.ids.calculation.text=x
    def minus(self,calculation):
        x=""+calculation+"-"
        self.ids.calculation.text=x
    def multiplication(self,calculation):
        x=""+calculation+"X"
        self.ids.calculation.text=x
    def divide(self,calculation):
        x=""+calculation+"/"
        self.ids.calculation.text=x

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()