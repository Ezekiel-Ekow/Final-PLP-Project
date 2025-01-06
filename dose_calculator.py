import sqlite3
def calculate_dose(medication_name, weight, age=None):
    """
    Calculate the pediatric dose based on BNF standards.

    Args:
    - medication_name (str): Name of the medication.
    - weight (float): Weight of the child in kilograms.
    - age (int): Age of the child in years (optional).

    Returns:
    - dict: A dictionary containing dose calculation and any warnings.
    """
    try:
        conn = sqlite3.connect("medications.db")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT dose_per_kg, max_dose, min_age, max_age, notes 
        FROM medications WHERE name = ?;
        """, (medication_name,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            return {"error": f"Medication '{medication_name}' not found in the database."}

        dose_per_kg, max_dose, min_age, max_age, notes = result

        # Check for age restrictions
        if age is not None:
            if min_age is not None and age < min_age:
                return {"error": f"{medication_name} is not recommended for children under {min_age} years."}
            if max_age is not None and age > max_age:
                return {"error": f"{medication_name} is not recommended for children over {max_age} years."}

        # Calculate dose
        calculated_dose = weight * dose_per_kg
        if calculated_dose > max_dose:
            warning = f"Calculated dose ({calculated_dose} mg) exceeds maximum dose ({max_dose} mg). Adjusted to maximum dose."
            calculated_dose = max_dose
        else:
            warning = None

        # Return dose information
        return {
            "medication": medication_name,
            "weight": weight,
            "age": age,
            "calculated_dose": round(calculated_dose, 2),
            "warning": warning,
            "notes": notes,
        }

    except sqlite3.Error as e:
        return {"error": f"Database error: {str(e)}"}
