import { SavedActionTypes } from './saved.types';

const INITIAL_STATE = {
    savedPlaces: null
};

const savedReducer = ( state = INITIAL_STATE, action ) => {
    switch( action.type ){
        case SavedActionTypes.SET_SAVED_PLACES:
            return{
                ...state,
                savedPlaces: action.payload
            }
        default:
            return state
    }
};

export default savedReducer
