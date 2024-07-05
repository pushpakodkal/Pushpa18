import pandas as pd
from pandas._config import display
from sklearn import linear_model
from tkinter import *

df=pd.read_csv(r"C:\Users\rakesh kumar \OneDrive\Desktop\skill_lab\homeprice_banglore.csv")
x=df.drop(columns=['prices'])
y=df.drop(columns=['bedrooms','area','age'],axis='columns')


window=Tk()
window.title("HOUSE PRICES")
window.geometry("700x300+100+85")

srtlabel=Label(text=" kindly Enter your  sqrt requirements :",)
srtlabel.grid(column=0,row=0)
srt=Entry(width=40)
srt.grid(row=0,column=1)

bedlabel=Label(text=" kindly Enter the  beds requirements:")
bedlabel.grid(column=0,row=1)
bed=Entry(width=40)
bed.grid(column=1,row=1)

agelabel=Label(text=" kindly Enter the  age  :")
agelabel.grid(column=0,row=2)
age=Entry(width=40)
age.grid(row=2,column=1)

b1=Button(window,text="Find",width=9,height=2,fg="#HHHHHH",bg="#403F8F",command=lambda: find())
b1.grid(row=4,column=1)

display=Label(window,text=" ",width=120,height=4,fg="#HHHHHH",bg="#403F8F")
display.grid(row=6,column=0,columnspan=3)

model=linear_model.LinearRegression()
model.fit(x,y)

n=1
def find():
 global n
 while n==1:
    sqrt = int(srt.get())
    beds = int(bed.get())
    ages = int (age.get())
    amount=model.predict([[sqrt,beds,ages]])
    display.config(text=f"{"The Assessed Value for the House with",sqrt,"sqrt with",age,"years old house for RS:",float(amount[0][0])}")
    n+=1

window.mainloop()
