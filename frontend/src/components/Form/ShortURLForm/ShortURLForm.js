import React, { useState, useRef } from 'react';
import styles from './ShortURLForm.module.css';
import { Col, Form, InputGroup, Button } from 'react-bootstrap';

const ShortURLForm = (props) => {
	const shortURLRef = useRef(null);
	const [ copied, setCopied ] = useState(false);

	const copyToClipboard = (event) => {
		event.preventDefault();
		shortURLRef.current.select();
		document.execCommand('copy');
		event.target.focus();
		setCopied(true);
	};

	const shortURLChangeHandler = (event) => {
		event.preventDefault();
		event.stopPropagation();
	};

	const copiedFeedback = copied ? <p className={styles.CopiedFeedback}>Copied to clipboard</p> : null;

	return (
		<React.Fragment>
			{props.shortURL ? (
				<Form>
					<Form.Row className={styles.ShortURLForm}>
						<Form.Group as={Col} md="6" controlId="URL" className={styles.Form}>
							<Form.Label className={styles.InputLabel}>Get Short URL</Form.Label>

							<InputGroup className={styles.InputField}>
								<InputGroup.Prepend>
									<Button variant="outline-success" onClick={copyToClipboard}>
										Copy URL
									</Button>
								</InputGroup.Prepend>
								<Form.Control
									type="text"
									ref={shortURLRef}
									value={props.shortURL}
									placeholder="Copy URL here..."
									aria-describedby="Short URL"
                                    onChange={shortURLChangeHandler}
                                    className={styles.URLTextInput}
								/>
							</InputGroup>
							{copiedFeedback}
						</Form.Group>
					</Form.Row>
				</Form>
			) : null}
		</React.Fragment>
	);
};

export default ShortURLForm;
