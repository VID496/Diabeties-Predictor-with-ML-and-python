#plese use it in pycharm for best Experience
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
df=pd.read_csv('/home/viditgupta234gc/Documents/datasets/diabetes-dataset.csv')#enter Your Dataset
X_train, X_test, y_train, y_test=train_test_split(df.drop('Outcome',axis=1),df.Outcome,random_state=42,stratify=df.Outcome)

model=DecisionTreeClassifier()
model.fit(X_train, y_train)



root=Tk()



inp1=tk.IntVar()

inp2=tk.IntVar()

inp3=tk.IntVar()

inp4=tk.IntVar()

inp5=tk.IntVar()

inp6=tk.IntVar()

inp7=tk.IntVar()

inp8=tk.IntVar()

inp9=tk.StringVar()


inp1_entry=Entry(root,textvariable=inp1).grid(rows=1,columns=1)

preg_label=Label(root,text='Enter your Pregnancies').grid(rows=1,columns=1)

inp2_entry=Entry(root,textvariable=inp2).grid(rows=1,columns=1)

Glucose_label=Label(root,text='Enter your Glucose').grid(rows=1,columns=1)

inp3_entry=Entry(root,textvariable=inp3).grid(rows=1,columns=1)

BloodPressure_label=Label(root,text='Enter your BloodPressure').grid(rows=1,columns=1)

inp4_entry=Entry(root,textvariable=inp4).grid(rows=1,columns=1)

SkinThickness_label=Label(root,text='Enter your SkinThickness').grid(rows=1,columns=1)

inp5_entry=Entry(root,textvariable=inp5).grid(rows=1,columns=1)

Insulin_label=Label(root,text='Enter your Insulin').grid(rows=1,columns=1)

inp6_entry=Entry(root,textvariable=inp6).grid(rows=1,columns=1)

BMI_label=Label(root,text='Enter your BMI').grid(rows=1,columns=1)

inp7_entry=Entry(root,textvariable=inp7).grid(rows=1,columns=1)

DiabetesPedigreeFunction_label=Label(root,text='Enter your DiabetesPedigreeFunction').grid(rows=1,columns=1)

inp8_entry=Entry(root,textvariable=inp8).grid(rows=1,columns=1)

Age_label=Label(root,text='Enter your Age').grid(rows=1,columns=1)

c = (inp1.get(), inp2.get(), inp3.get(), inp4.get(), inp5.get(), inp6.get(), inp7.get(), inp8.get())

Df = pd.DataFrame(c).T


def sub():
    c= (inp1.get(),inp2.get(),inp3.get(),inp4.get(),inp5.get(),inp6.get(),inp7.get(),inp8.get())
    Df=pd.DataFrame(c).T
    y_pred=model.predict(Df)
    if y_pred==1:
        Out_label = Label(root, text='Yes he/she is suffering from diabetes').grid(rows=1, columns=1)
        return print(Out_label)
    if y_pred==0:
        Out_label = Label(root, text='No he/she is not suffering from diabetes').grid(rows=1, columns=1)
        return print(Out_label)



sub_buton=Button(text="Submit",command=sub).grid()

root.title('diabetes prediction')
root.maxsize(250, 1000)
root.minsize(250,400)
root.geometry("250x400")
root.mainloop()


