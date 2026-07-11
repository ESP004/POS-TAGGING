import customtkinter as ctk
from tkinter import ttk


class ResultFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):

        # ---------------- Title ---------------- #

        title = ctk.CTkLabel(
            self,
            text="POS Tagging Result",
            font=("Arial", 18, "bold")
        )

        title.pack(anchor="w", padx=10, pady=(10, 5))

        # ---------------- Table Frame ---------------- #

        table_frame = ctk.CTkFrame(self)

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

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

        self.table.heading("Word", text="Word")
        self.table.heading("POS Tag", text="POS Tag")
        self.table.heading("Meaning", text="Meaning")

        self.table.column("Word", width=200)
        self.table.column("POS Tag", width=100, anchor="center")
        self.table.column("Meaning", width=300)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )

        self.table.configure(
            yscrollcommand=scrollbar.set
        )

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # ==============================================
    # Public Methods
    # ==============================================

    def clear(self):
        """Remove all rows."""

        for row in self.table.get_children():
            self.table.delete(row)

    def insert_row(self, word, tag, meaning):
        """Insert one row."""

        self.table.insert(
            "",
            "end",
            values=(word, tag, meaning)
        )

    def load_results(self, rows):
        """
        rows = [
            ("The","DT","Determiner"),
            ("cat","NN","Noun")
        ]
        """

        self.clear()

        for row in rows:
            self.insert_row(*row)