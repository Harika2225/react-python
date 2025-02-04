import React, { useEffect, useState } from 'react';
import api from "../../api.js";
import AddGroceriesForm from './AddGroceries.js';

const GroceriesList = () => {
  const [groceries, setGroceries] = useState([]);

  const getGroceries = async () => {
    try {
      const response = await api.get('/groceries');
      setGroceries(response.data.groceries);
    } catch (error) {
      console.error("Error fetching groceries", error);
    }
  };

  const addGroceries = async (groceriesName) => {
    try {
      await api.post('/groceries', { name: groceriesName });
      getGroceries();  
    } catch (error) {
      console.error("Error adding fruit", error);
    }
  };

  useEffect(() => {
    getGroceries();
  }, []);

  return (
    <div>
      <h2>Groceries List</h2>
      <ul>
        {groceries.map((grocery, index) => (
          <li key={index}>{grocery.name}</li>
        ))}
      </ul>
      <AddGroceriesForm addGroceries={addGroceries} />
    </div>
  );
};

export default GroceriesList;