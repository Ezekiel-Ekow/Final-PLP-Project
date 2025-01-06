import React from "react";

const ResultCard = ({ result }) => {
  return (
    <div className="result-box">
      <h3>Calculation Result</h3>
      <p><strong>Medication:</strong> {result.medication}</p>
      <p><strong>Weight:</strong> {result.weight} kg</p>
      <p><strong>Calculated Dose:</strong> {result.calculated_dose} mg</p>
      {result.warning && (
        <p style={{ color: "red" }}><strong>Warning:</strong> {result.warning}</p>
      )}
    </div>
  );
};

export default ResultCard;
