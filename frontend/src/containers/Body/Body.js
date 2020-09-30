import React, { useState } from 'react';

import styles from './Body.module.css';

import { Container } from 'react-bootstrap';
import URLForm from '../../components/Form/URLForm/URLForm';
import ShortURLForm from '../../components/Form/ShortURLForm/ShortURLForm';

import axios from 'axios';

const LandingPage = () => {
	const [ shortURL, setShortURL ] = useState('');

	const getShortURLHandler = (url) => {
		const urlObj = {
			original_link: url,
			expire_at: '2020/10/20'
		};

		const API = `http://shorturl3-ece-528-building-ci-cd-for-api.k-apps.osh.massopen.cloud`;
		// const API = `http://localhost:5000/`
		axios
			.post(API, urlObj)
			.then((result) => {
				setShortURL(result.data.short_link);
			})
			.catch((err) => {
				console.log(err);
			});
	};

	return (
		<Container className={styles.Body}>
			<URLForm getShortURLHandler={getShortURLHandler} />
			<ShortURLForm shortURL={shortURL} />
		</Container>
	);
};

export default LandingPage;
