import tkinter as tk
from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

root = tk.Tk()
root.attributes('-fullscreen',True)
root.geometry('1200x690+0+0')
root.title('WOW! Silog Menu')
root.config(bg = 'red')

OrderValues = [0,1,2,3,4,5,6,7,8,9,10]
i=1
j=1
k=1

Meals = {'Chixsilog':85.00,'Porksilog':85.00,'Torgisilog':85.00,'Spamsilog':85.00,'Bangsilog':85.00,
         'Hotsilog':65.00,'Tapsilog':75.00,'Sisiglog':75.00,'Tosilog':65.00,'Hamsilog':65.00}
MealOPmenu = dict()
MealVars = dict()

Drinks = {'Water':10.00,'Coke':18.00,'Royal':18.00,'Tea':20.00,'Coffee':20.00}
DrinksOPmenu = dict()
DrinksVars = dict()

Desserts = {'Ice Cream':35.00,'Leche Flan':45.00,'Maruya':55.00,'Cake':99.00}
DessertsOPmenu = dict()
DessertsVars = dict()

var1 = StringVar()
var1.set('')

varTax = StringVar()
varChange = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varPayment = IntVar()
varPaymentMethod = IntVar()
varCheckMethod = StringVar()


varTax.set('₱ 0.0')
varChange.set('₱ 0.0')
varSubTotal.set('₱ 0.0')
varTotal.set('₱ 0.0')
varPayment.set('')
varCheckMethod.set('₱ 0.0')


Tops = Frame(root, bg = 'goldenrod1', relief = GROOVE, bd = 15, pady = 4)
Tops.pack(side = TOP, fill = BOTH)

lblTitle = Label(Tops, font = ('Elephant',30,'bold'),
                 text = "Gal's Silog to GO!", bg = 'orange', justify = CENTER, fg = 'white')
lblTitle.pack(side = TOP, fill = BOTH)

def CheckMethod(q):
    cost = 0
    totalm = 0
    totaldk = 0
    totalds = 0
    cktotal = 0
    tax = 0

    for ml in Meals:
        totalm += float(Meals[ml] * MealVars[ml].get())
    for dnk in Drinks:
        totaldk += float(Drinks[dnk] * DrinksVars[dnk].get())
    for dsr in Desserts:
        totalds += float(Desserts[dsr] * DessertsVars[dsr].get())
    

    cost += float('%.2f' % (totalm + totaldk + totalds))
    tax += float('%.2f' % (cost * 3.4/ 100))    
    cktotal += float('%.2f' % (cost + tax))
    
    txtCheckMethod.config(state = NORMAL)
    txtCheckMethod.delete(0, END)
    txtCheckMethod.insert('0','₱ {0}'.format(cktotal))
    check = txtCheckMethod.get()
    txtCheckMethod.config(state = DISABLED)

    if check == '₱ 0.0':
            messagebox.showerror("Info","Please pick your order")
    
        
