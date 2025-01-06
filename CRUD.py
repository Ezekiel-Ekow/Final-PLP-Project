import sqlite3

def get_medication_by_name(name):
    conn = sqlite3.connect("medications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medications WHERE name = ?;", (name,))
    medication = cursor.fetchone()
    conn.close()
    return medication

# Example usage
medication = get_medication_by_name("Paracetamol")
print("Fetched Medication:", medication)



# Add new medication

def add_medication(name, route, dose_per_kg, max_dose):
    conn = sqlite3.connect("medications.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO medications (name, route, dose_per_kg, max_dose)
    VALUES (?, ?, ?, ?);
    """, (name, route, dose_per_kg, max_dose))
    conn.commit()
    conn.close()

# Example usage
add_medication("Azithromycin", "liquid", 10.0, 500.0)




# Update medication

def update_medication(name, dose_per_kg=None, max_dose=None):
    conn = sqlite3.connect("medications.db")
    cursor = conn.cursor()
    if dose_per_kg:
        cursor.execute("UPDATE medications SET dose_per_kg = ? WHERE name = ?;", (dose_per_kg, name))
    if max_dose:
        cursor.execute("UPDATE medications SET max_dose = ? WHERE name = ?;", (max_dose, name))
    conn.commit()
    conn.close()

# Example usage
update_medication("Paracetamol", dose_per_kg=16.0)





# delete medication
def delete_medication(name):
    conn = sqlite3.connect("medications.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medications WHERE name = ?;", (name,))
    conn.commit()
    conn.close()

# Example usage
delete_medication("Ibuprofen")

