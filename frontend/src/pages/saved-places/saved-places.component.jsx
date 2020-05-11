import React, { useEffect, useState } from 'react';

import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import { selectCurrentUser } from "../../redux/user/user.selectors";

import PlaceTile from '../../components/place-tile/place-tile.component';

import { SavedPageContainer, SavedPageMapContainer, SavedPlacesContainer, SavedImageContainer } from './saved.styles.jsx';

const SavedPlaces = ({ currentUser }) => {
    const [saved, setSaved] = useState([])

    const fetchData = async ({ currentUser }) => {
          const url = 'http://localhost:5000/get_data'
          try {
              const response = await fetch(
                  currentUser
                  ? `${url}/${currentUser.id}/${currentUser.email}`
                  : null
              );
              const output = await response.json()
              setSaved(output.data.saved)
          } catch(e) {
              console.error(e)
          }
      }

    useEffect(() => {
        fetchData({ currentUser })
    }, [])

    return(
    <SavedPageContainer>
        <SavedPlacesContainer>
            { saved.length > 0 ?
                saved.map(place => {
                place.location = { address: place.address , lat: place.latitude , lng: place.longitude }
                place.categories = new Array({name: place.category})
                console.log(place.categories)
                return (
                    <PlaceTile key={place.name} {...place} />
                )})
                :
            <h3>Log in to store your favourite places!</h3>

        }
        </SavedPlacesContainer>
        <SavedImageContainer>
            <SavedPageMapContainer>
            </SavedPageMapContainer>
        </SavedImageContainer>
    </SavedPageContainer>
)};

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
})

export default connect(mapStateToProps)(SavedPlaces);
