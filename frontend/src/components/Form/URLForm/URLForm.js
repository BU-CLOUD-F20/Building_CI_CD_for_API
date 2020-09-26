import React, { useState } from 'react';
import { Form } from 'react-bootstrap';
import Button from '../../Button/Button';

const URLForm = () => {
	const [ validated, setValidated ] = useState(false);

	const handleSubmit = (event) => {
		const form = event.currentTarget;
		if (form.checkValidity() === false) {
			event.preventDefault();
			event.stopPropagation();
		}

		setValidated(true);
	};

	return (
		<Form noValidate validated={validated} onSubmit={handleSubmit}>
			<Form.Row>
				<Form.Group as={Col} md="4" controlId="validationCustom01">
					<Form.Label>Paste Long URL below: </Form.Label>
					<Form.Control required type="text" placeholder="First name" defaultValue="Mark" />
					<Form.Control.Feedback>Looks good!</Form.Control.Feedback>
				</Form.Group>
			</Form.Row>

			<Button type="submit" color="#2789f2">
				Submit form
			</Button>
		</Form>
	);
};

export default URLForm;
