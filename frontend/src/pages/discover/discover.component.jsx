import React from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import { selectCurrentUser } from '../../redux/user/user.selectors';

import { DiscoverContainer } from './discover.styles.jsx';

const getLocation = () => {
  if (navigator.geolocation) {
    return navigator.geolocation.getCurrentPosition(sendPosition);
  } else {
    return "Geolocation is not supported by this browser.";
  }
}

const sendPosition = (position) => {
  const lat = position.coords.latitude
  const lan = position.coords.longitude
  console.log(`${lat}, ${lan}`)
  // const email =
  const data = JSON.stringify({email:'a', lat:lat, lon:lan})
  console.log(data)
//     (async () => {
//     const rawResponse = await fetch('http://localhost:5000/test',{
//         method: 'POST',
//         headers:{
//         'Accept': 'application/json',
//         'Content-Type': 'application/json'
//         },
//         body: data
//     });
// })
}

const sendLoc = async (email) => {
    setInterval(function(){console.log(email);}, 3000);
    }

const Discover = ({ currentUser }) => {
    currentUser ? sendLoc(currentUser.email) : sendLoc(null)
    return (
    <DiscoverContainer>
    <p>Hello</p>
    </DiscoverContainer>
)};

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
})

export default connect(mapStateToProps)(Discover);
