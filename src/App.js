import React, { useState } from "react";
import CalculatorForm from "./components/CalculatorForm";
import ResultCard from "./components/ResultCard";
import "./App.css"; // Import custom styles

const App = () => {
  const [result, setResult] = useState(null);

  const handleCalculate = async (medication, weight) => {
    try {
      const response = await fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ medication, weight }),
      });
  
      const data = await response.json();
      console.log("API Response:", data); // Log the response
  
      if (!response.ok) {
        throw new Error(data.error || "Failed to calculate dose");
      }
  
      setResult(data); // Update the result state
      console.log("Updated Result State:", data); // Log the updated state
    } catch (error) {
      console.error("Error:", error.message);
      alert(error.message);
    }
  };
  

  return (
    <div className="app-container">
      <h1 className="app-title">Pediatric Dose Calculator</h1>
      <div className="calculator-container">
        <CalculatorForm onCalculate={handleCalculate} />
      </div>
      {result && (
        <div className="result-container">
          <ResultCard result={result} />
        </div>
      )}
    </div>
  );
};

export default App;


