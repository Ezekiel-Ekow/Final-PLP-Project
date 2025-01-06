import sqlite3

# Connect to the database
conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

# Update the schema to ensure it has the necessary columns
try:
    cursor.execute("ALTER TABLE medications ADD COLUMN min_age INTEGER DEFAULT 0;")
    cursor.execute("ALTER TABLE medications ADD COLUMN max_age INTEGER DEFAULT NULL;")
    cursor.execute("ALTER TABLE medications ADD COLUMN notes TEXT DEFAULT NULL;")
    print("Schema updated successfully.")
except sqlite3.Error as e:
    print(f"Schema update failed: {e}")

# Define BNF-compliant sample data
sample_data = [
    ("Paracetamol", "oral", 15.0, 1000.0, 0, None, "Max 4 doses/day"),
    ("Ibuprofen", "oral", 10.0, 600.0, 3, 12, "Avoid in severe dehydration"),
    ("Ceftriaxone", "intravenous", 50.0, 2000.0, 0, None, "Consult specialist for neonatal use"),
    ("Amoxicillin", "oral", 20.0, 750.0, 0, None, "Divide dose for severe infections"),
    ("Gentamicin", "intravenous", 7.5, 400.0, 0, None, "Monitor renal function"),
    ("Vancomycin", "intravenous", 10.0, 2000.0, 0, None, "Monitor trough levels"),
    ("Ondansetron", "oral", 0.15, 8.0, 2, None, "Max 3 doses/day"),
    ("Hydrocortisone", "intravenous", 4.0, 300.0, 0, None, "Administer in emergencies"),
    ("Phenytoin", "intravenous", 20.0, 1000.0, 0, None, "Slow infusion recommended"),
    ("Metronidazole", "oral", 10.0, 500.0, 0, None, "Take with food to avoid nausea")
]

# Insert data into the table
cursor.executemany("""
INSERT INTO medications (name, route, dose_per_kg, max_dose, min_age, max_age, notes)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", sample_data)

# Commit changes and close connection
conn.commit()
conn.close()
print("Database updated and populated with BNF-compliant medications!")
