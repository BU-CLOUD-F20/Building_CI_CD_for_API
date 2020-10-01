import React from 'react';
import styled from 'styled-components';
import { useSpring, animated, config } from 'react-spring';

import Brand from './Brand/Brand';
import CollapseMenu from './CollapseMenu/CollapseMenu';
import BurgerMenu from './BurgerMenu/BurgerMenu';

const Navbar = (props) => {
	const barAnimation = useSpring({
		from: { transform: 'translate3d(0, -10rem, 0)' },
		transform: 'translate3d(0, 0, 0)'
	});

	const linkAnimation = useSpring({
		from: { transform: 'translate3d(0, 30px, 0)', opacity: 0 },
		to: { transform: 'translate3d(0, 0, 0)', opacity: 1 },
		delay: 800,
		config: config.wobbly
	});

	return (
		<React.Fragment>
			<NavBar style={barAnimation}>
				<FlexContainer>
					<Brand />
					<NavLinks style={linkAnimation}>
						<a href="/">Home</a>
						<a href="/">Sign Up</a>
						<a href="/">Log In</a>
					</NavLinks>
					<BurgerWrapper>
						<BurgerMenu navbarState={props.isOpen} handleNavbar={props.navbarHandler} />
					</BurgerWrapper>
				</FlexContainer>
			</NavBar>
			<CollapseMenu navbarState={props.isOpen} handleNavbar={props.navbarHandler} />
		</React.Fragment>
	);
};

export default Navbar;

const NavBar = styled(animated.nav)`
  position: fixed;
  margin-bottom: 0;
  width: 100%;
  top: 0;
  left: 0;
  background: #f8f8f8;
  z-index: 1;
  font-size: 1.4rem;
`;

const FlexContainer = styled.div`
	max-width: 120rem;
	display: flex;
	margin: auto;
	padding: 0 2rem;
	justify-content: space-between;
	height: 5rem;
`;

const NavLinks = styled(animated.ul)`
  justify-self: end;
  list-style-type: none;
  margin: auto 0;

  & a {
    color: #8a8a8a;
    text-transform: uppercase;
    font-weight: 600;
    border-bottom: 1px solid transparent;
    margin: 0 1.5rem;
    transition: all 300ms linear 0s;
    text-decoration: none;
    cursor: pointer;
    font-size: 1.25rem;

    &:hover {
      color: #242424;
      border-bottom: 1px solid #242424;
    }

    @media (max-width: 768px) {
      display: none;
    }
  }
`;

const BurgerWrapper = styled.div`
	margin: auto 0;

	@media (min-width: 769px) {
		display: none;
	}
`;
