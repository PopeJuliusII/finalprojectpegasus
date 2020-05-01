import React from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import { auth } from '../../firebase/firebase.utils';
import SaveIcon from '../save-icon/save-icon.component';
import SaveDropdown from '../save-dropdown/save-dropdown.component';
import { selectStoreHidden } from '../../redux/store/store.selectors';
import { selectCurrentUser } from '../../redux/user/user.selectors';

import { ReactComponent as Logo } from '../../assets/pegasus.svg';

import { HeaderContainer, LogoContainer, OptionsContainer, OptionLink } from './header.styles';

const Header = ({ currentUser, hidden }) => (
    <HeaderContainer>
        <LogoContainer to='/'>
            <Logo className='logo' />
        </LogoContainer>
        <OptionsContainer>
            <OptionLink to='/discover'>
                DISCOVER
            </OptionLink>
            <OptionLink to='/saved'>
                SAVED
            </OptionLink>
            <OptionLink to='/profile'>
                PROFILE
            </OptionLink>
            {
                currentUser ? (
                <OptionLink as='div' onClick={() => auth.signOut()}>SIGN OUT</OptionLink>
                ):(
                <OptionLink to='/signin'>
                    SIGN IN
                </OptionLink>
            )}
            <SaveIcon />
        </OptionsContainer>
        {
        hidden ? null : <SaveDropdown />
        }
    </HeaderContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
    hidden: selectStoreHidden
})

export default connect(mapStateToProps)(Header);
