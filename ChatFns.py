from Tkinter import *
from socket import *
import urllib
import re

def FilteredMessage(EntryText):
    """
    Filter out all useless white lines at the end of a string,
    returns a new, beautifully filtered string.
    """
    EndFiltered = ""
    for i in range(len(EntryText)-1,-1,-1):
        if EntryText[i]!='\n':
            EndFiltered = EntryText[0:i+1]
            break
    for i in range(0,len(EndFiltered), 1):
            if EndFiltered[i] != "\n":
                    return EndFiltered[i:]+'\n'
    return ""

def LoadConnectionInfo(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            ChatLog.insert(END, EntryText+'\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def LoadMyEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, "You: " + EntryText)
            ChatLog.tag_add("You", LineNumber, LineNumber+0.4)
            ChatLog.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def LoadOtherEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            try:
                LineNumber = float(ChatLog.index('end'))-1.0
            except:
                pass
            ChatLog.insert(END, "Anon: " + EntryText)
            ChatLog.tag_add("Anon", LineNumber, LineNumber+0.6)
            ChatLog.tag_config("Anon", foreground="#04B404", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)