import secrets
import string
import sys
import urllib
import any
import requests
import mysql.connector
import Tkinter
import MySQLdb
from Tkinter import IntVar


class Dossantos(Tkinter.Frame):
       def __init__(self, BSU):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, BSU)
        self.BSU_Professor = None
        self.Nickson = None
        self.BSU=BSU
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """"
        Dossantos's MySQL server
        """
        self.BSU.title("DB operations")
        self.BSU.grid_rowconfigure(0,weight=1)
        self.BSU.grid_columnconfigure(0,weight=1)
        self.BSU.config(background="lavender")

        self.label_user=Tkinter.Label(self.BSU,text="DB User: ",anchor=Tkinter.W,background="dark slate gray",foreground="white")
        self.label_password=Tkinter.Label(self.BSU,text="DB Password:", anchor=Tkinter.W,background="dark slate gray")

        self.label_user.grid(row=0,column=0,sticky=Tkinter.E+Tkinter.W)
        self.label_password.grid(row=1,column=0, sticky=Tkinter.E+Tkinter.W)

        self.dbuser=Tkinter.Entry(self.parent)
        self.dbpassword=Tkinter.Entry(self.BSU,show="BSU*******")

        self.dbuser.grid(row=0,column=1,sticky=Tkinter.E+Tkinter.W)
        self.dbpassword.grid(row=1,column=1,sticky=Tkinter.E+Tkinter.W)


    def item_insertion_window(self):
        self.new_window=Tkinter.Toplevel(self)
        self.new_window.wm_title(" My Best Professor")
        self.new_window.grid_rowconfigure(0, weight=1)
        self.new_window.grid_columnconfigure(0, weight=1)

        self.exitb=Tkinter.Button(self.new_window,text="Exit",command=self.new_window.quit)
        self.submitb=Tkinter.Button(self.new_window,text="Submit",command=self.increment_db)
        self.exitb.grid(row=8,column=1)
        self.submitb.grid(row=8,column=0,sticky=Tkinter.W)

        self.v=IntVar()
        self.BSU_Professor=[('Dr.John Santor', 1), ('Dr.Black', 2),
                      ('Dr. Helen Khojasteh ', 3), ('Dr. Kim', 4),
                      ('Dr. Elif Demirbas', 5), ('Dr.Eping Li', 6),
                      ('Dr. Roger Homer', 7)]
        self.i=0
        for self.txt, star in self.BSU_Professor:
            self.i=self.i+1
            self.rb=Tkinter.BSUbutton(self.new_window,text=self.txt,variable=self.v,value=star)
            self.rb.grid(row=self.i,column=0,sticky=Tkinter.W)


    def which_BSU_Students(self,BSU):
        self.BSU_Students = {
                        1:"Alina Pakiad",
                        2:"Jonathan Opio",
                        3:"Junseak Hur",
                        4:"Maya Elysse",
                        5:"Mauli Sanketh Mature",
                        6:"Nickson Dossantos",
                        7:"Rydia Hayes Huer",
                        8: "Shatala Gaitode",
                        9: "Suvarna Sahu",
                        10: "Timathy Largeres",
        }
        return self.professor.get(BSU,"Unknown")

    def increment_db(self):
        #print self.v.get()
        self.chosenprofessor=self.which_professor(self.v.get())
        print self.chosenprofessor;

        self.config = {
                  'user': 'ndossantos1',
                  'passwd': 'Electronick2',
                  'host': '127.0.0.1',
                  'db': 'ndossantos',
        }
        try:
            self.connecttodb=MySQLdb.connect(**self.config)
        except MySQLdb.Error:
               print  "Connexion error",

        self.cursor=self.connecttodb.cursor()

        self.cursor.execute("""BSU Board""",self.chosenprofessor)

        self.connecttodb.commit()
        self.connecttodb.close()



    def dbconnexion(self):
        if self.dbuser.get()=="ndossantos1" and  self.dbpassword.get()=="Electronick2":
            self.item_insertion_window()
        else:
            self.initialize_user_interface()



def main():
    root=Tkinter.Tk()
    d=Electronick2(root)
    root.mainloop()

if __name__=="__main__":
    main()