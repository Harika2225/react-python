import React, { useState } from "react";
import { MdAddCircle } from "react-icons/md";

const AddGroceriesForm = ({ addGroceries }) => {
  const [groceriesName, setGroceriesName] = useState("");

  const handleSubmit = () => {
    if (groceriesName) {
      addGroceries(groceriesName);
      setGroceriesName("");
    }
  };
  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleSubmit();
  };

  return (
    <div className="addGrocery">
      <input
        type="text"
        value={groceriesName}
        onChange={(e) => setGroceriesName(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Enter grocery name"
      />
      <button className="addGroceryIcon" type="submit" onClick={handleSubmit}>
        <MdAddCircle />
      </button>
    </div>
  );
};

export default AddGroceriesForm;
