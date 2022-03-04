from time import strftime
from tkinter import *
from tkinter import messagebox
import random




root = Tk()
root.geometry("1300x760+0+0")
root.title("Food Billing System")
root.configure(background="cornsilk")

#######################  Top Part Is Started ###########################

Tops = Frame(root,bg="cornsilk",border=15,pady=15,relief=RIDGE)
Tops.pack(side=TOP,fill=X)

lalTitle = Label(Tops,font="monospace 60 bold",text="Food Billing System"
                ,fg="yellow",justify=CENTER,bd=21,bg='black',)
lalTitle.pack()

lalTitle = Label(Tops,font="monospace 15 bold",text="Presented by @ Shishir"
                ,fg="yellow",justify=CENTER,bd=21,bg='red',)
lalTitle.pack(fill=X)

###########################  Top Part is End ###########################
###########################  Recipt Part Started #######################
ReceiptCal_F = Frame(root,bg="cornsilk",bd=10,relief=SUNKEN)
ReceiptCal_F.pack(side=RIGHT)

Bottons_F = Frame(ReceiptCal_F,bg="cornsilk",bd=3,relief=SUNKEN)
Bottons_F.pack(side=BOTTOM)

Cal_F = Frame(ReceiptCal_F,bg="cornsilk",bd=6,relief=SUNKEN)
Cal_F.pack(side=TOP)

Receipt_F = Frame(ReceiptCal_F,bg="cornsilk",bd=4,relief=SUNKEN)
Receipt_F.pack(side=TOP)

########################## Recipt Part End #############################
########################## Menu Part strted ############################

MenuFrame = Frame(root ,bg="cornsilk",bd=10,relief=SUNKEN)
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame,bg="cornsilk",bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame,bg="cornsilk",bd=4)
Drinks_F.pack(side=TOP)


Drinks_F = Frame(MenuFrame,bg="cornsilk",bd=4, relief= SUNKEN)
Drinks_F.pack(side=LEFT)
Food_F = Frame(MenuFrame,bg="cornsilk",bd=4, relief=SUNKEN)
Food_F.pack(side=RIGHT)

########################## Menu Part Ended ############################
########################## Variable Declaration #######################

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()


DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operater = ""

E_Sprite = StringVar()
E_Pepsi = StringVar()
E_Coke = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_Tea = StringVar()
E_GingerTea = StringVar()
E_ColdCoffee = StringVar()

E_Noddels = StringVar()
E_Moomos = StringVar()
E_Maggie = StringVar()
E_Pasta = StringVar()
E_Sandwich = StringVar()
E_Fires = StringVar()
E_Samosa = StringVar()
E_chole = StringVar()

############################# SET value 0 ###########################

E_Sprite.set("0")
E_Pepsi.set("0")
E_Coke.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_Tea.set("0")
E_GingerTea.set("0")
E_ColdCoffee.set("0")

E_Noddels.set("0")
E_Moomos.set("0")
E_Maggie.set("0")
E_Pasta.set("0")
E_Sandwich.set("0")
E_Fires.set("0")
E_Samosa.set("0")
E_chole.set("0")


DateofOrder.set(strftime("%d - %m - %y"))

########################### Function Declaration #############################

def Exit():
    iExit = messagebox.askyesno("Exit","Confirm Do You Want To Exit")
    if iExit > 0:
        root.destory()
        return

