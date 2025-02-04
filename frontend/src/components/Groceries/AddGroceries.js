import React, { useState } from 'react';

const AddGroceriesForm = ({ addGroceries }) => {
  const [groceriesName, setGroceriesName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (groceriesName) {
      addGroceries(groceriesName);
      setGroceriesName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={groceriesName}
        onChange={(e) => setGroceriesName(e.target.value)}
        placeholder="Enter grocery name"
      />
      <button type="submit">Add Grocery</button>
    </form>
  );
};

export default AddGroceriesForm;