#Quote Of the Day (Lucifer Edition)

import tkinter
import random

tkinter.Tcl().eval('info patchlevel')

from tkinter import *
from tkinter import ttk

class aplicacion:
    def __init__(self):

        self.raiz = Tk()
        self.raiz.geometry("850x150")
        self.raiz.resizable(width=False, height=False)
        self.raiz.title("Quote of the Day (Lucifer EDITION)")

        self.tinfo = Text(self.raiz, width=120, height=8)
        self.tinfo.pack(side=TOP)
        
        
        self.binfo = ttk.Button(self.raiz, text="Quotes",
                                command=self.quote)
        self.binfo.pack(side=LEFT)
        self.bsalir = ttk.Button(self.raiz, text="Salir",
                                 command=self.raiz.destroy)

        self.bsalir.pack(side=RIGHT)

        self.raiz.configure(bg = 'beige')


        TextQ = "                 \n"
        TextQ += "                 \n"
        TextQ += "          Bienvenido a Random Quotes \n"
        TextQ += "                 \n"
        TextQ += "                 \n"

        self.tinfo.insert("1.0", TextQ)
        self.binfo.focus_set()
        self.raiz.mainloop()

    def quote(self):

        self.tinfo.delete("1.0", END)

        quotes = []

        quotes.append("“Sometimes it’s easier to make intimate issues about something bigger than yourself.” \n             -Linda Martin")
        quotes.append("“When angels fall, they also… rise.” \n             -Lucifer Morningstar")
        quotes.append("“If you desire something, just take it.” \n             -Lucifer Morningstar")
        quotes.append("“You see, what I hate more than anything is a liar. A charlatan. Someone who doesn’t believe in what they say. ” \n             -Lucifer Morningstar")
        quotes.append("“A deal’s a deal, especially one with the Devil. ” \n             -Lucifer Morningstar")
        quotes.append("“Now tell me, what is it that you truly desire?” \n             -Lucifer Morningstar")
        quotes.append("Whenever you're faced with a choice, ask yourself the question: WWLD... What would Lucifer do?")
        quotes.append("Chloe: If I pushed this into your chest... it would kill you?\n" + "  Lucifer: Yes\n" + "  Chloe: But you jumped in front it anyway\n" + "...\n" + "  Lucifer: And I would do it again, and again, and again, don't you know that, detective?\n")                   

        dailyQuote = random.choice(quotes)

        TextQ = "\n"
        TextQ += "\n"
        TextQ += "    " + dailyQuote
        TextQ += "\n"
        TextQ += "\n"

        self.tinfo.insert("1.0", TextQ)
        

def main():
    my_app = aplicacion()
    return 0

if __name__ == "__main__":
    main()
