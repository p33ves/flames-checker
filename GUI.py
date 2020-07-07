import tkinter as tk
import flames_checker

window = tk.Tk()
welcome = tk.Label(window, text="Check Flames!")
welcome.grid(row=0, column=1)


name1_label = tk.Label(window, text="Enter name of person1:")
name1_label.grid(row=1, column=0)
name1 = tk.Entry(window, width=50)
name1.grid(row=1, column=1)

name2_label = tk.Label(window, text="Enter name of person2:")
name2_label.grid(row=2, column=0)
name2 = tk.Entry(window, width=50)
name2.grid(row=2, column=1)


def run_checker():
    result = flames_checker.checker(name1.get(), name2.get())
    line_number = 4
    output_label = tk.Label(window, text=result)
    output_label.grid(row=line_number, column=1)


check_button = tk.Button(window, text="Calculate", command=run_checker)
check_button.grid(row=3, column=1)


window.mainloop()
