import tkinter as tk
from tkinter import ttk
import main
import storage

# ---------- Colors ----------
BG = "#2f2f2f"
FG = "#eeeeee"
SUB_FG = "#9e9e9e"

BTN_RED = "#c0392b"
BTN_RED_H = "#e74c3c"

BTN_BLUE = "#2980b9"
BTN_BLUE_H = "#3498db"

BTN_GRAY = "#555555"
BTN_GRAY_H = "#777777"

# Severity row colors
SEVERITY_STYLE = {
    "Critical": {"bg": "#5c1a1a", "fg": "#ffb3b3"},
    "High":     {"bg": "#5a3314", "fg": "#ffcc99"},
    "Medium":   {"bg": "#5a4a14", "fg": "#fff0b3"},
    "Low":      {"bg": "#1f4f2e", "fg": "#b3ffcc"},
}

class SIEMDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-SIEM Dashboard")
        self.root.geometry("1000x600")
        self.root.configure(bg=BG)

        # ---------- Title ----------
        tk.Label(
            root,
            text="Mini-SIEM Dashboard",
            font=("Segoe UI", 20, "bold"),
            fg=FG,
            bg=BG
        ).pack(pady=(12, 2))

        tk.Label(
            root,
            text="made by Ali",
            font=("Segoe UI", 10),
            fg=SUB_FG,
            bg=BG
        ).pack(pady=(0, 10))

        # ---------- Buttons ----------
        btn_frame = tk.Frame(root, bg=BG)
        btn_frame.pack(pady=8)

        self.make_button(
            btn_frame, "⚔ Simulate Attack",
            self.simulate_attack, BTN_RED, BTN_RED_H, 18
        ).pack(side="left", padx=6)

        self.make_button(
            btn_frame, "🔄 Refresh (Clear)",
            self.refresh_and_clear, BTN_BLUE, BTN_BLUE_H, 18
        ).pack(side="left", padx=6)

        self.make_button(
            btn_frame, "❌ Exit",
            self.exit_app, BTN_GRAY, BTN_GRAY_H, 12
        ).pack(side="left", padx=6)

        # ---------- Status ----------
        self.status = tk.Label(
            root,
            text="Status: Ready",
            fg=SUB_FG,
            bg=BG,
            font=("Segoe UI", 10)
        )
        self.status.pack(pady=4)

        self.counter = tk.Label(
            root,
            text="Incidents: 0",
            fg=FG,
            bg=BG,
            font=("Segoe UI", 11, "bold")
        )
        self.counter.pack(pady=(0, 6))

        # ---------- Table ----------
        self.setup_table()
        self.load_incidents()

    # ---------- Button Factory ----------
    def make_button(self, parent, text, cmd, bg, hover, width):
        btn = tk.Button(
            parent,
            text=text,
            command=cmd,
            bg=bg,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=width,
            relief="flat",
            cursor="hand2"
        )
        btn.bind("<Enter>", lambda e: btn.config(bg=hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    # ---------- Table ----------
    def setup_table(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            background="#1e1e1e",
            foreground="#dddddd",
            fieldbackground="#1e1e1e",
            rowheight=30,
            borderwidth=0
        )

        style.configure(
            "Treeview.Heading",
            background="#3a3a3a",
            foreground="#ffffff",
            font=("Segoe UI", 10, "bold")
        )

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=20, pady=10)

        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        self.table = ttk.Treeview(
            frame,
            columns=("time", "type", "severity", "description"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.table.yview)

        self.table.heading("time", text="Time")
        self.table.heading("type", text="Attack Type")
        self.table.heading("severity", text="Severity")
        self.table.heading("description", text="Description")

        self.table.column("time", width=160, anchor="center")
        self.table.column("type", width=200, anchor="center")
        self.table.column("severity", width=100, anchor="center")
        self.table.column("description", width=460, anchor="w")

        for sev, colors in SEVERITY_STYLE.items():
            self.table.tag_configure(
                sev,
                background=colors["bg"],
                foreground=colors["fg"]
            )

        self.table.pack(expand=True, fill="both")

    # ---------- Logic 
    def load_incidents(self):
        self.table.delete(*self.table.get_children())
        incidents = storage.load_incidents()

        for inc in incidents:
            self.table.insert(
                "", "end",
                values=(
                    inc["time"],
                    inc["type"],
                    inc["severity"],
                    inc["description"]
                ),
                tags=(inc["severity"],)
            )

        self.counter.config(text=f"Incidents: {len(incidents)}")
        self.status.config(text="Status: Loaded")

    def simulate_attack(self):
        main.run_analysis()
        self.load_incidents()
        self.status.config(text="Status: Attack simulated")

    def refresh_and_clear(self):
        storage.clear_incidents()
        self.load_incidents()
        self.status.config(text="Status: Incidents cleared")

    def exit_app(self):
        storage.clear_incidents()
        self.root.destroy()


def start_dashboard():
    root = tk.Tk()
    SIEMDashboard(root)
    root.mainloop()


if __name__ == "__main__":
    start_dashboard()
