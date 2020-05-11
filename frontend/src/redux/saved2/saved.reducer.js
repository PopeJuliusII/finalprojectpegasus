import SavedActionTypes from './saved.types';

const INITIAL_STATE = {
    saved: null,
    isFetching: false,
    errorMessage: undefined
};

const savedReducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case SavedActionTypes.FETCH_SAVED_START:
            return{
                ...state,
                isFetching: true
            }
        case SavedActionTypes.FETCH_SAVED_SUCCESS:
            return{
                ...state,
                isFetching: false,
                saved: action.payload
            }
        default:
            return state
    }
};

export default savedReducer;
