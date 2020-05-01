import React from 'react';
import { DiscoverContainer } from './discover.styles.jsx';

const getLocation = () => {
  if (navigator.geolocation) {
    return navigator.geolocation.getCurrentPosition(sendPosition);
  } else {
    return "Geolocation is not supported by this browser.";
  }
}

const sendPosition = position => {
  const lat = position.coords.latitude
  const lan = position.coords.longitude
  console.log(`${lat}, ${lan}`)
  console.log('HELLOOOO')
}

const test = async () => {
    setInterval(function(){ console.log('hello'); }, 3000);
    }

const Discover = () => {
    test()
    return (
    <DiscoverContainer>
    <p>Hello</p>
    </DiscoverContainer>
)};

export default Discover;
