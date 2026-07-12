import customtkinter as ctk

from gui.input_frame import InputFrame
from gui.results_frame import ResultFrame
from gui.chart_frame import ChartFrame
from gui.summary_frame import SummaryFrame


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("POS Tagging & Grammar Analyzer")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width = int(screen_width * 0.9)
        height = int(screen_height * 0.8)

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.minsize(screen_width * 0.8, screen_height * 0.7)

        ctk.set_appearance_mode("System") #Thems
        ctk.set_default_color_theme("blue") # default colors

        self.configure_grid()
        self.create_widgets()

    def configure_grid(self):

        # Window Grid
        self.grid_rowconfigure(0, weight=0)   # Title
        self.grid_rowconfigure(1, weight=0)   # Input
        self.grid_rowconfigure(2, weight=3)   # Results
        self.grid_rowconfigure(3, weight=2)   # Charts
        self.grid_rowconfigure(4, weight=0)   # Status

        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):

        # -------------------------
        # Title
        # -------------------------

        title = ctk.CTkLabel(
            self,
            text="POS Tagging & Grammar Analyzer",
            font=("Arial", 30, "bold")
        )

        title.grid(
            row=0,
            column=0,
            pady=(20, 10)
        )

        # -------------------------
        # Input Frame
        # -------------------------

        self.input_frame = InputFrame(self)

        self.input_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        # -------------------------
        # Middle Section
        # -------------------------

        middle_frame = ctk.CTkFrame(self)

        middle_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        middle_frame.grid_columnconfigure(0, weight=3)
        middle_frame.grid_columnconfigure(1, weight=2)
        middle_frame.grid_rowconfigure(0, weight=1)

        self.result_frame = ResultFrame(middle_frame)

        self.result_frame.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=10,
            sticky="nsew"
        )

        self.summary_frame = SummaryFrame(middle_frame)
        
        self.summary_frame.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=10,
            sticky="nsew"
        )

        # -------------------------
        # Charts
        # -------------------------

        self.chart_frame = ChartFrame(self)

        self.chart_frame.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        # -------------------------
        # Status Bar
        # -------------------------

        self.status = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w"
        )

        self.status.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20,
            pady=(5, 15)
        )