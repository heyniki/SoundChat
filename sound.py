import random
from Tkinter import *

class menu(object):
    def createButtons(self):
        font = "Helvetica 20"
        self.startButton = Button(self.canvas, font=font, text="Start Sound Chat", width = 16,
                               height = 1, bg = "black", fg="white", command=self.startPressed)

    def startPressed(self): #when start chat is pressed       
        self.canvas.delete(ALL)
        self.chatBack = PhotoImage(file="chatBackground.gif")

        self.root.destroy()
        import chat2
        chat2.run()

    def init(self):
        self.createButtons()

        self.canvas.delete(ALL)

        self.title = PhotoImage(file="background2.gif")
        self.canvas.create_image(0, 0, anchor = NW, image=self.title)
        self.canvas.create_window(350, 350, window=self.startButton)

    def run(self, width, height):
        self.width = width
        self.height = height    
        self.halfWidth = self.width/2 #useful for buttons
        self.root = Tk()
        self.root.resizable(width=FALSE, height=FALSE) #non-resizable!
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.init()
        self.root.mainloop()
   
app = menu()
app.run(700, 500) 