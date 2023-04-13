"""
Layout file - contains layout of invoice app.

Contains following classes (layouts):
    - Sidebar
    - Invoices
    - Review Invoices
    - Customers
    - Settings

Every class has following functions:
    - __init__() - initialize and place part of layout(sidebar, settings, etc.)
    - create_widgets() - creates widgets for the class
    - create_layout() - creates layout for the class (placement using pack, grid,...)
"""
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry as ttkDateEntry


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

        # pyxl logo
        self.pyxl_img = tk.PhotoImage(file="static/pyxl-med-logo-150x57.png")
        self.l_pyxl_img = ttk.Label(self, image=self.pyxl_img, anchor="center")

    def create_layout(self):
        """Places created widgets in the window (from the create_widgets() method)."""

        self.btn_invoice_new.pack(fill="both")
        self.btn_invoice_review.pack(fill="both")
        self.btn_customers.pack(fill="both")
        self.btn_settings.pack(fill="both")
        self.btn_quit.pack(fill="both")
        self.l_pyxl_img.pack(fill="both", pady=25)


class Invoices(ttk.Frame):
    """Invoices window. Requires master as parameter."""

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
        """Create widgets in Review Invoices window. Does not place them in the window. To place
        widgets, call create_layout() method."""

        # customer in db
        self.l_customer_in_db = ttk.Label(
            self, text="Komitent je u bazi:", anchor="center"
        )
        self.combo_customer_in_db = ttk.Combobox(
            self,
            values=["Ne", "Da"],
        )

        # search db for customer
        self.l_customer_search_db = ttk.Label(self, text="Pretraži:", anchor="center")
        self.e_customer_search_db = ttk.Entry(self)

        # search results
        self.customer_search_db_results = ttk.Treeview(
            self, columns=["no", "name", "id_no", "tax_id"], show="headings", height=5
        )

        self.customer_search_db_results.heading("no", text="R.br.")
        self.customer_search_db_results.column(
            "no", minwidth=0, width=35, stretch=False
        )

        self.customer_search_db_results.heading("name", text="IME/NAZIV")

        self.customer_search_db_results.heading("id_no", text="MB")
        self.customer_search_db_results.column(
            "id_no", minwidth=0, width=100, stretch=False
        )

        self.customer_search_db_results.heading("tax_id", text="PIB")
        self.customer_search_db_results.column(
            "tax_id", minwidth=0, width=100, stretch=False
        )

        # button choose customer
        self.btn_select_customer_from_db = ttk.Button(self, text="Izaberi")

        # invoice id
        self.l_invoice_id = ttk.Label(self, text="Broj fakture:", anchor="center")
        self.e_invoice_id = ttk.Entry(self)

        # check last used invoice id
        self.l_invoice_id_check = ttk.Label(
            self, text="Poslednji broj fakture", anchor="center"
        )

        # invoice dates
        self.l_invoice_date = ttk.Label(self, text="Datum fakture:", anchor="center")
        self.e_invoice_date = ttkDateEntry(self, date_pattern="dd/MM/yyyy")

        # date of purchase
        self.l_invoice_date_of_purchase = ttk.Label(
            self, text="Datum prometa:", anchor="center"
        )
        self.e_invoice_date_of_purchase = ttkDateEntry(self, date_pattern="dd/MM/yyyy")

        # place of purchase
        self.l_invoice_place_of_purchase = ttk.Label(
            self, text="Mesto prometa:", anchor="center"
        )
        self.e_invoice_place_of_purchase = ttk.Entry(self)

        # customer
        self.l_customer_name = ttk.Label(self, text="Komitent:", anchor="center")
        self.e_customer_name = ttk.Entry(self)

        # customer address
        self.l_customer_address = ttk.Label(self, text="Adresa:", anchor="center")
        self.e_customer_address = ttk.Entry(self)

        # customer city
        self.l_customer_city = ttk.Label(self, text="Grad:", anchor="center")
        self.e_customer_city = ttk.Entry(self)

        # customer id no
        self.l_customer_id_no = ttk.Label(self, text="MB:", anchor="center")
        self.e_customer_id_no = ttk.Entry(self)

        # customer tax id
        self.l_customer_tax_id = ttk.Label(self, text="PIB:", anchor="center")
        self.e_customer_tax_id = ttk.Entry(self)

        # customer email
        self.l_customer_email = ttk.Label(self, text="E-mail:", anchor="center")
        self.e_customer_email = ttk.Entry(self)

        # option to save customer in db
        self.btn_customer_save_in_db = ttk.Button(self, text="Sačuvaj komitenta")

        # type of service
        self.l_type_of_service = ttk.Label(self, text="Vrsta usluge:", anchor="center")
        self.e_type_of_service = ttk.Entry(self)

        # unit of service
        self.l_unit_of_service = ttk.Label(self, text="Jedinica:", anchor="center")
        self.e_unit_of_service = ttk.Entry(self)

        # quantity
        self.l_quantity_of_service = ttk.Label(self, text="Količina:", anchor="center")
        self.e_quantity_of_service = ttk.Entry(self)

        # price without VAT
        self.l_price_of_service = ttk.Label(
            self, text="Cena bez PDV-a:", anchor="center"
        )
        self.e_price_of_service = ttk.Entry(self)

        # add service
        self.btn_add_service = ttk.Button(self, text="Dodaj stavku")

        # list of services
        self.list_of_services = ttk.Treeview(
            self,
            columns=[
                "no",
                "type_of_service",
                "unit",
                "quantity",
                "price",
                "vat",
                "total",
            ],
            show="headings",
        )
        self.list_of_services.heading("no", text="R.br.")
        self.list_of_services.column("no", minwidth=0, width=35, stretch=False)

        self.list_of_services.heading("type_of_service", text="VRSTA USLUGE")

        self.list_of_services.heading("unit", text="JEDINICA")
        self.list_of_services.column("unit", minwidth=0, width=65, stretch=False)

        self.list_of_services.heading("quantity", text="KOLIČINA")
        self.list_of_services.column("quantity", minwidth=0, width=65, stretch=False)

        self.list_of_services.heading("price", text="CENA BEZ PDVa")
        self.list_of_services.column("price", minwidth=0, width=100, stretch=False)

        self.list_of_services.heading("vat", text="PDV")
        self.list_of_services.column("vat", minwidth=0, width=80, stretch=False)

        self.list_of_services.heading("total", text="UKUPNO")
        self.list_of_services.column("total", minwidth=0, width=120, stretch=False)

        # total amount of services
        self.l_total_amount = ttk.Label(self, text="UKUPNO:", anchor="center")
        self.l_total_amount_var = ttk.Label(self, text="999.99", anchor="center")

        # description
        self.l_desc = ttk.Label(self, text="Komentar/opis usluge:", anchor="center")
        self.e_desc = tk.Text(self, height=4, font=("Segoe UI", 9))

        # buttons save and print
        self.btn_invoice_save_db = ttk.Button(self, text="Sačuvaj fakturu (baza)")
        self.btn_invoice_save_pdf = ttk.Button(self, text="Sačuvaj fakturu (PDF)")
        self.btn_invoice_print = ttk.Button(self, text="Štampaj fakturu")

    def create_layout(self):
        """Places created widgets in the window (from the create_widgets() method)."""

        # 6 columns
        for _ in range(6):
            self.columnconfigure(_, weight=1)

        # 16 rows
        for _ in range(18):
            self.rowconfigure(_, weight=1)

        # GRID
        # customer in base
        self.l_customer_in_db.grid(row=0, column=0, sticky="ew", pady=2)
        self.combo_customer_in_db.grid(row=0, column=1, sticky="ew", pady=2)

        # search
        self.l_customer_search_db.grid(row=1, column=0, sticky="ew", pady=2)
        self.e_customer_search_db.grid(
            row=1, column=1, columnspan=5, sticky="ew", pady=2
        )

        # search results
        self.customer_search_db_results.grid(
            row=2, column=0, columnspan=6, sticky="ew", pady=5
        )
        self.btn_select_customer_from_db.grid(
            row=3, column=5, sticky="ew", pady=(5, 15)
        )

        # invoice id
        self.l_invoice_id.grid(row=4, column=0, sticky="", pady=2)
        self.e_invoice_id.grid(row=4, column=1, sticky="ew", pady=2)
        self.l_invoice_id_check.grid(
            row=4, column=2, columnspan=4, sticky="w", pady=2, ipadx=5
        )

        # invoice date
        self.l_invoice_date.grid(row=5, column=0, sticky="ew", pady=(2, 30))
        self.e_invoice_date.grid(row=5, column=1, sticky="ew", pady=(2, 30))

        # date of purchase
        self.l_invoice_date_of_purchase.grid(
            row=5, column=2, sticky="ew", pady=(2, 30), ipadx=5
        )
        self.e_invoice_date_of_purchase.grid(row=5, column=3, sticky="ew", pady=(2, 30))

        # place of purchase (city)
        self.l_invoice_place_of_purchase.grid(
            row=5, column=4, sticky="ew", pady=(2, 30)
        )
        self.e_invoice_place_of_purchase.grid(
            row=5, column=5, sticky="ew", pady=(2, 30)
        )

        # customer
        self.l_customer_name.grid(row=6, column=0, sticky="ew", pady=2)
        self.e_customer_name.grid(row=6, column=1, columnspan=5, sticky="ew", pady=2)

        # customer address
        self.l_customer_address.grid(row=7, column=0, sticky="ew", pady=2)
        self.e_customer_address.grid(row=7, column=1, columnspan=3, sticky="ew", pady=2)

        # customer city
        self.l_customer_city.grid(row=7, column=4, sticky="ew", pady=2)
        self.e_customer_city.grid(row=7, column=5, sticky="ew", pady=2)

        # customer id no
        self.l_customer_id_no.grid(row=8, column=0, sticky="ew", pady=2)
        self.e_customer_id_no.grid(row=8, column=1, sticky="ew", pady=2)

        # customer tax id
        self.l_customer_tax_id.grid(row=8, column=2, sticky="ew", pady=2)
        self.e_customer_tax_id.grid(row=8, column=3, sticky="ew", pady=2)

        # customer email
        self.l_customer_email.grid(row=8, column=4, sticky="ew", pady=2)
        self.e_customer_email.grid(row=8, column=5, sticky="ew", pady=2)

        # button to save customer in db
        self.btn_customer_save_in_db.grid(
            row=9, column=4, columnspan=2, sticky="ew", pady=(2, 30)
        )

        # type of service
        self.l_type_of_service.grid(row=10, column=0, sticky="ew", pady=2)
        self.e_type_of_service.grid(row=10, column=1, columnspan=5, sticky="ew", pady=2)

        # unit of service
        self.l_unit_of_service.grid(row=11, column=0, sticky="ew", pady=2)
        self.e_unit_of_service.grid(row=11, column=1, sticky="ew", pady=2)

        # quantity
        self.l_quantity_of_service.grid(row=11, column=2, sticky="ew", pady=2)
        self.e_quantity_of_service.grid(row=11, column=3, sticky="ew", pady=2)

        # price without VAT
        self.l_price_of_service.grid(row=11, column=4, sticky="ew", pady=2)
        self.e_price_of_service.grid(row=11, column=5, sticky="ew", pady=2)

        # add service button
        self.btn_add_service.grid(row=12, column=5, sticky="ew", pady=2)

        # list of service
        self.list_of_services.grid(
            row=13, column=0, columnspan=6, sticky="ew", pady=(20, 0)
        )

        # total amount of services
        self.l_total_amount.grid(row=14, column=4, sticky="e", pady=2)
        self.l_total_amount_var.grid(row=14, column=5, sticky="ew", pady=2)

        # description
        self.l_desc.grid(row=15, column=0, columnspan=2, sticky="w", pady=2)
        self.e_desc.grid(row=16, column=0, columnspan=6, sticky="ew", pady=2)

        # buttons save and print
        self.btn_invoice_save_db.grid(row=17, column=3, sticky="ew", pady=10, ipadx=3)
        self.btn_invoice_save_pdf.grid(row=17, column=4, sticky="ew", pady=10, ipadx=3)
        self.btn_invoice_print.grid(row=17, column=5, sticky="ew", pady=10)