def Reset():

    PaidTax = StringVar()
    SubTotal = StringVar()
    TotalCost = StringVar()
    CostofFood = StringVar()
    CostofDrinks = StringVar()
    ServiceCharge = StringVar()
    txtReceipt.delete("1.0",END)


    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_Coke.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_Tea.set("0")
    E_GingerTea.set("0")
    E_ColdCoffee.set("0")

    E_Noddels.set("0")
    E_Moomos.set("0")
    E_Maggie.set("0")
    E_Pasta.set("0")
    E_Sandwich.set("0")
    E_Fires.set("0")
    E_Samosa.set("0")
    E_chole.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtSprite.configure(state = DISABLED)
    txtPepsi.configure(state = DISABLED)
    txtCoke.configure(state = DISABLED)
    txtFanta.configure(state = DISABLED)
    txtCocaCola.configure(state = DISABLED)
    txtTea.configure(state = DISABLED)
    txtGingerTea.configure(state = DISABLED)
    txtColdCoffee.configure(state = DISABLED)

    txtNoddels.configure(state = DISABLED)
    txtMoomos.configure(state = DISABLED)
    txtMaggie.configure(state = DISABLED)
    txtPasta.configure(state = DISABLED)
    txtSandwich.configure(state = DISABLED)
    txtFires.configure(state = DISABLED)
    txtSamosa.configure(state = DISABLED)
    txtchole.configure(state = DISABLED)
    
def CostofItem():
    Item1=float(E_Sprite.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_Coke.get())
    Item4=float(E_Fanta.get())
    Item5=float(E_CocaCola.get())
    Item6=float(E_Tea.get())
    Item7=float(E_GingerTea.get())
    Item8=float(E_ColdCoffee.get())

    Item9=float(E_Noddels.get())
    Item10=float(E_Moomos.get())
    Item11=float(E_Maggie.get())
    Item12=float(E_Pasta.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Fires.get())
    Item15=float(E_Samosa.get())
    Item16=float(E_chole.get())

    PriceofDrinks =(Item1 * 40) + (Item2 * 40) + (Item3 * 40) + (Item4 * 40) + (Item5 * 40) + (Item6 * 10) + (Item7 * 12) + (Item8 * 35)

    PriceofFood =(Item9 * 60) + (Item10 * 50) + (Item11 * 30) + (Item12 * 50) + (Item13 * 20) + (Item14 * 60) + (Item15 * 15) + (Item16 * 30)

    
    DrinksPrice = "$",str("%.2f"%PriceofDrinks)
    FoodPrice = "$",str("%.2f"%PriceofFood)

    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)

    SC = "$",str("%.2f"%40)
    ServiceCharge.set(SC)

    SubTotalofITEMS = "$",str('%.2f'%(PriceofDrinks + PriceofFood + 40))
    SubTotal.set(SubTotalofITEMS)

    Tax = "$",str('%.2f'%((PriceofDrinks + PriceofFood + 40) * 0.18))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 40) * 0.18)
    TC="$",str('%.2f'%(PriceofDrinks + PriceofFood + 40 + TT))
    TotalCost.set(TC)
############################## Check box functions #############################################
def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',END)
        E_Sprite.set("")
    elif(var1.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chkPepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',END)
        E_Pepsi.set("")
    elif(var2.get() == 0):
        txtPepsi.configure(state = DISABLED)
        E_Pepsi.set("0")

def chk_Coke():
    if(var3.get() == 1):
        txtCoke.configure(state = NORMAL)
        txtCoke.delete('0',END)
        txtCoke.focus()
    elif(var3.get() == 0):
        txtCoke.configure(state = DISABLED)
        E_Coke.set("0")

def chk_Tea():
    if(var4.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.delete('0',END)
        txtTea.focus()
    elif(var4.get() == 0):
        txtTea.configure(state = DISABLED)
        E_Tea.set("0")

def chk_GingerTea():
    if(var5.get() == 1):
        txtGingerTea.configure(state = NORMAL)
        txtGingerTea.delete('0',END)
        txtGingerTea.focus()
    elif(var5.get() == 0):
        txtGingerTea.configure(state = DISABLED)
        E_GingerTea.set("0")

def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = DISABLED)
        E_Fanta.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_ColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        E_ColdCoffee.set("0")

def chk_Noddels():
    if(var9.get() == 1):
        txtNoddels.configure(state = NORMAL)
        txtNoddels.delete('0',END)
        txtNoddels.focus()
    elif(var9.get() == 0):
        txtNoddels.configure(state = DISABLED)
        E_Noddels.set("0")

def chk_Maggie():
    if(var10.get() == 1):
        txtMaggie.configure(state = NORMAL)
        txtMaggie.delete('0',END)
        txtMaggie.focus()
    elif(var10.get() == 0):
        txtMaggie.configure(state = DISABLED)
        E_Maggie.set("0")

def chk_Pasta():
    if(var11.get() == 1):
        txtPasta.configure(state = NORMAL)
        txtPasta.delete('0',END)
        txtPasta.focus()
    elif(var11.get() == 0):
        txtPasta.configure(state = DISABLED)
        E_Pasta.set("0")

def chk_Samosa():
    if(var12.get() == 1):
        txtSamosa.configure(state = NORMAL)
        txtSamosa.delete('0',END)
        txtSamosa.focus()
    elif(var12.get() == 0):
        txtSamosa.configure(state = DISABLED)
        E_Samosa.set("0")

def chk_Sandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state = NORMAL)
        txtSandwich.delete('0',END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state = DISABLED)
        E_Sandwich.set("0")

