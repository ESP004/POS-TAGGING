import customtkinter as ctk


class ChartFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Visualization",
            font=("Arial", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=10,
            pady=(10, 10)
        )

        self.placeholder = ctk.CTkLabel(
            self,
            text="Charts will appear here",
            font=("Arial", 16)
        )

        self.placeholder.pack(
            expand=True
        )