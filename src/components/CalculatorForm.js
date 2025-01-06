import React, { useState, useEffect } from "react";

const CalculatorForm = ({ onCalculate }) => {
  const [medication, setMedication] = useState("");
  const [weight, setWeight] = useState("");
  const [medications, setMedications] = useState([]);

  useEffect(() => {
    const fetchMedications = async () => {
      try {
        const response = await fetch("http://localhost:5000/medications");
        const data = await response.json();
        setMedications(data);
      } catch (error) {
        console.error("Error fetching medications:", error);
      }
    };

    fetchMedications();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (medication && weight > 0) {
      onCalculate(medication, weight);
    } else {
      alert("Please select a medication and enter a valid weight!");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="calculator-form">
      <div className="form-group">
        <label htmlFor="medication" className="form-label">Medication:</label>
        <select
          id="medication"
          value={medication}
          onChange={(e) => setMedication(e.target.value)}
          className="form-select"
          required
        >
          <option value="">Select Medication</option>
          {medications.map((med) => (
            <option key={med} value={med}>
              {med}
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <label htmlFor="weight" className="form-label">Weight (kg):</label>
        <input
          type="number"
          id="weight"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          className="form-input"
          required
        />
      </div>
      <button type="submit" className="calculate-button">Calculate</button>
    </form>
  );
};

export default CalculatorForm;
