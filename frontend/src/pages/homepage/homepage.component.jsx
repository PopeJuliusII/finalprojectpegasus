import React from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import { HomePageContainer, HomePageImageContainer } from './homepage.styles';

import { setCurrentUser } from '../../redux/user/user.actions';
import { selectCurrentUser } from '../../redux/user/user.selectors';

const Homepage = ({ currentUser }) => {
    return (
    <HomePageContainer>
        <HomePageImageContainer>
            WELCOME { currentUser ? `, ${currentUser.displayName.toUpperCase()}!` : '!' }
        </HomePageImageContainer>
    </HomePageContainer>
)};

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
})

const mapDispatchToProps = dispatch => ({
    setCurrentUser: user => dispatch(setCurrentUser(user))
});

export default connect(mapStateToProps, mapDispatchToProps)(Homepage);
