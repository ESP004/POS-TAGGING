import customtkinter as ctk
from tkinter import filedialog


class InputFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="transparent")

        self.create_widgets()

    def create_widgets(self):

        # -------------------------
        # Section Title
        # -------------------------

        title = ctk.CTkLabel(
            self,
            text="Input Text",
            font=("Arial", 18, "bold")
        )

        title.pack(anchor="w", padx=10, pady=(10, 5))

        # -------------------------
        # Text Box
        # -------------------------

        self.textbox = ctk.CTkTextbox(
            self,
            height=180
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # -------------------------
        # Buttons
        # -------------------------

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.load_button = ctk.CTkButton(
            button_frame,
            text="Load File",
            width=120,
            command=self.load_file
        )

        self.analyze_button = ctk.CTkButton(
            button_frame,
            text="Analyze",
            width=120,
            command=self.analyze_text
        )

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            width=120,
            command=self.clear_text
        )

        self.export_button = ctk.CTkButton(
            button_frame,
            text="Export CSV",
            width=120,
            command=self.export_csv
        )

        self.load_button.pack(side="left", padx=5)
        self.analyze_button.pack(side="left", padx=5)
        self.clear_button.pack(side="left", padx=5)

        self.export_button.pack(
            side="right",
            padx=5
        )

    # =====================================================
    # Public Methods
    # =====================================================

    def get_text(self):
        """Return textbox content."""
        return self.textbox.get("1.0", "end").strip()

    def set_text(self, text):
        """Replace textbox content."""
        self.clear_text()
        self.textbox.insert("1.0", text)

    def clear_text(self):
        """Clear textbox."""
        self.textbox.delete("1.0", "end")

    # =====================================================
    # Button Callbacks
    # =====================================================

    def load_file(self):
        """
        Placeholder:
        Load a .txt file into the textbox.
        """

        file_path = filedialog.askopenfilename(
            title="Select Text File",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as file:
            self.set_text(file.read())

    def analyze_text(self):
        """
        Placeholder.

        Later this will call:

            Tokenizer
                    ↓
            POS Tagger
                    ↓
            Grammar Analyzer
        """
        print("Analyze button clicked")

    def export_csv(self):
        """
        Placeholder.

        Later:
        Export POS results to CSV.
        """
        print("Export CSV")