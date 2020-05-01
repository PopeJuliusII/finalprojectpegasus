import React from 'react';

import './stored-place.styles.scss'

const StoredPlace = ({ item: { imageUrl, price, name, quantity }}) => (
    <div className='store-place'>
        <img src={imageUrl} alt='item' />
        <div className='place-details'>
            <span className='name'>{name}</span>
            <span className='price'>
                {quantity} x ${price}
            </span>
        </div>
    </div>
)

export default StoredPlace;
