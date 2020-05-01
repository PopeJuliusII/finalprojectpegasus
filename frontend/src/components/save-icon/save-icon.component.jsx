import React from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';

import { toggleStoreHidden } from '../../redux/store/store.actions';
import { selectStoreItemsCount } from '../../redux/store/store.selectors'

import { ReactComponent as Heart } from '../../assets/heart.svg';


import './save-icon.styles.scss'

const SaveIcon = ({ toggleStoreHidden, itemCount }) =>(
    <div className='save-icon' onClick={toggleStoreHidden}>
        <Heart className='heart-icon'/>
        <span className='place-count'>{itemCount}</span>
    </div>
);

const mapDispatchToProps = dispatch => ({
        toggleStoreHidden: () => dispatch(toggleStoreHidden())
})

const mapStateToProps = createStructuredSelector({
    itemCount: selectStoreItemsCount
})

export default connect(mapStateToProps, mapDispatchToProps)(SaveIcon);
