import tkinter as tk


class theCalculator:

    def __init__(self, master):
        master.wm_title("Calculator")
        master.geometry("340x350")
        master.resizable(0, 0)

        signsList = ["-","+","*","/","%"]
        #Declaring the buttons
        
        self.textField = tk.Entry(master, width=16, font=("Arial Bold",20))
        self.textField.place(x=40,y=50)

        self.cButton = tk.Button(master, text="C", width=14, height=2, command = lambda:cleanSpace(self))
        self.cButton.place(x=40, y=100)

        self.modButton = tk.Button(master, text="%", width=5, height=2,command=lambda:signThings(self,"%"))
        self.modButton.place(x=180, y=100)

        self.divButton = tk.Button(master, text="/", width=5, height=2,command=lambda:signThings(self,"/"))
        self.divButton.place(x=248, y=100)

        self.xButton = tk.Button(master, text="x", width=5, height=2, bg="yellow",command=lambda:signThings(self,"*"))
        self.xButton.place(x=248, y=142)

        self.minusButton = tk.Button(master, text="-", width=5, height=2, bg="yellow",command=lambda:signThings(self,"-"))
        self.minusButton.place(x=248, y=185)

        self.plusButton = tk.Button(master, text="+", width=5, height=2, bg ="yellow",command=lambda:signThings(self,"+"))
        self.plusButton.place(x=248, y=228)

        self.nineButton = tk.Button(master, text="9", width=5, height=2,command=lambda:setText(self,"9"))
        self.nineButton.place(x=40, y=142)

        self.eightButton = tk.Button(master, text="8", width=5, height=2,command=lambda:setText(self,"8"))
        self.eightButton.place(x=110, y=142)

        self.sevenButton = tk.Button(master, text="7", width=5, height=2,command=lambda:setText(self,"7"))
        self.sevenButton.place(x=180, y=142)

        self.sixButton = tk.Button(master, text="6", width=5, height=2,command=lambda:setText(self,"6"))
        self.sixButton.place(x=40, y=185)

        self.fiveButton = tk.Button(master, text="5", width=5, height=2,command=lambda:setText(self,"5"))
        self.fiveButton.place(x=110, y=185)

        self.fourButton = tk.Button(master, text="4", width=5, height=2,command=lambda:setText(self,"4"))
        self.fourButton.place(x=180, y=185)

        self.threeButton = tk.Button(master, text="3", width=5, height=2,command=lambda:setText(self,"3"))
        self.threeButton.place(x=40, y=228)

        self.twoButton = tk.Button(master, text="2", width=5, height=2,command=lambda:setText(self,"2"))
        self.twoButton.place(x=110, y=228)

        self.oneButton = tk.Button(master, text="1", width=5, height=2,command=lambda:setText(self,"1"))
        self.oneButton.place(x=180, y=228)

        self.zeroButton = tk.Button(master, text="0", width=14, height=2,command=lambda:zeroThings(self))
        self.zeroButton.place(x=40, y=271)

        self.pointButton = tk.Button(master, text=".", width=5, height=2,command=lambda:dotThings(self))
        self.pointButton.place(x=180, y=271)

        self.equalsButton = tk.Button(master, text="=", width=5, height=2, bg="yellow",command=lambda:calculate(self))
        self.equalsButton.place(x=248, y=271)

        #Declaring the methods
        
        def setText(self, text):
            
            self.textField.insert(tk.END,  text)

        def signThings(self, sign):
            
            theText = self.textField.get()

            if(len(theText)==0):
                print("The first character can't be a sign")
                return 0;

            if(theText[-1] in signsList):
                print("Can't have two signs one after another")
                return 0;

            if(theText[-1]=="."):
                print("Can't have a sign after .")
                return 0;

            self.textField.insert(tk.END, sign)


        def calculate(self):
            
            theResult = eval(self.textField.get())
            self.textField.delete(0, tk.END)
            self.textField.insert(0, str(round(theResult,4)))

        def cleanSpace(self):
            
            self.textField.delete(0, tk.END)

        def zeroThings(self):
            
            theText = self.textField.get()
            if(len(theText)==1):
                if(theText==0):
                    print("Can't have two zeroes one after another")
                else:
                    self.textField.insert(tk.END,"0")
            elif(len(theText)>1):
                self.textField.insert(tk.END,"0")

        def dotThings(self):
            
            theText = self.textField.get()
            numberOfSigns = 0
            numberOfDots = 0

            for c in theText:
                if c in signsList:
                    numberOfSigns +=1
                if c==".":
                    numberOfDots +=1
            try:
                if (numberOfSigns>=numberOfDots and theText[-1] not in signsList):
                    self.textField.insert(tk.END,".")
            except Exception as e:
                self.textField.insert(tk.END,".")
                    
                                        
root = tk.Tk()

calc = theCalculator(root)

root.mainloop()
