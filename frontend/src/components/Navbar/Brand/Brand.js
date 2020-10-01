import React from 'react';
import styles from './Brand.module.css';
import Logo from '../../../assets/images/logo.jpg';

const Brand = () => (
	<a href="/">
		<img className={styles.Logo} src={Logo} alt="Doubly Logo" />
	</a>
);

export default Brand;
