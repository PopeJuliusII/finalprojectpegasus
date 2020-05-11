import SavedActionTypes from './saved.types';

export const fetchSavedStart = () => ({
    type: SavedActionTypes.FETCH_SAVED_START,
});

export const fetchSavedSuccess = savedPlaces => ({
    type: SavedActionTypes.FETCH_SAVED_SUCCESS,
    payload: savedPlaces
})

export const fetchSavedFailure = errorMessage => ({
    type: SavedActionTypes.FETCH_SAVED_FAILURE,
    payload: errorMessage
})

export const fetchSavedStartAsync = async () => {
    return dispatch => {
        try{
        const email = 'a@a.com'
        const id = 'C4C4'
        dispatch(fetchSavedStart());
        const response = await fetch(`https://localhost5000/get_data/${id}/${email}`)
        const savedPlaces = await response.json()
        dispatch(fetchSavedSuccess(savedPlaces));
    } catch (error) {
        dispatch(fetchSavedFailure(error.message)))
    }
}
}