def chk_Fires():
    if(var14.get() == 1):
        txtFires.configure(state = NORMAL)
        txtFires.delete('0',END)
        txtFires.focus()
    elif(var14.get() == 0):
        txtFires.configure(state = DISABLED)
        E_Fires.set("0")

def chk_chole():
    if(var15.get() == 1):
        txtchole.configure(state = NORMAL)
        txtchole.delete('0',END)
        txtchole.focus()
    elif(var15.get() == 0):
        txtchole.configure(state = DISABLED)
        E_chole.set("0")

def chk_Moomos():
    if(var16.get() == 1):
        txtMoomos.configure(state = NORMAL)
        txtMoomos.delete('0',END)
        txtMoomos.focus()
    elif(var16.get() == 0):
        txtMoomos.configure(state = DISABLED)
        E_Moomos.set("0")

##################################### Recipt functions #########################################

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + E_Sprite.get() +'\n')
    txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+ E_Pepsi.get()+'\n')
    txtReceipt.insert(END,'Coke:\t\t\t\t\t'+ E_Coke.get()+'\n')
    txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ E_Fanta.get()+'\n')
    txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(END,'Tea:\t\t\t\t\t'+ E_Tea.get()+'\n')
    txtReceipt.insert(END,'GingerTea:\t\t\t\t\t'+ E_GingerTea.get()+'\n')
    txtReceipt.insert(END,'ColdCoffee:\t\t\t\t\t'+ E_ColdCoffee.get()+'\n')
    txtReceipt.insert(END,'Noddels:\t\t\t\t\t'+ E_Noddels.get()+'\n')
    txtReceipt.insert(END,'Moomos:\t\t\t\t\t'+ E_Moomos.get()+'\n')
    txtReceipt.insert(END,'maggie:\t\t\t\t\t'+ E_Maggie.get()+'\n')
    txtReceipt.insert(END,'Pasta:\t\t\t\t\t'+ E_Pasta.get()+'\n')
    txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ E_Sandwich.get()+'\n')
    txtReceipt.insert(END,'Fires:\t\t\t\t\t'+ E_Fires.get()+'\n')
    txtReceipt.insert(END,'Samosa:\t\t\t\t\t'+ E_Samosa.get()+'\n')
    txtReceipt.insert(END,'Chole:\t\t\t\t\t'+ E_chole.get()+'\n')
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")

#################################################### check box Declearation ################################################