class ReviewInvoices(ttk.Frame):
    """Review invoices window. Requiers master as parameter."""

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
        """Create widgets in Review Invoices window. Does not place them in the window. To place
        widgets, call create_layout() method."""

        # search for invoices by name, invoice id, date -disabled by default
        self.l_search = ttk.Label(self, text="Pretraži:", anchor="center")
        self.e_search = ttk.Entry(self)

        # search results
        self.search_results = ttk.Treeview(
            self,
            columns=["id", "name", "invoice_id", "invoice_date", "invoice_amount"],
            show="headings",
        )
        self.search_results.heading("id", text="ID")
        self.search_results.column("id", minwidth=0, width=40, stretch=False)

        self.search_results.heading("name", text="IME/NAZIV")

        self.search_results.heading("invoice_id", text="BROJ FAKTURE")
        self.search_results.column("invoice_id", minwidth=0, width=120, stretch=False)

        self.search_results.heading("invoice_date", text="DATUM FAKTURE")
        self.search_results.column("invoice_date", minwidth=0, width=120, stretch=False)

        self.search_results.heading("invoice_amount", text="IZNOS")
        self.search_results.column(
            "invoice_amount", minwidth=0, width=120, stretch=False
        )

        # buttons
        self.btn_invoice_edit = ttk.Button(self, text="Prikaži ili izmeni")
        self.btn_invoice_delete = ttk.Button(self, text="Obriši")

        # invoice id
        self.l_invoice_id = ttk.Label(self, text="Broj fakture:", anchor="center")
        self.e_invoice_id = ttk.Entry(self)

        # check last used invoice id
        self.l_invoice_id_check = ttk.Label(
            self, text="Poslednji broj fakture", anchor="center"
        )

        # invoice dates
        self.l_invoice_date = ttk.Label(self, text="Datum fakture:", anchor="center")
        self.e_invoice_date = ttkDateEntry(self, date_pattern="dd/MM/yyyy")

        # date of purchase
        self.l_invoice_date_of_purchase = ttk.Label(
            self, text="Datum prometa:", anchor="center"
        )
        self.e_invoice_date_of_purchase = ttkDateEntry(self, date_pattern="dd/MM/yyyy")

        # place of purchase
        self.l_invoice_place_of_purchase = ttk.Label(
            self, text="Mesto prometa:", anchor="center"
        )
        self.e_invoice_place_of_purchase = ttk.Entry(self)

        # customer
        self.l_customer_name = ttk.Label(self, text="Komitent:", anchor="center")
        self.e_customer_name = ttk.Entry(self)

        # customer address
        self.l_customer_address = ttk.Label(self, text="Adresa:", anchor="center")
        self.e_customer_address = ttk.Entry(self)

        # customer city
        self.l_customer_city = ttk.Label(self, text="Grad:", anchor="center")
        self.e_customer_city = ttk.Entry(self)

        # customer id no
        self.l_customer_id_no = ttk.Label(self, text="MB:", anchor="center")
        self.e_customer_id_no = ttk.Entry(self)

        # customer tax id
        self.l_customer_tax_id = ttk.Label(self, text="PIB:", anchor="center")
        self.e_customer_tax_id = ttk.Entry(self)

        # customer email
        self.l_customer_email = ttk.Label(self, text="E-mail:", anchor="center")
        self.e_customer_email = ttk.Entry(self)

        # type of service
        self.l_type_of_service = ttk.Label(self, text="Vrsta usluge:", anchor="center")
        self.e_type_of_service = ttk.Entry(self)

        # unit of service
        self.l_unit_of_service = ttk.Label(self, text="Jedinica:", anchor="center")
        self.e_unit_of_service = ttk.Entry(self)

        # quantity
        self.l_quantity_of_service = ttk.Label(self, text="Količina:", anchor="center")
        self.e_quantity_of_service = ttk.Entry(self)

        # price without VAT
        self.l_price_of_service = ttk.Label(
            self, text="Cena bez PDV-a:", anchor="center"
        )
        self.e_price_of_service = ttk.Entry(self)

        # add service
        self.btn_add_service = ttk.Button(self, text="Dodaj stavku")

        # list of services
        self.list_of_services = ttk.Treeview(
            self,
            columns=[
                "no",
                "type_of_service",
                "unit",
                "quantity",
                "price",
                "vat",
                "total",
            ],
            show="headings",
        )
        self.list_of_services.heading("no", text="R.br.")
        self.list_of_services.column("no", minwidth=0, width=35, stretch=False)

        self.list_of_services.heading("type_of_service", text="VRSTA USLUGE")

        self.list_of_services.heading("unit", text="JEDINICA")
        self.list_of_services.column("unit", minwidth=0, width=65, stretch=False)

        self.list_of_services.heading("quantity", text="KOLIČINA")
        self.list_of_services.column("quantity", minwidth=0, width=65, stretch=False)

        self.list_of_services.heading("price", text="CENA BEZ PDVa")
        self.list_of_services.column("price", minwidth=0, width=100, stretch=False)

        self.list_of_services.heading("vat", text="PDV")
        self.list_of_services.column("vat", minwidth=0, width=80, stretch=False)

        self.list_of_services.heading("total", text="UKUPNO")
        self.list_of_services.column("total", minwidth=0, width=120, stretch=False)

        # total amount of services
        self.l_total_amount = ttk.Label(self, text="UKUPNO:", anchor="center")
        self.l_total_amount_var = ttk.Label(self, text="999.99", anchor="center")

        # description
        self.l_desc = ttk.Label(self, text="Komentar/opis usluge:", anchor="center")
        self.e_desc = tk.Text(self, height=4, font=("Segoe UI", 9))

        # buttons save and print
        self.btn_invoice_save_db = ttk.Button(self, text="Sačuvaj fakturu (baza)")
        self.btn_invoice_save_pdf = ttk.Button(self, text="Sačuvaj fakturu (PDF)")
        self.btn_invoice_print = ttk.Button(self, text="Štampaj fakturu")

    def create_layout(self):
        """Places created widgets in the window (from the create_widgets() method)."""

        # 6 columns
        for _ in range(6):
            self.columnconfigure(_, weight=1)

        # 16 rows
        for _ in range(16):
            self.rowconfigure(_, weight=1)

        # GRID
        # search entry
        self.l_search.grid(row=0, column=0, sticky="ew", pady=(5, 3))
        self.e_search.grid(row=0, column=1, columnspan=5, sticky="ew", pady=(5, 3))

        # search results
        self.search_results.grid(row=1, column=0, columnspan=6, sticky="ew")

        # buttons - edit or delete
        self.btn_invoice_edit.grid(row=2, column=4, sticky="ew", pady=(3, 15))
        self.btn_invoice_delete.grid(row=2, column=5, sticky="ew", pady=(3, 15))

        # invoice id
        self.l_invoice_id.grid(row=3, column=0, sticky="", pady=2)
        self.e_invoice_id.grid(row=3, column=1, sticky="", pady=2)
        self.l_invoice_id_check.grid(
            row=3, column=2, columnspan=4, sticky="w", pady=2, ipadx=5
        )

        # invoice date
        self.l_invoice_date.grid(row=4, column=0, sticky="ew", pady=2)
        self.e_invoice_date.grid(row=4, column=1, sticky="ew", pady=2)

        # date of purchase
        self.l_invoice_date_of_purchase.grid(row=4, column=2, sticky="ew", pady=2)
        self.e_invoice_date_of_purchase.grid(row=4, column=3, sticky="ew", pady=2)

        # place of purchase
        self.l_invoice_place_of_purchase.grid(row=4, column=4, sticky="ew", pady=2)
        self.e_invoice_place_of_purchase.grid(
            row=4, column=5, columnspan=2, sticky="ew", pady=2
        )

        # customer
        self.l_customer_name.grid(row=5, column=0, sticky="ew", pady=(20, 2))
        self.e_customer_name.grid(
            row=5, column=1, columnspan=5, sticky="ew", pady=(20, 2)
        )

        # customer address
        self.l_customer_address.grid(row=6, column=0, sticky="ew", pady=2)
        self.e_customer_address.grid(row=6, column=1, columnspan=3, sticky="ew", pady=2)

        # customer city
        self.l_customer_city.grid(row=6, column=4, sticky="ew", pady=2)
        self.e_customer_city.grid(row=6, column=5, sticky="ew", pady=2)

        # customer id no
        self.l_customer_id_no.grid(row=7, column=0, sticky="ew", pady=2)
        self.e_customer_id_no.grid(row=7, column=1, sticky="ew", pady=2)

        # customer tax id
        self.l_customer_tax_id.grid(row=7, column=2, sticky="ew", pady=2)
        self.e_customer_tax_id.grid(row=7, column=3, sticky="ew", pady=2)

        # customer email
        self.l_customer_email.grid(row=7, column=4, sticky="ew", pady=2)
        self.e_customer_email.grid(row=7, column=5, sticky="ew", pady=2)

        # type of service
        self.l_type_of_service.grid(row=8, column=0, sticky="ew", pady=2)
        self.e_type_of_service.grid(row=8, column=1, columnspan=5, sticky="ew", pady=2)

        # unit of service
        self.l_unit_of_service.grid(row=9, column=0, sticky="ew", pady=2)
        self.e_unit_of_service.grid(row=9, column=1, sticky="ew", pady=2)

        # quantity
        self.l_quantity_of_service.grid(row=9, column=2, sticky="ew", pady=2)
        self.e_quantity_of_service.grid(row=9, column=3, sticky="ew", pady=2)

        # price without VAT
        self.l_price_of_service.grid(row=9, column=4, sticky="ew", pady=2)
        self.e_price_of_service.grid(row=9, column=5, sticky="ew", pady=2)

        # add service button
        self.btn_add_service.grid(row=10, column=5, sticky="ew", pady=(2, 20))

        # list of service
        self.list_of_services.grid(row=11, column=0, columnspan=6, sticky="ew")

        # total amount of services
        self.l_total_amount.grid(row=12, column=4, sticky="e", pady=2)
        self.l_total_amount_var.grid(row=12, column=5, sticky="ew", pady=2)

        # description
        self.l_desc.grid(row=13, column=0, sticky="ew", pady=2)
        self.e_desc.grid(row=14, column=0, columnspan=6, sticky="ew", pady=2)

        # buttons save and print
        self.btn_invoice_save_db.grid(row=15, column=3, sticky="ew", pady=10)
        self.btn_invoice_save_pdf.grid(row=15, column=4, sticky="ew", pady=10)
        self.btn_invoice_print.grid(row=15, column=5, sticky="ew", pady=10)


