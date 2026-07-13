import customtkinter as ctk


class Toast(ctk.CTkToplevel):
    """
    Modern toast notification for CustomTkinter.
    """

    COLORS = {
        "success": "#4CAF50",
        "warning": "#FBC02D",
        "error": "#EF5350",
        "info": "#42A5F5"
    }

    ICONS = {
        "success": "✓",
        "warning": "⚠",
        "error": "✕",
        "info": "ℹ"
    }

    def __init__(self, parent, message, toast_type="info", duration=2500):
        super().__init__(parent)

        self.overrideredirect(True)
        self.attributes("-topmost", True)

        width = 360
        height = 72

        parent.update_idletasks()

        self.final_x = (
            parent.winfo_rootx()
            + parent.winfo_width()
            - width
            - 20
        )

        self.final_y = (
            parent.winfo_rooty()
            + parent.winfo_height()
            - height
            - 20
        )

        self.geometry(f"{width}x{height}+{self.final_x}+{self.final_y + 25}")

        self.configure(
            fg_color=("white", "#202020")
        )

        card = ctk.CTkFrame(
            self,
            corner_radius=24,
            border_width=1,
            border_color=("gray78", "gray30"),
            fg_color=("white", "#262626")
        )
        card.pack(fill="both", expand=True, padx=2, pady=2)

        accent = ctk.CTkFrame(
            card,
            width=6,
            corner_radius=24,
            fg_color=self.COLORS.get(toast_type, "#42A5F5")
        )
        accent.pack(side="left", fill="y", padx=(8, 12), pady=8)

        icon = ctk.CTkLabel(
            card,
            text=self.ICONS.get(toast_type, "ℹ"),
            text_color=self.COLORS.get(toast_type, "#42A5F5"),
            width=28,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=20,
                weight="bold"
            )
        )
        icon.pack(side="left")

        label = ctk.CTkLabel(
            card,
            text=message,
            anchor="w",
            justify="left",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold"
            )
        )
        label.pack(side="left", fill="x", expand=True, padx=(10, 18))

        self._step = 0

        self.after(5, self._slide_up)
        self.after(duration, self._fade_out)

    def _slide_up(self):

        if self._step >= 12:
            return

        y = self.final_y + (12 - self._step) * 2

        self.geometry(f"+{self.final_x}+{y}")

        self._step += 1

        self.after(12, self._slide_up)

    def _fade_out(self):

        try:
            alpha = self.attributes("-alpha")
        except Exception:
            alpha = 1.0

        if alpha <= 0:
            self.destroy()
            return

        self.attributes("-alpha", alpha - 0.08)
        self.after(30, self._fade_out)
