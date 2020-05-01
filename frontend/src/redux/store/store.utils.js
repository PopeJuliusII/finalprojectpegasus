export const addItemToStore = (storeItems, storeItemToAdd) => {
  const existingStoreItem = storeItems.find(
    storeItem => storeItem.id === storeItemToAdd.id
  );

  if (existingStoreItem) {
    return storeItems.map(storeItem =>
      storeItem.id === storeItemToAdd.id
        ? { ...storeItem, quantity: storeItem.quantity + 1 }
        : storeItem
    );
  }

  return [...storeItems, { ...storeItemToAdd, quantity: 1 }];
};

export const removeItemFromStore = (storeItems, storeItemToRemove) => {
  const existingStoreItem = storeItems.find(
    storeItem => storeItem.id === storeItemToRemove.id
  );

  if (existingStoreItem.quantity === 1) {
    return storeItems.filter(storeItem => storeItem.id !== storeItemToRemove.id);
  }

  return storeItems.map(storeItem =>
    storeItem.id === storeItemToRemove.id
      ? { ...storeItem, quantity: storeItem.quantity - 1 }
      : storeItem
  );
};