def iExit():
    qExit = tk.messagebox.askyesno("Silog list", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
    
def Reset():
    var1.set('Cash')
    varTax.set('₱ 0.0')
    varChange.set('₱ 0.0')
    varSubTotal.set('₱ 0.0')
    varTotal.set('₱ 0.0')
    varPayment.set('')
    varCheckMethod.set('₱ 0.0')

    for mlv in MealVars:
        MealVars[mlv].set(OrderValues[0])
    for dnkv in DrinksVars:
        DrinksVars[dnkv].set(OrderValues[0])
    for dsrv in DessertsVars:
        DessertsVars[dsrv].set(OrderValues[0])


def subTOTAL():
    try:
        m = float(varPayment.get())
        totalm = 0
        totaldk = 0
        totalds = 0
        cost = 0
        tax = 0
        change = 0
        total = 0
        check = 0

        for ml in Meals:
            totalm += float(Meals[ml] * MealVars[ml].get())
        for dnk in Drinks:
            totaldk += float(Drinks[dnk] * DrinksVars[dnk].get())
        for dsr in Desserts:
            totalds += float(Desserts[dsr] * DessertsVars[dsr].get())       

        cost += float('%.2f' % (totalm + totaldk + totalds))
        tax += float('%.2f' % (cost * 3.4/ 100))
        change += float('%.2f' % (m - (cost + tax)))
        total += float('%.2f' % (cost + tax))

        if cost == 0.0:
            messagebox.showerror("Info","Please pick your order")
        elif m <= cost:
            messagebox.showerror("Info","Your payment is not enough!")
        else:
            
            txtChange.config(state = NORMAL)
            txtChange.delete(0, END)
            txtChange.insert('0','₱ {0}'.format(change))
            txtChange.config(state = DISABLED)
            
            txtTotal.config(state = NORMAL)
            txtTotal.delete(0, END)
            txtTotal.insert('0','₱ {0}'.format(total))
            txtTotal.config(state = DISABLED)
            
            txtTax.config(state = NORMAL)
            txtTax.delete(0, END)
            txtTax.insert('0','₱ {0}'.format(tax))
            txtTax.config(state = DISABLED)
                     
            txtSubTotal.config(state = NORMAL)
            txtSubTotal.delete(0, END)
            txtSubTotal.insert('0','₱ {0}'.format(cost))
            txtSubTotal.config(state = DISABLED)

            txtCheckMethod.config(state = NORMAL)
            txtCheckMethod.delete(0, END)
            txtCheckMethod.insert('0','₱ {0}'.format(check))
            txtCheckMethod.config(state = DISABLED)
         
    except:
        messagebox.showerror("Invalid input! or Empty input!","Please input a payment by number, not space or letter")
    
    

#-------------------------------Payment---------------------------------
f0 = Frame (root, bd = 12, relief = RIDGE, bg = 'dodgerblue')
f0.pack(side = RIGHT, fill = BOTH, expand = True)

Payframe = Frame (f0, bd = 12, relief = SUNKEN, pady = 5)
Payframe.pack(side = RIGHT, fill = BOTH, expand = True)

lblPayment = Label(Payframe, font = ('Script MT Bold', 20,'bold'), text = 'Payment', anchor = N, width = 6,bg = 'lightgray')
lblPayment.pack(side = TOP, fill = X)

f0 = Frame (Payframe, bd = 10, relief = RAISED, pady = 5, bg = 'green3')
f0.pack(side = BOTTOM, fill = BOTH, expand = True)


btnTotal = Button (f0, padx = 14, pady = 1, activebackground ='goldenrod1', font = ('times new roman', 15, 'bold'), width = 4,
                   text = 'Total ',command = subTOTAL).pack(side = LEFT, fill = BOTH, expand = True)
btnExit = Button (f0, padx = 14, pady = 1, activebackground ='red', font = ('times new roman', 15, 'bold'), width = 4,
                   text = 'Exit ', command = lambda: iExit()).pack(side = RIGHT, fill = BOTH, expand = True)

btnReset = Button (f0, padx = 14, pady = 1, activebackground ='goldenrod1', font = ('times new roman', 15, 'bold'), width = 4,
                   text = 'Reset ', command = Reset).pack(side = RIGHT, fill = BOTH, expand = True)



#----------------------------------------------------------------------------------------
f0 = Frame (Payframe, bd = 10, relief = SUNKEN, pady = 5, bg = 'lightgreen')
f0.pack(side = BOTTOM, fill = BOTH, expand = True)

lblChange = Label(f0, font = ('times new roman', 18, 'bold'), text = 'Change' , anchor = W, bg = 'lightgreen')
lblChange.pack(expand = True)
txtChange = Entry (f0, font = ('times new roman', 18, 'bold'), textvariable = varChange, width = 15, state = DISABLED)
txtChange.pack(expand = True)

lblTax =  Label(f0, font = ('times new roman', 18, 'bold'), text = 'Tax',  anchor = W, bg = 'lightgreen')
lblTax.pack(expand = True)
txtTax = Entry (f0, font = ('times new roman', 18, 'bold'), textvariable = varTax, width = 15,  state = DISABLED)
txtTax.pack(expand = True)

lblSubTotal =  Label(f0, font = ('times new roman', 18, 'bold'), text = 'Sub Total', width = 15, bg = 'lightgreen')
lblSubTotal.pack(expand = True)
txtSubTotal = Entry (f0, font = ('times new roman', 18, 'bold'), textvariable = varSubTotal, width = 15, state = DISABLED)
txtSubTotal.pack(expand = True)

lblTotal =  Label(f0, font = ('times new roman', 18, 'bold'), text = 'Total', width = 15, bg = 'lightgreen')
lblTotal.pack(expand = True)
txtTotal = Entry (f0, font = ('times new roman', 18, 'bold'), textvariable = varTotal, width = 15, state = DISABLED)
txtTotal.pack(expand = True)

#---------------------------------------------------------------------------------------
f0 = Frame (Payframe, bd = 10, relief = RAISED, pady = 5, bg = 'green3')
f0.pack(side = BOTTOM, fill = BOTH, expand = True)

txtCheckMethod = Entry (f0, font = ('times new roman', 18, 'bold'), textvariable = varCheckMethod, width = 15,  state = DISABLED)
txtCheckMethod.pack(expand = True)

lblPaymentMethod = Label(f0, font = ('times new roman', 18, 'bold'), text = 'Payment Method', width = 15, bg = 'green3')
lblPaymentMethod.pack(expand = True)

txtPayment = Entry (f0, font = ('times new roman', 18, 'bold'), textvariable = varPayment, width = 15)
txtPayment.pack(expand = True)

cmbPaymentMethod = ttk.Combobox(f0, textvariable = var1, state = 'readonly', font = ('times new roman', 15, 'bold'), width = 14)
cmbPaymentMethod['value'] = ('Cash')
cmbPaymentMethod.current(0)
cmbPaymentMethod.pack(expand = True)


#------------------------------FRAME 1-------------------------------------
BottomMainFrame = Frame(root, relief = RIDGE, bd = 15, bg = 'red')
BottomMainFrame.pack(side = BOTTOM, fill = BOTH, expand = True)

f1 = Frame (BottomMainFrame,bd = 12, relief = SUNKEN, pady = 5)
f1.pack(side = LEFT, fill = BOTH, expand = True)

lblMeal = Label(f1, font = ('Script MT Bold', 20,'bold'), text = 'Meals', anchor = N, width = 25, bg = 'lightgray')
lblMeal.pack(side = TOP, fill = X)

MealsName = Frame(f1,borderwidth = 5,relief = SUNKEN)
MealsName.pack(side = LEFT, fill = BOTH, expand = True)

PricesFrameM = Frame(f1, borderwidth = 5,relief = SUNKEN)
PricesFrameM.pack(side = LEFT, fill = BOTH, expand = True)

Mcount = Frame(f1, borderwidth = 5, bg = 'goldenrod1', relief = SUNKEN)
Mcount.pack(side = RIGHT, fill = BOTH, expand = True)

for m in Meals:
    MealVars[m] = IntVar(Mcount)
    MealLabel = Label(MealsName, text = m, font = ('times new roman', 16, 'bold'),width = 10)
    MealLabel.pack(expand = True)
    PriceMeal = Label(PricesFrameM, text = ('₱{0}'.format(Meals[m])),font = ('times new roman', 16, 'bold'),width = 10)
    PriceMeal.pack(expand = True)
    MealOPmenu[m] = OptionMenu(Mcount, MealVars[m],*OrderValues, command = CheckMethod)
    MealOPmenu[m].config(font = ('times new roman',16,'bold'), bg = 'lightgray', activebackground ='coral')
    MealOPmenu[m].pack(expand = True)
    i+=1

#---------------------------FRAME 2---------------------------------------    
f2 = Frame(BottomMainFrame, bd = 12, relief = SUNKEN,pady = 5)
f2.pack(side = TOP, fill = BOTH, expand = True)

lblDrinks = Label(f2, font = ('Script MT Bold', 20,'bold'), text = 'Drinks', anchor = N, width = 25, bg = 'lightgray')
lblDrinks.pack(side = TOP, fill = X)

DrinksName = Frame(f2,borderwidth = 5,relief = SUNKEN)
DrinksName.pack(side = LEFT, fill = BOTH, expand = True)

PricesFrameDk = Frame(f2, borderwidth = 5,relief = SUNKEN)
PricesFrameDk.pack(side = LEFT, fill = BOTH, expand = True)

Dkcount = Frame(f2, borderwidth = 5, bg = 'goldenrod1', relief = SUNKEN)
Dkcount.pack(side = RIGHT, fill = BOTH, expand = True)

for dk in Drinks:
    DrinksVars[dk] = IntVar(Dkcount)
    DrinkLabel = Label(DrinksName, text = dk, font = ('times new roman', 16, 'bold'),width = 10)
    DrinkLabel.pack(expand = True)
    PriceDrink = Label(PricesFrameDk, text = ('₱{0}'.format(Drinks[dk])),font = ('times new roman', 16, 'bold'),width = 10)
    PriceDrink.pack(expand = True)
    DrinksOPmenu[dk] = OptionMenu(Dkcount,DrinksVars[dk],*OrderValues, command = CheckMethod)
    DrinksOPmenu[dk].config(font = ('times new roman',16,'bold'), bg = 'lightgray', activebackground ='coral')
    DrinksOPmenu[dk].pack(expand = True)
    j+=1


#--------------------------------FRAME 3 bottom--------------------------------
f3 = Frame(BottomMainFrame, bd = 12, relief = SUNKEN, pady = 5)
f3.pack(side = BOTTOM, fill = BOTH, expand = True)

lblDesserts = Label(f3, font = ('Script MT Bold', 20,'bold'), text = 'Desserts', anchor = N, width = 25, bg = 'lightgray')
lblDesserts.pack(side = TOP, fill = X)

DessertsName = Frame(f3,borderwidth = 5,relief = SUNKEN)
DessertsName.pack(side = LEFT, fill = BOTH, expand = True)

PricesFrameDs = Frame(f3, borderwidth = 5,relief = SUNKEN)
PricesFrameDs.pack(side = LEFT, fill = BOTH, expand = True)

Dscount = Frame(f3, borderwidth = 5, bg = 'goldenrod1', relief = SUNKEN)
Dscount.pack(side = RIGHT, fill = BOTH, expand = True)

for ds in Desserts:
    DessertsVars[ds] = IntVar(Dscount)
    DessertsLabel = Label(DessertsName, text = ds, font = ('times new roman', 16, 'bold'),width = 10)
    DessertsLabel.pack(expand = True)
    PriceDesserts = Label(PricesFrameDs, text = ('₱{0}'.format(Desserts[ds])),font = ('times new roman', 16, 'bold'),width = 10)
    PriceDesserts.pack(expand = True)
    DessertsOPmenu[ds] = OptionMenu(Dscount, DessertsVars[ds],*OrderValues, command = CheckMethod)
    DessertsOPmenu[ds].config(font = ('times new roman',16,'bold'), bg = 'lightgray', activebackground ='coral')
    DessertsOPmenu[ds].pack(expand = True)
    k+=1

root.mainloop()
