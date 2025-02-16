import React, { useState } from 'react';
import axios from 'axios';

export const EnergyForm = () => {
  const [formData, setFormData] = useState({ power: 10 });

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/plots/generate-pdf/', formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="number" 
        value={formData.power} 
        onChange={(e) => setFormData({...formData, power: e.target.value})}
      />
      <button type="submit">Generuj wniosek</button>
    </form>
  );
};
