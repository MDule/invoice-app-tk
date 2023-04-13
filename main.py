"""
Tkinter based invoice software used for storing invoices in DB and creating PDF
invoices.

Author: Dušan Miletić
Date: Avgust, 2022
"""

import tkinter as tk

# from tkinter import ttk
# from tkcalendar import DateEntry as ttkDateEntry
from layout import Sidebar, Invoices, ReviewInvoices, Customers, Settings

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
        # self.settings = Settings(self)
        # self.customers = Customers(self)
        # self.review_invoices = ReviewInvoices(self)
        self.invoices = Invoices(self)

        # define commands for buttons
        # self.sidebar.btn_quit.configure(command=lambda: self.settings.destroy())
        # self.sidebar.btn_settings.configure(
        #     command=lambda: self.settings.__init__(self)
        # )

        # run
        self.mainloop()


if __name__ == "__main__":
    App("Invoice Creator v0.1", (960, 1015))
