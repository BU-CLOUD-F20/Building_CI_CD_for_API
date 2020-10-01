import React from 'react';
import { Button } from 'react-bootstrap';

const CustomButton = (props) => (
	<Button style={{ backgroundColor: props.color}} type={props.type} variant={props.variant}>
		{props.children}
	</Button>
);

export default CustomButton;
