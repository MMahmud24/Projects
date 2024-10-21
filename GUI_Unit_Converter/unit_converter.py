import tkinter as tk

class Converter:
    def __init__(self, main):
        main.title("Unit Converter")
        main.geometry("300x360")
        main.resizable(False, False)

        self.input_label = tk.Label(main, text='Enter A Value:')
        self.input_label.grid(column=0, row=0)

        self.input_entry = tk.Entry(main)
        self.input_entry.grid(column=1, row=0)

        self.from_label = tk.Label(main, text='From')
        self.from_label.grid(column=0, row=1)

        self.from_val = tk.StringVar(main)
        self.from_val.set('meters')

        self.from_options = tk.OptionMenu(main, self.from_val, "meters", "kilometers", "centimeters")
        self.from_options.grid(column=1, row=1)

        self.to_label = tk.Label(main, text='To')
        self.to_label.grid(column=0, row=2)

        self.to_val = tk.StringVar(main)
        self.to_val.set('kilometers')

        self.to_options = tk.OptionMenu(main, self.to_val, "meters", "kilometers", "centimeters")
        self.to_options.grid(column=1, row=2)

        self.convert_button = tk.Button(main, text='Convert', command=self.convert)
        self.convert_button.grid(column=0, row=3)

        self.output_label = tk.Label(main, text="")
        self.output_label.grid(column=1, row=3)

    def convert(self):
        input_val = float(self.input_entry.get())
        from_unit = self.from_val.get()
        to_unit = self.to_val.get()

        # Convert input to meters first
        if from_unit == "centimeters":
            meters_value = input_val / 100
        elif from_unit == "kilometers":
            meters_value = input_val * 1000
        else:
            meters_value = input_val

        # Convert meters to the target unit
        if to_unit == "centimeters":
            output_value = meters_value * 100
        elif to_unit == "kilometers":
            output_value = meters_value / 1000
        else:
            output_value = meters_value

        self.output_label.config(text=str(output_value))


root = tk.Tk()
converter = Converter(root)
root.mainloop()
