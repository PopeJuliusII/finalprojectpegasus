import StoreActionTypes from './store.types';
import { addItemToStore, removeItemFromStore } from './store.utils';

const INITIAL_STATE = {
  hidden: true,
  storeItems: []
};

const storeReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case StoreActionTypes.TOGGLE_STORE_HIDDEN:
      return {
        ...state,
        hidden: !state.hidden
      };
    case StoreActionTypes.ADD_ITEM:
      return {
        ...state,
        storeItems: addItemToStore(state.storeItems, action.payload)
      };
    case StoreActionTypes.REMOVE_ITEM:
      return {
        ...state,
        storeItems: removeItemFromStore(state.storeItems, action.payload)
      };
    case StoreActionTypes.CLEAR_ITEM_FROM_STORE:
      return {
        ...state,
        storeItems: state.storeItems.filter(
          storeItem => storeItem.id !== action.payload.id
        )
      };
    default:
      return state;
  }
};

export default storeReducer;
