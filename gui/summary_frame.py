import customtkinter as ctk


class SummaryFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Grammar Summary",
            font=("Arial", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=10,
            pady=(10, 10)
        )

        self.summary_box = ctk.CTkTextbox(
            self,
            state="disabled"
        )

        self.summary_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

    # ==========================================
    # Public Methods
    # ==========================================

    def clear(self):

        self.summary_box.configure(state="normal")

        self.summary_box.delete("1.0", "end")

        self.summary_box.configure(state="disabled")

    def set_summary(self, text):

        self.summary_box.configure(state="normal")

        self.summary_box.delete("1.0", "end")

        self.summary_box.insert("1.0", text)

        self.summary_box.configure(state="disabled")