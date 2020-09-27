import React, { useState } from 'react';

import styles from './Body.module.css';

import { Container } from 'react-bootstrap';
import URLForm from '../../components/Form/URLForm/URLForm';
import ShortURLForm from '../../components/Form/ShortURLForm/ShortURLForm';

const LandingPage = () => {
	const [ shortURL, setShortURL ] = useState('');

	const getShortURLHandler = (url) => {
		console.log('Short URL Handler called on : ', url);
		setShortURL(url);
	};

	return (
		<Container className={styles.Body}>
			<URLForm getShortURLHandler={getShortURLHandler} />
			<ShortURLForm shortURL={shortURL} />
		</Container>
	);
};

export default LandingPage;