Sprite=Checkbutton(Drinks_F,text='Sprite',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk',command=chkSprite).grid(row=0,sticky=W)
Pepsi=Checkbutton(Drinks_F,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk',command=chkPepsi).grid(row=1,sticky=W)
Coke=Checkbutton(Drinks_F,text='Coke',variable=var3,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    bg='cornsilk',command=chk_Coke).grid(row=2,sticky=W)
Fanta=Checkbutton(Drinks_F,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    bg='cornsilk',command=chk_Fanta).grid(row=5,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='CocaCola',variable=var7,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    bg='cornsilk',command=chk_CocaCola).grid(row=6,sticky=W)
Tea=Checkbutton(Drinks_F,text='Tea',variable=var4,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    bg='cornsilk',command=chk_Tea).grid(row=3,sticky=W)
GingerTea=Checkbutton(Drinks_F,text='GingerTea',variable=var5,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    bg='cornsilk',command=chk_GingerTea).grid(row=4,sticky=W)
ColdCoffee=Checkbutton(Drinks_F,text='ColdCoffee',variable=var8,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    bg='cornsilk',command=chk_ColdCoffee).grid(row=7,sticky=W)

############################################# Entry Box decleratiom

txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=0,column=1)

txtPepsi = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=1,column=1)

txtCoke = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Coke)
txtCoke.grid(row=2,column=1)

txtFanta = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtTea= Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Tea)
txtTea.grid(row=3,column=1)

txtGingerTea = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_GingerTea)
txtGingerTea.grid(row=4,column=1)

txtColdCoffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_ColdCoffee)
txtColdCoffee.grid(row=7,column=1)

################################# For food check Box declaration #####################################

Noddels = Checkbutton(Food_F,text="Noddels\t\t\t ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Noddels).grid(row=0,sticky=W)
VegBurger = Checkbutton(Food_F,text="VegBurger",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Moomos).grid(row=1,sticky=W)
Maggie = Checkbutton(Food_F,text="maggie ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Maggie).grid(row=3,sticky=W)
Pasta = Checkbutton(Food_F,text="Pasta ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Pasta).grid(row=2,sticky=W)
Sandwich = Checkbutton(Food_F,text="Sandwich ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Sandwich).grid(row=4,sticky=W)
Fires = Checkbutton(Food_F,text="Fires ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Fires).grid(row=5,sticky=W)
Samosa = Checkbutton(Food_F,text="Samosa ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_Samosa).grid(row=6,sticky=W)
chole = Checkbutton(Food_F,text="chole",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk',command=chk_chole).grid(row=7,sticky=W)

###################################  For food Entry box ###################################### 

txtNoddels=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Noddels)
txtNoddels.grid(row=0,column=1)

txtMoomos=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Moomos)
txtMoomos.grid(row=1,column=1)

txtMaggie=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Maggie)
txtMaggie.grid(row=3,column=1)

txtPasta=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Pasta)
txtPasta.grid(row=2,column=1)

txtSandwich=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Sandwich)
txtSandwich.grid(row=4,column=1)

txtFires=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Fires)
txtFires.grid(row=5,column=1)

txtSamosa=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Samosa)
txtSamosa.grid(row=6,column=1)

txtchole=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_chole)
txtchole.grid(row=7,column=1)

##################################### labels decleration ##############################################

lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='cornsilk',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='cornsilk',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='cornsilk',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='cornsilk',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='cornsilk',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='cornsilk',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)

################################ Buttons declearation for Total, Recipt, Reset, Exit ##############################

btnTotal=Button(Bottons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='cornsilk',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Bottons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='cornsilk',command=Receipt).grid(row=0,column=1)
btnReset=Button(Bottons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='cornsilk',command=Reset).grid(row=0,column=2)
btnExit=Button(Bottons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='cornsilk',command=Exit).grid(row=0,column=3)

##############################  Creating Basic Calculater #############################################

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='cornsilk',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='cornsilk',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='cornsilk',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='cornsilk',command=lambda:btnClick('+')).grid(row=2,column=3)
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='cornsilk',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='cornsilk',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='cornsilk',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='cornsilk',command=lambda:btnClick('-')).grid(row=3,column=3)
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='cornsilk',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='cornsilk',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='cornsilk',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='cornsilk',command=lambda:btnClick('*')).grid(row=4,column=3)
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='cornsilk',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='cornsilk',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='cornsilk',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='cornsilk',command=lambda:btnClick('/')).grid(row=5,column=3)


root.mainloop()