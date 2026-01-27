import storage
import random

# Call once to create DB
storage.init_db()

ATTACK_TYPES = ["Brute Force", "Phishing", "Malware", "Ransomware"]
SEVERITIES = ["Low", "Medium", "High", "Critical"]
DESCRIPTIONS = [
    "Multiple failed login attempts",
    "Suspicious email link clicked",
    "Malware detected on host",
    "File encrypted by ransomware"
]

def run_analysis():
    # Simulate one attack
    type_ = random.choice(ATTACK_TYPES)
    severity = random.choice(SEVERITIES)
    description = random.choice(DESCRIPTIONS)
    storage.add_incident(type_, severity, description)
