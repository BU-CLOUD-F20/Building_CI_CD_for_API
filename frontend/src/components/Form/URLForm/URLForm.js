import React, { useState } from 'react';
import { Form, InputGroup, Col } from 'react-bootstrap';
import Button from '../../Button/Button';

const URLForm = () => {
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
	};

	return (
		<Form noValidate validated={validated} onSubmit={handleSubmit}>
			<Form.Row>
				<Form.Group as={Col} md="6" controlId="URL">
					<Form.Label>Enter URL</Form.Label>
					<InputGroup>
						<Form.Control
							type="text"
							placeholder="Paste URL here..."
							aria-describedby="Long URL"
							required
						/>
						<Form.Control.Feedback type="invalid">Please enter a valid URL.</Form.Control.Feedback>
						<Form.Control.Feedback>Generating short URL...</Form.Control.Feedback>
					</InputGroup>
				</Form.Group>
			</Form.Row>
			<Button type="submit" color="#2789f2">
				Get Shortened URL
			</Button>
		</Form>
	);
};

export default URLForm;
