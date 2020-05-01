import StoreActionTypes from './store.types';

export const toggleStoreHidden = () => ({
  type: StoreActionTypes.TOGGLE_STORE_HIDDEN
});

export const addItem = item => ({
  type: StoreActionTypes.ADD_ITEM,
  payload: item
});

export const removeItem = item => ({
  type: StoreActionTypes.REMOVE_ITEM,
  payload: item
});

export const clearItemFromStore = item => ({
  type: StoreActionTypes.CLEAR_ITEM_FROM_STORE,
  payload: item
});
