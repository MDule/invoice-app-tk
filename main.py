"""
Tkinter based invoice software used  for storing invoices in DB and creating PDF
invoices.

Author: Dušan Miletić
Date: Avgust, 2022
"""

import tkinter as tk
from tkinter import ttk

# from tkinter import filedialog as fd ## for logo filedialog


class App(tk.Tk):
    """Main app window (root) class. For object creation, the following is needed:

    title: str - Title that appears on the top window bar;
    size: tuple(int, int) - Values for window size in width, height manner."""

    def __init__(self, title: str, size: tuple[int, int]):
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # widgets
        self.sidebar = Sidebar(self)
        self.settings = Settings(self)

        # define commands for buttons
        self.sidebar.btn_quit.configure(command=lambda: self.settings.destroy())
        self.sidebar.btn_settings.configure(
            command=lambda: self.settings.__init__(self)
        )

        # run
        self.mainloop()


class Sidebar(ttk.Frame):
    """Sidebar menu on the left. Requrest master as parameter."""

    def __init__(self, master):
        super().__init__(master)
        # sidebar occupies 20% of the window width
        self.place(x=5, y=5, relwidth=0.2, relheight=1)

        # create widgets
        self.create_widgets()
        # place widgets in window
        self.create_layout()

    def create_widgets(self):
        """Create sidebar widgets. Does not place them in the window. To place
        widgets, call create_layout() method."""

        self.btn_invoice_new = ttk.Button(self, text="Nova faktura")
        self.btn_invoice_review = ttk.Button(self, text="Pregled faktura")
        self.btn_customers = ttk.Button(self, text="Komitenti")
        self.btn_settings = ttk.Button(self, text="Podešavanja")
        self.btn_quit = ttk.Button(self, text="Izlaz")

    def create_layout(self):
        """Places created widgets in the window (from the create_widgets() method)."""

        self.btn_invoice_new.pack(fill="both")
        self.btn_invoice_review.pack(fill="both")
        self.btn_customers.pack(fill="both")
        self.btn_settings.pack(fill="both")
        self.btn_quit.pack(fill="both")


class Settings(ttk.Frame):
    """Settings window. Requiers master as parameter."""

    def __init__(self, master):
        super().__init__(master)
        # sidebar occupies 200px of the window width
        # self.place(relx=0.225, y=5, relwidth=0.75, relheight=0.95)
        self.place(relx=0.225, y=5, relwidth=0.75)

        # create widgets
        self.create_widgets()
        # place widgets in window
        self.create_layout()

    def create_widgets(self):
        """Create sidebar widgets. Does not place them in the window. To place
        widgets, call create_layout() method."""

        # company name
        self.l_company_name = ttk.Label(self, text="Naziv firme:", anchor="center")
        self.e_company_name = ttk.Entry(self)
        # address
        self.l_company_address = ttk.Label(self, text="Adresa firme:", anchor="center")
        self.e_company_address = ttk.Entry(self)
        # city
        self.l_company_city = ttk.Label(self, text="Grad:", anchor="center")
        self.e_company_city = ttk.Entry(self)
        # e-mail
        self.l_company_email = ttk.Label(self, text="E-mail adresa:", anchor="center")
        self.e_company_email = ttk.Entry(self)
        # company id
        self.l_company_id = ttk.Label(self, text="Matični broj:", anchor="center")
        self.e_company_id = ttk.Entry(self)
        # company vat no
        self.l_company_vat_no = ttk.Label(self, text="PIB:", anchor="center")
        self.e_company_vat_no = ttk.Entry(self)
        # vat system user
        self.l_company_vat = ttk.Label(self, text="U sistemu PDV-a:", anchor="center")
        self.e_company_vat = ttk.Combobox(self, values=["Ne", "Da"])
        # bank name
        self.l_company_bank_name = ttk.Label(self, text="Banka:", anchor="center")
        self.e_company_bank_name = ttk.Entry(self)
        # bank account number RSD
        self.l_company_bank_rsd = ttk.Label(
            self, text="Broj TR (RSD):", anchor="center"
        )
        self.e_company_bank_rsd = ttk.Entry(self)
        # bank account number EUR
        self.l_company_bank_eur = ttk.Label(
            self, text="Broj TR (EUR):", anchor="center"
        )
        self.e_company_bank_eur = ttk.Entry(self)
        # company logo
        self.l_company_logo = ttk.Label(self, text="Logo:", anchor="center")
        self.btn_company_logo = ttk.Button(self, text="Odaberi fajl..")
        self.l_company_logo_message = ttk.Label(
            self, text="Ovde putanja", anchor="center"
        )
        # save button
        self.btn_save_settings = ttk.Button(self, text="Sačuvaj")
        self.l_save_settings = ttk.Label(self, text="uspešno sačuvano", anchor="center")

    def create_layout(self):
        """Places created widgets in the window (from the create_widgets() method)."""

        # 2 columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=20)
        # 14 rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)
        self.rowconfigure(12, weight=1)
        self.rowconfigure(13, weight=1)

        # GRID
        # company name
        self.l_company_name.grid(row=0, column=0, sticky="ew", pady=2)
        self.e_company_name.grid(row=0, column=1, sticky="ew", pady=2)
        # company address
        self.l_company_address.grid(row=1, column=0, sticky="ew", pady=2)
        self.e_company_address.grid(row=1, column=1, sticky="ew", pady=2)
        # city
        self.l_company_city.grid(row=2, column=0, sticky="ew", pady=2)
        self.e_company_city.grid(row=2, column=1, sticky="ew", pady=2)
        # email
        self.l_company_email.grid(row=3, column=0, sticky="ew", pady=2)
        self.e_company_email.grid(row=3, column=1, sticky="ew", pady=2)
        # company ID
        self.l_company_id.grid(row=4, column=0, sticky="ew", pady=2)
        self.e_company_id.grid(row=4, column=1, sticky="ew", pady=2)
        # company vat no
        self.l_company_vat_no.grid(row=5, column=0, sticky="ew", pady=2)
        self.e_company_vat_no.grid(row=5, column=1, sticky="ew", pady=2)
        # vat system user
        self.l_company_vat.grid(row=6, column=0, sticky="ew", pady=2)
        self.e_company_vat.grid(row=6, column=1, sticky="w", pady=2)
        # bank name
        self.l_company_bank_name.grid(row=7, column=0, sticky="ew", pady=2)
        self.e_company_bank_name.grid(row=7, column=1, sticky="ew", pady=2)
        # bank account number RSD
        self.l_company_bank_rsd.grid(row=8, column=0, sticky="ew", pady=2)
        self.e_company_bank_rsd.grid(row=8, column=1, sticky="ew", pady=2)
        # bank account number EUR
        self.l_company_bank_eur.grid(row=9, column=0, sticky="ew", pady=2)
        self.e_company_bank_eur.grid(row=9, column=1, sticky="ew", pady=2)
        # company logo
        self.l_company_logo.grid(row=10, column=0, sticky="ew", pady=2)
        self.btn_company_logo.grid(row=10, column=1, sticky="ew", pady=2)
        self.l_company_logo_message.grid(row=11, column=1, sticky="ew", pady=2)
        # save button
        self.btn_save_settings.grid(row=12, column=1, pady=10)
        self.l_save_settings.grid(row=13, column=1)


if __name__ == "__main__":
    # App("title", (960, 720))
    # App("title", (960, 300))
    App("title", (600, 350))
