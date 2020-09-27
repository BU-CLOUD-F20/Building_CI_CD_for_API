import React, { useState } from 'react';
import { Form, InputGroup, Col } from 'react-bootstrap';
import Button from '../../Button/Button';

import styles from './URLForm.module.css';

const URLForm = (props) => {
	const [ validated, setValidated ] = useState(false);

	const handleSubmit = (event) => {
		event.preventDefault();

		const form = event.currentTarget;
		if (form.checkValidity() === false) {
			event.stopPropagation();
		}

		const longURL = event.target.elements.URL.value;
		console.log('Long URL: ', longURL);
		setValidated(true);
		props.getShortURLHandler(longURL);

	};

	return (
		<Form noValidate validated={validated} onSubmit={handleSubmit}>
			<Form.Row className={styles.URLForm}>
				<Form.Group as={Col} md="6" controlId="URL" className={styles.Form}>
					<Form.Label className={styles.InputLabel}>Enter URL</Form.Label>
					<InputGroup className={styles.InputField}>
						<Form.Control
							type="text"
							placeholder="Paste URL here..."
							aria-describedby="Long URL"
							required
						/>
						<Form.Control.Feedback type="invalid">Please enter a valid URL.</Form.Control.Feedback>
						<Form.Control.Feedback>Generating short URL...</Form.Control.Feedback>
					</InputGroup>
					<div className={styles.GetButton}>
						<Button type="submit" color="#2789f2">
							Get Shortened URL
						</Button>
					</div>
				</Form.Group>
			</Form.Row>
		</Form>
	);
};

export default URLForm;
