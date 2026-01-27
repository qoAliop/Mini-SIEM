import storage
import random
import correlator

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

    # Run correlation
    for c in correlator.correlate():
        storage.add_incident(c["type"], c["severity"], c["description"])

def run_analysis():
    # Simulate one attack
    type_ = random.choice(ATTACK_TYPES)
    severity = random.choice(SEVERITIES)
    description = random.choice(DESCRIPTIONS)
    storage.add_incident(type_, severity, description)

```python
if __name__ != "__main__":
    print("Please run UII.py to launch the dashboard.")
    exit()
