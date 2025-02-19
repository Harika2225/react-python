import React, { useState } from 'react';
import { MdAddCircle } from "react-icons/md";

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
    <div className='addGrocery'>
      <input
        type="text"
        value={groceriesName}
        onChange={(e) => setGroceriesName(e.target.value)}
        placeholder="Enter grocery name"
      />
      <button className='addGroceryIcon' type="submit" onClick={handleSubmit}><MdAddCircle/></button>
    </div>
  );
};

export default AddGroceriesForm;