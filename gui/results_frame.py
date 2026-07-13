import customtkinter as ctk
from tkinter import ttk


class ResultFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):

        # =====================================
        # Layout
        # =====================================

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # =====================================
        # Treeview Style
        # =====================================

        style = ttk.Style()

        style.configure(
            "Treeview",
            rowheight=24
        )

        # =====================================
        # Title
        # =====================================

        title = ctk.CTkLabel(
            self,
            text="POS Tagging Result",
            font=("Arial", 18, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=(10, 5)
        )

        # =====================================
        # Table Container
        # =====================================

        table_frame = ctk.CTkFrame(self)

        table_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0, 10)
        )

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # =====================================
        # Treeview
        # =====================================

        columns = (
            "Word",
            "POS Tag",
            "Meaning"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        # ---------- Headings ----------

        self.table.heading(
            "Word",
            text="Word",
            anchor="center"
        )

        self.table.heading(
            "POS Tag",
            text="POS Tag",
            anchor="center"
        )

        self.table.heading(
            "Meaning",
            text="Meaning",
            anchor="center"
        )

        # ---------- Columns ----------

        self.table.column(
            "Word",
            width=180,
            minwidth=120,
            stretch=True,
            anchor="w"
        )

        self.table.column(
            "POS Tag",
            width=90,
            minwidth=80,
            stretch=True,
            anchor="center"
        )

        self.table.column(
            "Meaning",
            width=320,
            minwidth=220,
            stretch=True,
            anchor="w"
        )

        # =====================================
        # Scrollbars
        # =====================================

        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.table.xview
        )

        self.table.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        # =====================================
        # Layout
        # =====================================

        self.table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scroll.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scroll.grid(
            row=1,
            column=0,
            sticky="ew"
        )

    # ===================================================
    # Public Methods
    # ===================================================

    def clear(self):

        for row in self.table.get_children():
            self.table.delete(row)

    def insert_row(self, word, tag, meaning):

        self.table.insert(
            "",
            "end",
            values=(word, tag, meaning)
        )

    def load_results(self, rows):

        self.clear()

        for row in rows:
            self.insert_row(*row)