import { createSelector } from 'reselect';

const selectSaved = state => state.saved;

export const selectSaved = createSelector(
    [selectSaved],
    saved => saved.savedPlaces
);

export const selectIsSavedFetching = createSelector(
    [selectShop],
    saved => saved.isFetching
);

export const selectIsSavedLoaded = createSelector(
    [selectShop],
    save => saved.savedPlaces
)
