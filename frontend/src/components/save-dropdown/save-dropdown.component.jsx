
import React from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import { withRouter } from 'react-router-dom';

import CustomButton from '../custom-button/custom-button.component';
import StoredPlace from '../stored-place/stored-place.component';
import { selectStoreItems } from '../../redux/store/store.selectors';
import { toggleStoreHidden } from '../../redux/store/store.actions';

import './save-dropdown.styles.scss';

const SaveDropdown = ({ storeItems, history, dispatch }) => (
  <div className='save-dropdown'>
    <div className='save-places'>
      {
         storeItems.length ? (
         storeItems.map(storeItem => (
        <StoredPlace key={storeItem.id} item={storeItem} />
      )))
      : (<span className='empty-message'>Nothing saved yet!</span>)}

    </div>
    <CustomButton onClick={() => {
            history.push('/saved');
            dispatch(toggleStoreHidden())
        }}>GO TO SAVED</CustomButton>
  </div>
);

const mapStateToProps = createStructuredSelector({
  storeItems: selectStoreItems
});

export default withRouter(connect(mapStateToProps)(SaveDropdown));
