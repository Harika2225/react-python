import React, { useEffect, useState } from 'react';
import api from "../../api.js";
import AddGroceriesForm from './AddGroceries.js';

const GroceriesList = () => {
  const [groceries, setGroceries] = useState([]);
  const [editId, setEditId] = useState(null);
  const [editName, setEditName] = useState('');

  const getGroceries = async () => {
    try {
      const response = await api.get('/groceries');
      console.log("API Response:", response.data);  // Log the response to check data structure
      setGroceries(response.data || []);  // Set groceries directly from response
    } catch (error) {
      console.error("Error fetching groceries", error);
      setGroceries([]);  // Ensure groceries is always an array
    }
  };

  const addGroceries = async (groceryName) => {
    try {
      const response = await api.post('/groceries', { name: groceryName });
      setGroceries([...groceries, response.data]);  // Add new grocery directly to state
    } catch (error) {
      console.error("Error adding grocery", error);
    }
  };

  const updateGrocery = async (id) => {
    try {
      await api.put(`/groceries/${id}`, { name: editName });
      setGroceries(groceries.map(grocery => grocery.id === id ? { ...grocery, name: editName } : grocery));  // Update locally
      setEditId(null);  // Reset edit state
      setEditName('');
    } catch (error) {
      console.error("Error updating grocery", error);
    }
  };

  const deleteGrocery = async (id) => {
    try {
      await api.delete(`/groceries/${id}`);
      setGroceries(groceries.filter(g => g.id !== id));  // Remove from local state
    } catch (error) {
      console.error("Error deleting grocery", error);
    }
  };

  useEffect(() => {
    getGroceries();
  }, []);

  return (
    <div>
      <h2>Groceries List</h2>
      <ul>
        {Array.isArray(groceries) && groceries.length > 0 ? (
          groceries.map((grocery) => (
            <li key={grocery.id}>
              {editId === grocery.id ? (
                <div>
                  <input
                    type="text"
                    value={editName}
                    onChange={(e) => setEditName(e.target.value)}
                    placeholder="Edit grocery name"
                  />
                  <button onClick={() => updateGrocery(grocery.id)}>Save</button>
                  <button onClick={() => { setEditId(null); setEditName(''); }}>Cancel</button>
                </div>
              ) : (
                <div>
                  {grocery.name}
                  <button onClick={() => { setEditId(grocery.id); setEditName(grocery.name); }}>Edit</button>
                  <button onClick={() => deleteGrocery(grocery.id)}>Delete</button>
                </div>
              )}
            </li>
          ))
        ) : (
          <li>No groceries found.</li>
        )}
      </ul>
      <AddGroceriesForm addGroceries={addGroceries} />
    </div>
  );
};

export default GroceriesList;
