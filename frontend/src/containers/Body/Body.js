import React from 'react';

import styles from './Body.module.css';

import { Container } from 'react-bootstrap';
import URLForm from '../../components/Form/URLForm/URLForm';

const LandingPage = () => (
	<Container className={styles.Body}>
		<URLForm />
	</Container>
);

export default LandingPage;
