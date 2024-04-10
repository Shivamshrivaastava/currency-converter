import tkinter as tk
from tkinter import ttk

class CurrencyConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Currency Converter')
        self.geometry('500x300')

        # Define currency lists and exchange rates
        self.currencies_list = ['United States Dollar', 'Pound Sterling', 'Euro', 'Indian Rupee', 'Swiss Franc', 'Japanese Yen']
        self.usd_to_other_list = [1, 0.72, 0.85, 83.36, 0.94, 110.70]

        # Create input fields and comboboxes
        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.from_entry_variable = tk.IntVar()
        self.to_entry_variable = tk.IntVar()

        self.from_entry = ttk.Entry(self, textvariable=self.from_entry_variable, width=40)
        self.from_combobox = ttk.Combobox(self, textvariable=self.from_currency, values=tuple(self.currencies_list), state='readonly')
        self.from_combobox.set(self.currencies_list[0])

        self.to_entry = ttk.Entry(self, textvariable=self.to_entry_variable, width=40, state='readonly')
        self.to_combobox = ttk.Combobox(self, textvariable=self.to_currency, values=tuple(self.currencies_list), state='readonly')
        self.to_combobox.set(self.currencies_list[4])

        self.from_entry.pack()
        self.from_combobox.pack()
        self.to_entry.pack()
        self.to_combobox.pack()

        # Bind events to currency converter function
        self.from_entry.bind('<KeyPress>', self.currency_converter)
        self.from_entry.bind('<KeyRelease>', self.currency_converter)

    def currency_converter(self, event):
        try:
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            amount = int(self.from_entry_variable.get())

            if from_currency == 'United States Dollar':
                converted = amount * self.usd_to_other_list[self.currencies_list.index(to_currency)]
                self.to_entry_variable.set(value=f'{converted:.2f}')
        except ValueError:
            # Handle non-numeric input
            self.to_entry_variable.set(value='Invalid input')

if __name__ == '__main__':
    app = CurrencyConverter()
    app.mainloop()
