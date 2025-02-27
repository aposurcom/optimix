import tkinter as tk
from tkinter import ttk
import func

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        # self.geometry("400x300")

        # Tkinter labels and input fields in 2 columns of product_A_material=4, product_B_material=2, material_max=60, product_A_labor=2, product_B_labor=3, labor_max=60
        self.lbl_product_A_material = ttk.Label(self, text="Product A Material:")
        self.lbl_product_A_material.grid(row=0, column=0, pady=5)
        self.product_A_material = ttk.Entry(self)
        self.product_A_material.grid(row=0, column=1, pady=5)

        self.lbl_product_B_material = ttk.Label(self, text="Product B Material:")
        self.lbl_product_B_material.grid(row=1, column=0, pady=5)
        self.product_B_material = ttk.Entry(self)
        self.product_B_material.grid(row=1, column=1, pady=5)

        self.lbl_material_max = ttk.Label(self, text="Material Max:")
        self.lbl_material_max.grid(row=2, column=0, pady=5)
        self.material_max = ttk.Entry(self)
        self.material_max.grid(row=2, column=1, pady=5)

        self.lbl_product_A_labor = ttk.Label(self, text="Product A Labor(h):")
        self.lbl_product_A_labor.grid(row=3, column=0, pady=5)
        self.product_A_labor = ttk.Entry(self)
        self.product_A_labor.grid(row=3, column=1, pady=5)

        self.lbl_product_B_labor = ttk.Label(self, text="Product B Labor(h):")
        self.lbl_product_B_labor.grid(row=4, column=0, pady=5)
        self.product_B_labor = ttk.Entry(self)
        self.product_B_labor.grid(row=4, column=1, pady=5)

        self.lbl_labor_max = ttk.Label(self, text="Labor Max(h):")
        self.lbl_labor_max.grid(row=5, column=0, pady=5)
        self.labor_max = ttk.Entry(self)
        self.labor_max.grid(row=5, column=1, pady=5)

        self.button = ttk.Button(self, text="Find answer", command=self.on_button_click)
        self.button.grid(row=6, column=0, columnspan=2, pady=5)

        self.lbl_result = ttk.Label(self, text="Instructions:\n1. Input required variables\n2. Press \"Find anwer\"!")
        self.lbl_result.grid(row=7, column=0, columnspan=2, pady=5)

    def on_button_click(self):
        # Check if all inputs are empty
        if self.product_A_material.get() == "" or self.product_B_material.get() == "" or self.material_max.get() == "" or self.product_A_labor.get() == "" or self.product_B_labor.get() == "" or self.labor_max.get() == "":
            # set default values
            self.product_A_material.insert(0, 4)
            self.product_B_material.insert(0, 2)
            self.material_max.insert(0, 60)
            self.product_A_labor.insert(0, 2)
            self.product_B_labor.insert(0, 3)
            self.labor_max.insert(0, 60)
            self.lbl_result.config(text="Default values are set.\n Please press \"Find answer\" again.")
            return
        
        # Check if input is a number
        try:
            product_A_material = int(self.product_A_material.get())
            product_B_material = int(self.product_B_material.get())
            material_max = int(self.material_max.get())
            product_A_labor = int(self.product_A_labor.get())
            product_B_labor = int(self.product_B_labor.get())
            labor_max = int(self.labor_max.get())
        except ValueError:
            self.lbl_result.config(text="Please input numbers only.")
            return

        # Check if one input is empty
        if self.product_A_material.get() == "" or self.product_B_material.get() == "" or self.material_max.get() == "" or self.product_A_labor.get() == "" or self.product_B_labor.get() == "" or self.labor_max.get() == "":
            self.lbl_result.config(text="Please input all required variables.")
            return
        # Call the function from func.py
        result = func.product_mix_optimization(
            product_A_material=int(self.product_A_material.get()),
            product_B_material=int(self.product_B_material.get()),
            material_max=int(self.material_max.get()),
            product_A_labor=int(self.product_A_labor.get()),
            product_B_labor=int(self.product_B_labor.get()),
            labor_max=int(self.labor_max.get())
        )
        self.lbl_result.config(text=result)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
