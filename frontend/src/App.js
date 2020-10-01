import React from 'react';
import './App.css';
import Body from './containers/Body/Body';
import Navigation from './containers/Navigation/Navigation';

function App() {
	return (
		<div className="App">
			<Navigation />
			<Body />
		</div>
	);
}

export default App;
