from flask import Flask, request, jsonify
from flask_cors import CORS
from dose_calculator import calculate_dose
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) with specific origin
CORS(app, origins=["http://localhost:3000", "https://your-frontend-domain.com"])

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Handle POST requests for dose calculation.
    """
    data = request.get_json()
    
    # Validate input data
    medication = data.get("medication")
    weight = data.get("weight")
    
    if not medication or not weight:
        return jsonify({"error": "Invalid input. Medication and weight are required."}), 400
    
    try:
        weight = float(weight)
    except ValueError:
        return jsonify({"error": "Weight must be a valid number."}), 400

    # Call the calculate_dose function
    result = calculate_dose(medication, weight)
    return jsonify(result)

@app.route("/medications", methods=["GET"])
def get_medications():
    """
    Fetch unique medication names from the database.
    """
    try:
        conn = sqlite3.connect("medications.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT name FROM medications;")  # Use DISTINCT
        medications = [row[0] for row in cursor.fetchall()]
        conn.close()
        return jsonify(medications)
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500


if __name__ == "__main__":
    # Debug log to confirm backend is running
    print("Backend server is running on http://localhost:5000")
    app.run(debug=True)
