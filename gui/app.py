
import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

from gui.input_frame import InputFrame
from gui.results_frame import ResultFrame
from gui.chart_frame import ChartFrame
from gui.summary_frame import SummaryFrame
from gui.toast import Toast

from core.tokenizer import Tokenizer
from core.pos_tagger import PosTagger
from core.grammar_analyzer import GrammarAnalyzer
from core.tag_dictionary import get_tag_meaning

from utils.file_loader import FileLoader
from utils.csv_exporter import CSVExporter


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("POS Tagging & Grammar Analyzer")

        self.iconbitmap("assets/app2.ico")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width = int(screen_width * 0.90)
        height = int(screen_height * 0.85)

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

        self.minsize(1100, 700)

        self.current_theme = "Light"

        ctk.set_appearance_mode(self.current_theme)
        ctk.set_default_color_theme("blue")

        # ==================================================
        # Backend
        # ==================================================

        self.tokenizer = Tokenizer()
        self.pos_tagger = PosTagger()
        self.grammar_analyzer = GrammarAnalyzer()

        # ==================================================
        # GUI
        # ==================================================

        self.configure_grid()
        self.create_widgets()

    # ======================================================

    def configure_grid(self):

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=3)

    # ======================================================

    def create_widgets(self):

        # ==================================================
        # Title
        # ==================================================

        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.grid(row=0, column=0, sticky="ew", padx=25, pady=(18, 18))
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=0)

        title = ctk.CTkLabel(
            title_frame,
            text="POS Tagging & Grammar Analyzer",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=34,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0
        )

        self.theme_button = ctk.CTkButton(
            title_frame,
            text="🌙 Dark Mode",
            width=130,
            command=self.toggle_theme
        )

        self.theme_button.grid(
            row=0,
            column=1,
            padx=(20, 0)
        )

        # ==================================================
        # Workspace
        # ==================================================

        workspace = ctk.CTkFrame(
            self,
            corner_radius=12,
            border_width=1,
            border_color=("gray75", "gray25")
        )

        workspace.grid(
            row=1,
            column=0,
            padx=25,
            pady=(0, 12),
            sticky="nsew"
        )

        workspace.grid_rowconfigure(0, weight=1)
        workspace.grid_columnconfigure(0, weight=1)
        workspace.grid_columnconfigure(1, weight=1)

        self.input_frame = InputFrame(
            workspace,
            analyze_callback=self.analyze,
            load_file_callback=self.load_file,
            export_csv_callback=self.export_csv,
            clear_callback=self.clear_all
        )

        self.input_frame.grid(
            row=0,
            column=0,
            padx=(12, 6),
            pady=12,
            sticky="nsew"
        )

        self.result_frame = ResultFrame(workspace)

        self.result_frame.grid(
            row=0,
            column=1,
            padx=(6, 12),
            pady=12,
            sticky="nsew"
        )

        bottom = ctk.CTkFrame(
            self,
            corner_radius=12,
            border_width=1,
            border_color=("gray75", "gray25")
        )

        bottom.grid(
            row=2,
            column=0,
            padx=25,
            pady=(0, 20),
            sticky="nsew"
        )

        bottom.grid_rowconfigure(0, weight=1)
        bottom.grid_columnconfigure(0, weight=1)
        bottom.grid_columnconfigure(1, weight=1)

        self.summary_frame = SummaryFrame(bottom)

        self.summary_frame.grid(
            row=0,
            column=0,
            padx=(12, 6),
            pady=12,
            sticky="nsew"
        )

        self.chart_frame = ChartFrame(bottom)

        self.chart_frame.grid(
            row=0,
            column=1,
            padx=(6, 12),
            pady=12,
            sticky="nsew"
        )

    # ======================================================
    # Theme
    # ======================================================

    def toggle_theme(self):

        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
            self.theme_button.configure(text="☀ Light Mode")
        else:
            ctk.set_appearance_mode("Light")
            self.theme_button.configure(text="🌙 Dark Mode")

    # ======================================================
    # Analyze
    # ======================================================

    def analyze(self):

        text = self.input_frame.get_text()
        if not text:
            Toast(
                self,
                "Nothing to analyze.",
                "warning"
            )
            return

        tokens = self.tokenizer.tokenize(text)

        tagged_tokens = self.pos_tagger.tag(tokens)

        summary = self.grammar_analyzer.analyze(tagged_tokens)

        # Handle summary frame
        if summary:
            summary_text = ""

            for key, value in summary.items():
                summary_text += f"{key}: {value}\n"

            self.summary_frame.set_summary(summary_text)
        else :
            self.summary_frame.clear()

        rows = [
            (
                token,
                tag,
                get_tag_meaning(tag)
            )
            for token, tag in tagged_tokens
        ]
        # For export csv
        self.last_rows = rows
        self.last_summary = summary
        self.last_tagged_tokens = tagged_tokens

        # Handle result frame
        if rows:
            self.result_frame.load_results(rows)
        else:
            self.result_frame.clear()

        # Handle chaet frame
        if summary:
            self.chart_frame.draw(summary)
        else:
            self.summary_frame.clear()

    # ======================================================
    # Loading a new file
    # ======================================================

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Open File",
            initialdir=str(Path.home() / "Documents"),
            filetypes=[
                ("Supported Files", "*.txt *.pdf *.docx"),
                ("Text Files", "*.txt"),
                ("PDF Files", "*.pdf"),
                ("Word Documents", "*.docx"),
                ("All Files", "*.*")
            ]
        )
        if not file_path:
            return
        
        text = FileLoader.load(file_path)
        self.clear_analysis()
        self.input_frame.set_text(text)
        self.clear_analysis()
        Toast(
            self,
            "File loaded successfully.",
            "success"
        )

    # ======================================================
    # Clear Analyze
    # ======================================================

    def clear_analysis(self):

        self.result_frame.clear()
        self.summary_frame.clear()
        self.chart_frame.clear()
        self.last_rows = []
        self.last_summary = {}
        self.last_tagged_tokens = []

    # ======================================================
    # Clear button Input frame
    # ======================================================

    def clear_all(self):
        self.input_frame.clear_text()
        self.clear_analysis()

    # ======================================================
    # Export to csv
    # ======================================================

    def export_csv(self):
        if not self.last_rows:
            Toast(
                self,
                "Nothing to export.",
                "warning"
            )
            return

        file_path = filedialog.asksaveasfilename(
            title="Export CSV",
            defaultextension=".csv",
            filetypes=[
                ("CSV Files", "*.csv")
            ]
        )
        if not file_path:
            return

        CSVExporter.export(
            file_path,
            self.last_rows
        )
        Toast(
            self,
            "CSV exported successfully.",
            "success"
        )

        