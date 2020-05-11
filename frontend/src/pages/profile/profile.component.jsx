import React, { useEffect, useState } from 'react';

import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import { selectCurrentUser } from "../../redux/user/user.selectors";

import { ProfilePageContainer, ProfilePageMapContainer, ProfilePlacesContainer, ProfileImageContainer } from './profile.styles.jsx';

import PrefTile from '../../components/pref-tile/pref-tile.component';


const Profile = ({ currentUser }) => {
    const [preferences, setPreferences] = useState(false)

    const fetchData = async ({ currentUser }) => {
          const url = 'http://localhost:5000/get_data'
          try {
              const response = await fetch(
                  currentUser
                  ? `${url}/${currentUser.id}/${currentUser.email}`
                  : null
              );
              const output = await response.json()
              setPreferences(output.data.prefs)
          } catch(e) {
              console.error(e)
          }
      }

    useEffect(() => {
        fetchData({ currentUser })
    }, [])

    const handleChange = event => {
        console.log(event)
        const { name, sentiment } = event.target;
        console.log(event.target.name)
        console.log('hello, Greg!')
    }

    return(
    <div>
        <ProfilePageContainer>
            <ProfilePlacesContainer>
                {preferences ?
                    Object.keys(preferences).map(function(key, index){
                    console.log(`${key} : ${preferences[key]}`)
                    return <PrefTile key={key} handleChange={handleChange} name={key} sentiment={preferences[key]} />
                    })
                    :
                    <h3>Log in to set your preferences!</h3>
                }
        </ProfilePlacesContainer>
            {console.log(preferences)}
            <ProfileImageContainer>
                <ProfilePageMapContainer>
                </ProfilePageMapContainer>
            </ProfileImageContainer>
        </ProfilePageContainer>
    </div>
)};

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
})

export default connect(mapStateToProps)(Profile);
