import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ChartFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.summary = None

        self.create_widgets()

    def create_widgets(self):

        # ----------------------------------
        # Title
        # ----------------------------------

        title = ctk.CTkLabel(
            self,
            text="Visualization",
            font=("Arial", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        # ----------------------------------
        # Chart Selector
        # ----------------------------------

        self.chart_selector = ctk.CTkSegmentedButton(
            self,
            values=["Bar Chart", "Pie Chart"],
            command=self.change_chart
        )

        self.chart_selector.pack(
            pady=(0, 10)
        )

        self.chart_selector.set("Bar Chart")

        # ----------------------------------
        # Chart Container
        # ----------------------------------

        self.chart_container = ctk.CTkFrame(self)

        self.chart_container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # ----------------------------------
        # Figure
        # ----------------------------------

        self.figure = Figure(
            figsize=(6, 3),
            dpi=100
        )

        self.axis = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=self.chart_container
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        self.axis.set_title("Chart will appear here")

        self.canvas.draw()

    # ==================================================
    # Public Methods
    # ==================================================

    def draw(self, summary):

        self.summary = summary.copy()

        self.summary.pop("Total Words", None)

        if not self.summary:
            return

        if self.chart_selector.get() == "Bar Chart":
            self._draw_bar_chart()
        else:
            self._draw_pie_chart()

    # ==================================================
    # Private Methods
    # ==================================================

    def change_chart(self, value):

        if self.summary is None:
            return

        if value == "Bar Chart":
            self._draw_bar_chart()
        else:
            self._draw_pie_chart()

    def _draw_bar_chart(self):

        self.figure.clear()

        self.axis = self.figure.add_subplot(111)

        categories = list(self.summary.keys())
        values = list(self.summary.values())

        self.axis.bar(
            categories,
            values
        )

        self.axis.set_title("POS Tag Distribution")

        self.axis.set_xlabel("Part of Speech")

        self.axis.set_ylabel("Count")

        self.axis.grid(
            axis="y",
            linestyle="--",
            alpha=0.4
        )

        self.axis.tick_params(
            axis="x",
            labelrotation=30
        )

        self.figure.tight_layout()

        self.canvas.draw()

    def _draw_pie_chart(self):

        self.figure.clear()

        # Pie axis (left side)
        self.axis = self.figure.add_axes(
            [0.05, 0.10, 0.55, 0.80]
        )

        categories = list(self.summary.keys())
        values = list(self.summary.values())

        total = sum(values)

        wedges, _ = self.axis.pie(
            values,
            startangle=90,
            labels=None,
            radius=1.15
        )

        self.axis.set_title("POS Tag Distribution")
        self.axis.set_aspect("equal")

        legend_labels = [
            f"{name} ({value} | {value / total:.1%})"
            for name, value in zip(categories, values)
        ]

        self.figure.legend(
            wedges,
            legend_labels,
            title="POS Tags",
            loc="center left",
            bbox_to_anchor=(0.68, 0.5),
            fontsize=9,
            title_fontsize=10,
            frameon=False
        )
        self.canvas.draw()


    def clear(self):

        self.summary = None
        self.figure.clear()
        self.axis = self.figure.add_subplot(111)
        self.axis.set_title("Chart will appear here")
        self.canvas.draw_idle()