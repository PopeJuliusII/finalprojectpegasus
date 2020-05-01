import React from 'react';
import { connect } from 'react-redux';

import { clearItemFromStore, addItem, removeItem } from '../../redux/store/store.actions'

import './checkout-item.styles.scss'

const CheckoutItem = ({ storeItem, clearItem, addItem, removeItem }) => {
    const { name, imageUrl, price, quantity } = storeItem;
    return (
        <div className='checkout-item'>
            <div className='image-container'>
                <img src={`${imageUrl}`} alt='item' />
            </div>
            <span className='name'>{ name }</span>
            <span className='quantity'>
                <div className='arrow' onClick={() => removeItem(storeItem)}>&#10094;</div>
                <span className='value'>{ quantity }</span>
                <div className='arrow' onClick={() => addItem(storeItem)}>&#10095;</div>
            </span>
            <span className='price'>{ price }</span>
            <span className='remove-button' onClick={() => clearItem(storeItem)}>&#10005;</span>
        </div>
)}

const mapDispatchToProps = dispatch => ({
    clearItem: item => dispatch(clearItemFromStore(item)),
    addItem: item => dispatch(addItem(item)),
    removeItem: item => dispatch(removeItem(item))
})

export default connect(null, mapDispatchToProps)(CheckoutItem);
