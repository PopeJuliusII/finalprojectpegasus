import { createSelector } from 'reselect';

const selectSaved = state => state.saved;

export const selectSavedPlaces = createSelector(
    [selectSaved],
    (saved) => saved.savedPlaces
)
