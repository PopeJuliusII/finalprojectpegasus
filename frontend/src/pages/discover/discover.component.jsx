import React, { useEffect, useState } from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import PlaceTile from '../../components/place-tile/place-tile.component';

import { selectCurrentUser } from '../../redux/user/user.selectors';

import { DiscoverPageContainer, DiscoverPageMapContainer, DiscoverRecsContainer } from './discover.styles.jsx';


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
// [40.751733, -73.9816807]}

const Discover = ({ currentUser }) => {

    const [coordinates, setCoordinates] = useState([40.751733, -73.9816807])
    const [recs, setRecs] = useState([])

    useEffect(() => {
        recCenter()
    }, [coordinates])

    useEffect(() => {
        timer()
    }, [currentUser])

    const timer = () => {
        setInterval(function(){
            fetchRec()
        }, 3000);
        }

    const fetchRec = () => {
          if (navigator.geolocation) {
            return navigator.geolocation.getCurrentPosition(sendPosition);
          } else {
            console.log('geolocation not supported by browser')
            // alert('geolocation not supported by browser')
            return null;
        }
    }

    const sendPosition = ( position ) => {
      const lat = position.coords.latitude
      const lon = position.coords.longitude
      console.log('a')
      if (lat !== coordinates[0] && lon !== coordinates[1]) {
          console.log('fail')
          setCoordinates([lat, lon])
  }}

  const recCenter = async () => {
  if ( currentUser ){
      try {
          const bata = JSON.stringify({id:currentUser.id, lat:coordinates[0], lon:coordinates[1]})
          console.log('data:', bata)
          const data = JSON.stringify({id:currentUser.id, lat:40.752685, lon:-73.9781084})
          console.log(data)
          const rawResponse = await fetch('http://localhost:5000/get_recommendation',{
              method: 'POST',
              headers:{
              'Accept': 'application/json',
              'Content-Type': 'application/json'
              },
              body: data
          });
          const output = await rawResponse.json()
          setRecs(output.data)
          console.log(recs)
      } catch(e) {
          console.log(e)
      }
  }
};

    return (
    <DiscoverPageContainer>
        <DiscoverPageMapContainer>
            <iframe width="100%" height="100%" src={`https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.4676944628436!2d${coordinates[1]}!3d${coordinates[0]}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDDCsDQ1JzA2LjIiTiA3M8KwNTgnNTQuMSJX!5e0!3m2!1sen!2sus!4v1589047748692!5m2!1sen!2sus`} frameBorder="0" scrolling="no" marginHeight="0" marginWidth="0"></iframe>
        </DiscoverPageMapContainer>
        <DiscoverRecsContainer>
            { recs.length > 0 ?
                recs.map(rec => (<PlaceTile key={rec.id} {...rec} />))
                :
            <h3>Log in to get recommendations!</h3>

        }
        </DiscoverRecsContainer>
    </DiscoverPageContainer>
)};

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
})

export default connect(mapStateToProps)(Discover);
