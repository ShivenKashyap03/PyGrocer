import os
import datetime as dt
import sqlite3 as sql

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from PIL import ImageTk, Image

import matplotlib as mat
import matplotlib.pyplot as plt

eql = lambda a,b: set(a) == set(b)
today = dt.datetime.now().strftime("%d - %m - %Y")
installdir = os.path.split(__file__)[ 0 ]

conn = sql.connect(installdir + "\\main.db")
cur = conn.cursor()
try: cur.execute("create table data(name text, date text, product text, grtotal float)")
except: pass

def main(idir):
    x = idir
    clear   = lambda wid : [i.destroy() for i in wid.winfo_children()]
    imgopen = lambda n: ImageTk.PhotoImage(Image.open(n))

    root = Tk()
    root.resizable(0, 0)
    root.geometry("900x700+0+0")
    root.title("PyGrocer")
    root.tk.call("source", x + "\\azure\\azure.tcl")
    root.tk.call("set_theme", "light")
    root.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(x + "\\img\\icon.png")))
    
    wcm = ImageTk.PhotoImage(Image.open(x + "\\img\\welcome.png").resize((875, 680)))
    frame=Frame(root,highlightthickness=10, highlightbackground="#0492C2")
    frame.pack(side="top", fill="both", expand=1)
    
    Label(frame, image=wcm).place(x=0, y=0)
    
    button = ttk.Button(frame,text = "Explore ➜", style="Accent.TButton", command = lambda:proceedtoLogin())
    button.place(x=630, y=620, width=200)

    theme = StringVar()

    def toggle_theme(*a):
        if theme.get() == "dark":
            theme.set("light")
            root.tk.call("set_theme", "light")

        else:
            theme.set("dark")
            root.tk.call("set_theme", "dark")  

    theme.trace_add('write', toggle_theme)
    
    toggler = ttk.Checkbutton(root, text = "Dark Theme", variable=theme, onvalue="light", offvalue="dark")
    toggler.pack(side="bottom", anchor="sw")

    class Product(Frame):
        def __init__(self, master, name, price, image, qtyfrom=0, qtyto=100):
            root.update()
            self.price = price
            self.name = name
            
            Frame.__init__(self, master, width=master.winfo_width() // 4, height=master.winfo_height())

            qty = IntVar(root, 0)
            
            self._ = ttk.Spinbox(
                self, from_=qtyfrom, to=qtyto, width=3, 
                textvariable=qty, state="readonly", font=("Segoe UI", 15, 'normal'))
            self._.pack(side="bottom", anchor='s', expand=1)
            
            Label(self, text = "%s | ₹ %s/-" % (name, price)).pack(side="bottom", fill='x', expand=1, anchor="c")
            
            l = Label(self, image=image); l.pack(side="top", anchor="c")
            l.dontloseit = image
            
            root.update()
            self.pack_propagate(0)

    def RenderInvoice(w, data, grt) -> None:
        global entry

        Label(w, text="Order Invoice:", font="Calbri 20 bold" ).pack(side='top', anchor='c', fill='x')
        Label(w, text="Date: %s" % today,  font="Calibri 15 bold").pack(side='top', anchor='nw')
        Label(w, text="Customer Name: ", font="Calibri 15 normal").pack(side='top', anchor='nw')
        
        
        entry = Entry(w, width=20, font=("Calibri",15), bd=2); entry.pack(side='top', anchor='nw')
        tree = ttk.Treeview(w, columns=(1,2,3,4), show='headings'); tree.pack(side="top", fill='x')
        
        for i in range(1, 5):
            tree.heading(i, text=("Product", "Price", "Quantity", "Product Total")[i-1], anchor='c')
            tree.column(i, anchor='c')
        
        for i in data:
            tree.insert('', 'end', values=i)
        
        Label(w, text="Grand Total: %f" % grt, font="Calibri 15 bold").pack(side='bottom', fill='x', anchor='c')

    def proceedtoLogin():
        frame.destroy()
        
        frame1 = Frame(root, height=300, width=700, highlightbackground="#0492C2", highlightthickness=10)
        frame1.pack(expand=1, fill="both")
        
        frame2 = Frame(frame1, bg="#69a1fa", width=600, height=400)
        frame2.place(x=150, y=100)

        Label(frame1,text="Login", font=("Calibri", 30,),bg="#69a1fa", foreground="white",relief = FLAT).pack(side="top", anchor="c", fill="x")
        Label(frame2,text=" Username : ",bg="#69a1fa",font=("Calibri",18), justify="left").place(x=120, y=150)
        Label(frame2,text=" Password : ",bg="#69a1fa",font=("Calibri",18)).place(x=120, y=250)

        name_entry1=Entry(frame2, width=20, font=("Calibri",18), bd=0)
        name_entry1.place(x=270, y=150)
        
        pwd_entry1=Entry(frame2,show="*", width=20, font=("Calibri",18), bd=0)
        pwd_entry1.place(x=270, y=250)

        def Logincheck():
            uname = name_entry1.get()
            pwd = pwd_entry1.get()
        
            if uname and pwd:
                # case sensitive ?
                if uname == 'tulika':
                    if pwd == 'tulika': 
                        proceedtoMain()

                elif uname == 'shiven':
                    if pwd == 'shiven':
                        proceedtoAdmin()

                else:
                    showerror("Login Failed!", "Username and/or password not recognized.")

            else:
                showerror("Field Empty", "Username or Password field(s) can not be empty.")

        button1 = ttk.Button(frame1, text = "Next", style="Accent.TButton", command=Logincheck)
        button1.place(x=650, y=620, width=200)

        def proceedtoMain():
            global objs
            clear(frame1)

            L1 = ttk.LabelFrame(frame1,text="Snacks:   ",)
            L1.pack(side="top", fill='x', expand=0)
            
            L2 = ttk.LabelFrame(frame1,text="Beverages: ")
            L2.pack(side="top", fill='x', expand=0)
            
            L3 = ttk.LabelFrame(frame1,text="Bread: ")
            L3.pack(side="top", fill='x', expand=0)

            data = {
                0 :
                [
                    ["Chips", 10, imgopen(x + "\\img\\" + "chips.jpg")],
                    ["Biscuits", 20, imgopen(x + "\\img\\" + "bisc.jpg" )],
                    ["Chocolate", 40, imgopen(x + "\\img\\" + "choc.jpg")], 
                    ["Maggi", 15, imgopen(x + "\\img\\" + "maggi.jpg") ]
                ],

                1 : 
                [
                    ["Juice", 10, imgopen(x + "\\img\\" + "juice.jpg")], 
                    ["Coca Cola", 35, imgopen(x + "\\img\\" + "coke.jpg")], 
                    ["Cold Coffee", 20, imgopen(x + "\\img\\" + "coffee.jpg")], 
                    ["Iced Tea", 10, imgopen(x + "\\img\\" +"icetea.jpg")]
                ],

                2 : 
                [
                    ["Garlic Bread", 20, imgopen(x + "\\img\\" + "gbread.jpg")],
                    ["Footlong Bread", 30, imgopen(x + "\\img\\" + "sub.jpg")], 
                    ["White Bread" , 40, imgopen(x + "\\img\\" + "wbread.jpe")], 
                    ["Brown Bread"   , 45, imgopen(x + "\\img\\" +"bbread.jpg")]
                ]
            }

            objs = []

            cont = [L1, L2, L3]
            c = 0

            for i in data:
                for j in data[i]:
                    _ = Product(cont[c], *j); _.pack(side="left", fill='both', expand=1)
                    objs.append(_)

                c+=1

            L1.pack_propagate(0)
            L2.pack_propagate(0)
            L3.pack_propagate(0)

            cart = ttk.Button(frame1, text="Proceed", style="Accent.TButton", command=lambda: invoice())
            cart.place(x=600, y=600, width=200)

        def placeorder(i):
            global entry;
            t = entry.get().strip();
            print(t)

            if not t:
                showerror("Name Field Empty!", "Customer Name Field can not be left empty!")

            else:
                n, d, p, g = i;
                # save order in db;
                conn.execute("insert into data values('%s', '%s', '%s', %f);" % (n, d, p, g))
                conn.commit()
                
                showinfo("Order Successful!", "Your order was placed!");
                proceedtoMain()

        def _viz():
            # sales per month.
            global s

            data = conn.execute("select * from data")
            data = list(data.fetchall())

            s = { i: 0 for i in range(1, 13) }

            for i in data:
                j = int(i[1].split("-")[1].strip())
            
                s[j] += i[-1]

            plt.bar(list(range(1, 13)), [s[_] for _ in s])
            
            plt.xlabel("Months")
            plt.ylabel("Sales Per Month")
            plt.legend(["bar"])
            plt.show()

        def sales():
            # open the command prompt and show the table.
            stuff = conn.execute("select * from data;")

            print(stuff.fetchall())
            
            showinfo(
                "Check console output!", 
                "All the database contents have been printed onto the console. Please check the terminal window."
            )

        def proceedtoAdmin():
            clear(frame1)
            img = ImageTk.PhotoImage(Image.open(x + "\\img\\admin.png").resize((600, 500)))
            
            aaa = Label(frame1, image=img,)
            aaa.dontloseit = img
            aaa.pack(side="bottom", anchor='c')

            viz = ttk.Button(frame1, text="Visualize past sales", style="Accent.TButton", command=_viz);  viz.pack(side="top",)
            dbexp = ttk.Button(frame1, text="Check Sales record", style="Accent.TButton", command=sales); dbexp.pack(side='top')

        def invoice():
            global objs
            root.update()
            
            items, prods, grt = [], [], 0
            
            for i in objs:
                if i is not None:
                    qtypero = i._.get()
                    try:
                        if int(qtypero) != 0:
                            qty = int(qtypero)
                            items.append([i.name, i.price, qty, qty * i.price])
                            grt += i.price * qty
                            prods.append("%s(%d)" % (i.name, qty))
                    except:
                        pass

            if not items:
                showinfo("Nothing to Order!", "You have not added any items to cart, terminating order.")
                return

            else:
                clear(frame1)
                RenderInvoice(frame1, items, grt)

            global entry
            tosave = [today, ",".join(prods), grt]

            finish = ttk.Button(frame1, text="Confirm Order", style="Accent.TButton", command = lambda: placeorder([entry.get().strip(), *tosave]))
            finish.place(x=0, y=590, width=200)
            cancel = ttk.Button(frame1, text="Cancel Order" , style="Accent.TButton", command=lambda: proceedtoMain())
            cancel.place(x=201, y=590, width=200)

    root.mainloop()

main(installdir)
