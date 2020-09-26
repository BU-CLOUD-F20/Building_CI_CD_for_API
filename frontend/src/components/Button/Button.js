import React from 'react';
import { Button } from 'react-bootstrap';

const Button = (props) => (
	<Button style={{ color: props.color }} type={props.type}>
		{props.children}
	</Button>
);

export default Button;
