import React from 'react';

import { Tiling, TogglePart } from './pref-tile.styles';
import './pref-tile.scss';

const PrefTile = ({ name, sentiment, handleChange }) => {
    return (
        <Tiling>
            <TogglePart>
                <label className="switch">
                    <input type="checkbox" checked={sentiment} onChange={handleChange}/>
                    <span className="slider round"></span>
                </label>
            </TogglePart>
            <div className='place-details'>
                <div className='name'>{name}</div>
            </div>
        </Tiling>
)}

export default PrefTile;
