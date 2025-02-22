import logo from './logo.svg';
import './App.css';
//Create react_app methods
// npx create - react - app test - app
// cd test - app
// npm start


function App() {
  fetch("http://127.0.0.1:8000/product/").then(response => {
    console.log(response.json());
  })
    .catch(error => {
      console.log(error);
    })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
