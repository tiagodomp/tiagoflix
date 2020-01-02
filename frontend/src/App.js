// import React from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React from 'react';
import axios from 'axios';
import './App.css';

function handleSubmit(event) {
  const text = document.querySelector('#char-input').value

  axios
    .get(`/index?text=${text}`).then(({data}) => {
      document.querySelector('#char-count').textContent = `${data.count} Caracteres!`
    })
    .catch(err => console.log(err))
}

function App() {
  return (
    <div className="App">
      <div>
        <label htmlFor='char-input'>Quantos Caracteres tem </label>
        <input id='char-input' type='text' />
        <button onClick={handleSubmit}>have?</button>
      </div>

      <div>
        <h3 id='char-count'></h3>
      </div>
    </div>
  );
}

export default App;
