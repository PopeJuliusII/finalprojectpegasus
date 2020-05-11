import { combineReducers } from 'redux';
import { persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

import userReducer from './user/user.reducer';
import storeReducer from './store/store.reducer';
import savedReducer from './saved/saved.reducer';


const persistConfig = {
    key: 'root',
    storage,
    whitelist: ['store']
}

const rootReducer = combineReducers({
    user: userReducer,
    store: storeReducer,
    saved: savedReducer
});

export default persistReducer(persistConfig, rootReducer)
