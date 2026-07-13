import customtkinter as ctk


class InputFrame(ctk.CTkFrame):

    def __init__(self, parent, analyze_callback, load_file_callback, export_csv_callback, clear_callback):
        super().__init__(parent)

        self.analyze_callback = analyze_callback
        self.load_file_callback = load_file_callback
        self.export_csv_callback = export_csv_callback
        self.clear_callback = clear_callback

        self.configure(fg_color="transparent")

        self.create_widgets()

    def create_widgets(self):

        # ---------------------------------
        # Layout
        # ---------------------------------

        self.grid_rowconfigure(0, weight=0)   # Title
        self.grid_rowconfigure(1, weight=1)   # Textbox
        self.grid_rowconfigure(2, weight=0)   # Buttons

        self.grid_columnconfigure(0, weight=1)

        # ---------------------------------
        # Title
        # ---------------------------------

        title = ctk.CTkLabel(
            self,
            text="Input Text",
            font=("Arial", 18, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=(10, 5)
        )

        # ---------------------------------
        # Textbox
        # ---------------------------------

        self.textbox = ctk.CTkTextbox(
            self
        )

        self.textbox.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0, 10)
        )

        # ---------------------------------
        # Button Frame
        # ---------------------------------

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0, 10)
        )

        button_frame.grid_columnconfigure(0, weight=0)
        button_frame.grid_columnconfigure(1, weight=0)
        button_frame.grid_columnconfigure(2, weight=0)
        button_frame.grid_columnconfigure(3, weight=1)
        button_frame.grid_columnconfigure(4, weight=0)

        # ---------------------------------
        # Buttons
        # ---------------------------------

        self.load_button = ctk.CTkButton(
            button_frame,
            text="Load File",
            width=120,
            command=self.load_file_callback
        )

        self.analyze_button = ctk.CTkButton(
            button_frame,
            text="Analyze",
            width=120,
            command=self.analyze_callback
        )

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            width=120,
            command=self.clear_callback
        )

        self.export_button = ctk.CTkButton(
            button_frame,
            text="Export CSV",
            width=120,
            command=self.export_csv_callback
        )

        self.load_button.grid(
            row=0,
            column=0,
            padx=(0, 10)
        )

        self.analyze_button.grid(
            row=0,
            column=1,
            padx=(0, 10)
        )

        self.clear_button.grid(
            row=0,
            column=2
        )

        self.export_button.grid(
            row=0,
            column=4,
            sticky="e"
        )

    # =====================================================
    # Public Methods
    # =====================================================

    def get_text(self):
        return self.textbox.get("1.0", "end").strip()
        if not text:
            Toast(
                self,
                "Please enter some text.",
                "warning"
            )
        return
        if text == "":
            Toast(
                self,
                "Please enter some text.",
                "warning"
            )
        return

    def set_text(self, text):
        self.textbox.insert("1.0", text)

    def clear_text(self):
        self.textbox.delete("1.0", "end")


    # =====================================================
    # Button Callbacks
    # =====================================================
