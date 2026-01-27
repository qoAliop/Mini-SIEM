# Mini-SIEM Dashboard

**Mini-SIEM** is a lightweight Security Information and Event Management (SIEM) tool built in Python.  
It provides a dark-themed, interactive dashboard that simulates cyber attacks, tracks incidents in real-time, and visualizes them by severity, giving a hands-on experience similar to a real SOC environment.

---

## Features

- **Dark-themed, user-friendly dashboard** with clear incident visualization.
- **Severity-based color coding** for quick identification:
  - Critical (red)
  - High (orange)
  - Medium (yellow)
  - Low (green)
- **Simulate attacks** with a single click to test detection and logging.
- **Refresh/Clear incidents** directly from the UI.
- **Exit button** clears all incidents and closes the app.
- **SQLite database** backend for reliable storage, replacing JSON files.
- Ready for **real log ingestion** or expansion with real-world detection rules.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mini-siem.git
cd mini-siem
