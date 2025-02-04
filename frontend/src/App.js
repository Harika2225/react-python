import React from 'react';
import './App.css';
import GroceriesList from './components/Groceries/GroceriesList';

const App = () => {
  return (
    <div>
      <header className="App-header">
        <h1>Groceries Management App</h1>
      <main>
        <GroceriesList />
      </main>
      </header>
    </div>
  );
};

export default App;