class Customers(ttk.Frame):
    """Customers window. Requiers master as parameter."""

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

        # buttons - 'new customer' and 'edit customer'
        self.btn_customer_new = ttk.Button(self, text="Unos novog komitenta")
        self.btn_customer_edit = ttk.Button(self, text="Izmeni/obriši komitenta")
        # search -disabled by default until edit is pressed
        self.l_search = ttk.Label(self, text="Pretraži:", anchor="center")
        self.e_search = ttk.Entry(self)
        # search results
        self.search_results = ttk.Treeview(
            self, columns=["id", "name"], show="headings"
        )
        self.search_results.heading("id", text="ID")
        self.search_results.column("id", minwidth=0, width=40, stretch=False)
        self.search_results.heading("name", text="IME/NAZIV")
        # type of customer
        self.l_customer_type = ttk.Label(self, text="Vrsta lica", anchor="center")
        self.combo_customer_type = ttk.Combobox(
            self, values=["Fizičko lice", "Pravno lice"]
        )
        # customer name
        self.l_customer_name = ttk.Label(self, text="Ime/naziv:", anchor="center")
        self.e_customer_name = ttk.Entry(self)
        # customer address
        self.l_customer_address = ttk.Label(self, text="Adresa:", anchor="center")
        self.e_customer_address = ttk.Entry(self)
        # city
        self.l_customer_city = ttk.Label(self, text="Grad:", anchor="center")
        self.e_customer_city = ttk.Entry(self)
        # email
        self.l_customer_email = ttk.Label(self, text="E-mail:", anchor="center")
        self.e_customer_email = ttk.Entry(self)
        # ID
        self.l_customer_id_no = ttk.Label(self, text="Matični broj:", anchor="center")
        self.e_customer_id_no = ttk.Entry(self)
        # Tax ID
        self.l_customer_tax_id = ttk.Label(self, text="PIB:", anchor="center")
        self.e_customer_tax_id = ttk.Entry(self)
        # save and delete
        self.btn_customer_save = ttk.Button(self, text="Sačuvaj")
        self.btn_customer_delete = ttk.Button(self, text="Obriši")
        # save and delete labels
        self.l_customer_save_or_delete = ttk.Label(
            self, text="uspesno sačuvano", anchor="center"
        )

    def create_layout(self):
        """Places created widgets in the window (from the create_widgets() method)."""

        # 2 columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=10)
        # 14 rows
        for _ in range(14):
            self.rowconfigure(_, weight=1)

        # GRID
        # button
        self.btn_customer_new.grid(row=0, column=0, sticky="ew", pady=10)
        # search
        self.l_search.grid(row=1, column=0, sticky="ew", pady=(15, 2))
        self.e_search.grid(row=1, column=1, columnspan=2, sticky="ew", pady=(15, 2))
        # search results
        self.search_results.grid(row=2, column=0, columnspan=3, sticky="ew", pady=2)
        # edit button
        self.btn_customer_edit.grid(row=3, column=2, sticky="", pady=(3, 25))
        # customer type
        self.l_customer_name.grid(row=4, column=0, sticky="ew", pady=2)
        self.e_customer_name.grid(row=4, column=1, columnspan=2, sticky="ew", pady=2)
        # customer address
        self.l_customer_address.grid(row=5, column=0, sticky="ew", pady=2)
        self.e_customer_address.grid(row=5, column=1, columnspan=2, sticky="ew", pady=2)
        # city
        self.l_customer_city.grid(row=6, column=0, sticky="ew", pady=2)
        self.e_customer_city.grid(row=6, column=1, columnspan=2, sticky="ew", pady=2)
        # email
        self.l_customer_email.grid(row=7, column=0, sticky="ew", pady=2)
        self.e_customer_email.grid(row=7, column=1, columnspan=2, sticky="ew", pady=2)
        # ID
        self.l_customer_id_no.grid(row=8, column=0, sticky="ew", pady=2)
        self.e_customer_id_no.grid(row=8, column=1, columnspan=2, sticky="ew", pady=2)
        # tax id
        self.l_customer_tax_id.grid(row=9, column=0, sticky="ew", pady=2)
        self.e_customer_tax_id.grid(row=9, column=1, columnspan=2, sticky="ew", pady=2)
        # save and delete
        self.btn_customer_save.grid(row=10, column=1, sticky="", pady=(10, 0))
        self.btn_customer_delete.grid(row=10, column=2, sticky="", pady=(10, 0))
        # save or delete label
        self.l_customer_save_or_delete.grid(
            row=11, column=1, columnspan=2, sticky="ew", pady=10
        )


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
        # company tax id
        self.l_company_tax_id = ttk.Label(self, text="PIB:", anchor="center")
        self.e_company_tax_id = ttk.Entry(self)
        # vat system user
        self.l_company_vat = ttk.Label(self, text="U sistemu PDV-a:", anchor="center")
        self.combo_company_vat = ttk.Combobox(self, values=["Ne", "Da"])
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
            self,
            text="Ovde putanja ili mozda u dugmetu gore umesto teksta",
            anchor="center",
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
        for _ in range(14):
            self.rowconfigure(_, weight=1)

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
        self.l_company_tax_id.grid(row=5, column=0, sticky="ew", pady=2)
        self.e_company_tax_id.grid(row=5, column=1, sticky="ew", pady=2)
        # vat system user
        self.l_company_vat.grid(row=6, column=0, sticky="ew", pady=2)
        self.combo_company_vat.grid(row=6, column=1, sticky="w", pady=2)
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
        self.btn_save_settings.grid(row=12, column=1, pady=(15, 3))
        self.l_save_settings.grid(row=13, column=1)
