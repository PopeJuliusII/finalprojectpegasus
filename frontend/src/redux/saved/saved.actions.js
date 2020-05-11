import { SavedActionTypes } from './saved.types';

export const setSavedPlaces = saved => ({
    type: SavedActionTypes.SET_SAVED_PLACES,
    payload: saved
})
