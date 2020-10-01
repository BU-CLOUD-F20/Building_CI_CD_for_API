import React, { useState } from 'react';
import Navbar from '../../components/Navbar/Navbar';

const Navigation = () => {
	const [ navbarOpen, setOpen ] = useState(false);

	const navbarHandler = () => {
		setOpen(!navbarOpen);
	};

	return <Navbar isOpen={navbarOpen} navbarHandler={navbarHandler} />;
};

export default Navigation;
