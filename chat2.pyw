from ChatFns import *

###import record

def sendMessage(string):
    a = []
    for c in string:
        a.append( format(ord(c), 'b'))
    return a


def receiveMessage(a):
    s = ""
    for c in a:
        s+= chr(int(c,2))
    return s

def listen(): 

    ##audio = record.getAudio()
    ##bitArray = removeBackgroundNoise(data)

    data = receiveMessage(sendMessage("listened\n"))

    LoadOtherEntry(ChatLog, data)

    EntryBox.config(state=NORMAL)
    SendButton.config(state=NORMAL)    


#---------------------------------------------------#
#------------------ MOUSE EVENTS -------------------#
#---------------------------------------------------#
def ClickAction():
    #Write message to chat window
    EntryText = FilteredMessage(EntryBox.get("0.0",END))
    LoadMyEntry(ChatLog, EntryText)

    #Scroll to the bottom of chat windows
    ChatLog.yview(END)

    #Erace previous message in Entry Box
    EntryBox.delete("0.0",END)
            
    sendMessage(EntryText)

    #listen here to take turns
    EntryBox.config(state=DISABLED)
    SendButton.config(state=DISABLED)
    listen()

#---------------------------------------------------#
#----------------- KEYBOARD EVENTS -----------------#
#---------------------------------------------------#
def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	EntryBox.config(state=DISABLED)

    
#---------------------------------------------------#
#-----------------GRAPHICS MANAGEMENT---------------#
#---------------------------------------------------#

#Create a window
base = Tk()
base.title("Sound Chat")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create a Chat window
ChatLog = Text(base, bd=0, bg="black", fg="white", height="8", width="50", font="Arial",)
#ChatLog.insert(END, "Waiting for your partner to connect..\n")
ChatLog.config(state=DISABLED)

#Bind a scrollbar to the Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create the Button to send message
SendButton = Button(base, font=30, text="Send", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="black", fg="white", width="29", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)

#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

def run(): 
    base.mainloop()