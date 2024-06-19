import tkinter as tk
from tkinter import messagebox
def body_mass_index():
  
 weight=float(input("ENTER THE WEIGHT IN KG :"))
 height=float(input("ENTER THE HEIGHT IN METER :"))
 sq=height*height                   
 bmi=weight/sq
 result.set(f"BMI IS :{bmi:,2f}")
 if bmi <= 18.4:
    message=" YOU LIE IN THE CATEGORY OF UNDERWEIGHT"
 elif bmi<=24.9:
    message="YOU LIE IN THE CATEGORY OF NORMAL"
 elif bmi>25.0:
    message="YOU LIE IN THE CATEGORY OF OVERWEIGHT"
 message.showinfo("Bmi result:,f{result.get()}\n{message}" )
root=tk.Tk()
root.title("bmi calculator")
result=tk.StringVar()
tk.Label(root,text="Weight(kg):").grid(row=0,column=0,padx=10,pady=10)
entry_weight=tk.Entry(root)
entry_weight.grid(row=0,column=1,padx=10,pady=10)

tk.Label(root,text="Height(M):").grid(row=1,column=0,padx=10,pady=10)
entry_height=tk.Entry(root)
entry_height.grid(row=1,column=1,padx=10,pady=10)

calculate_button=tk.Button(root,text="Calculate BMI",command=body_mass_index)
calculate_button.grid(row=2,column=0,columnspan=2,pady=20)

tk.Label(root,textvariable=result).grid(row=3,column=0,columnspan=2,pady=10)

root.mainloop()
