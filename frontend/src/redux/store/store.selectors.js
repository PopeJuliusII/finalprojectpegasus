import { createSelector } from 'reselect';

const selectStore = state => state.store;

export const selectStoreItems = createSelector(
  [selectStore],
  store => store.storeItems
);

export const selectStoreHidden = createSelector(
  [selectStore],
  store => store.hidden
);

export const selectStoreItemsCount = createSelector(
  [selectStoreItems],
  storeItems =>
    storeItems.reduce(
      (accumalatedQuantity, storeItem) =>
        accumalatedQuantity + storeItem.quantity,
      0
    )
);

export const selectStoreTotal = createSelector(
  [selectStoreItems],
  storeItems =>
    storeItems.reduce(
      (accumalatedQuantity, storeItem) =>
        accumalatedQuantity + storeItem.quantity * storeItem.price,
      0
    )
);
