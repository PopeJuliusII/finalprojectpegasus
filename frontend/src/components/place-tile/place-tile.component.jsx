import React from 'react';

import { Tiling } from './place-tile.styles';
import './place-tile.scss';

const PlaceTile = ({ name, location : { address, lat, lng }, categories }) => {

    return (
        <Tiling>
            <div className='place-details'>
                <div className='name'>{name}</div>
                <div className='details'><strong>{categories[0].name}</strong></div>
                <div className='details'><strong>Address:</strong> {address}</div>
                <div className='details'><strong>Latitude:</strong> {lat}</div>
                <div className='details'><strong>Longitude:</strong> {lng}</div>
            </div>
        </Tiling>
)}

export default PlaceTile
