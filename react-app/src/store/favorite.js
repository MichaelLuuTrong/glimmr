//constants
const POST_FAVORITE = "favorite/POST_FAVORITE"
const GET_USER_FAVORITES = "favorite/GET_USER_FAVORITES"
const DELETE_FAVORITE = "favorite/DELETE_FAVORITE"

//action creators
const postFavorite = (favorite) => ({
    type: POST_FAVORITE,
    favorite
});

const getUserFavorites = (favorites) => ({
    type: GET_USER_FAVORITES,
    favorites
})

const deleteFavorite = (favorite) => ({
    type: DELETE_FAVORITE,
    favorite
})

//thunks
export const postFavoriteThunk = (photo_id, user_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/favorites/${photo_id}/${user_id}`, {
            method: "POST"
        });

        if (res.ok) {
            const newFavorite = await res.json();
            dispatch(postFavorite(newFavorite))
            return newFavorite
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getUserFavoritesThunk = (user_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/favorites/${user_id}`)
        if (res.ok) {
            const favorites = await res.json();
            dispatch(getUserFavorites(favorites));
            return favorites
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const deleteFavoriteThunk = (photo_id, user_id) => async (dispatch) => {
    const res = await fetch(`/api/favorites/${photo_id}/${user_id}`, {
        method: "DELETE"
    });

    if (res.ok) {
        dispatch(deleteFavorite(photo_id, user_id))
        return
    }
};

//reducer
const initialState = { photoFavorites: {}, userFavorites: {} }

const favoriteReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case POST_FAVORITE: {
            console.log('POST_FAVORITE REDUCER HERE')
            newState = { ...state, photoFavorites: { ...state.photoFavorites } };
            newState.photoFavorites[action.favorite.id] = action.favorite;
            return newState
        }
        case GET_USER_FAVORITES: {
            if (!action.favorites || Object.keys(action.favorites).length === 0) {
                return { ...state, userFavorites: {} };
            }

            const newFavorites = { ...state.userFavorites }; // Copy the existing favorites

            for (const favoriteId in action.favorites) {
                if (action.favorites.hasOwnProperty(favoriteId)) {
                    newFavorites[favoriteId] = action.favorites[favoriteId];
                }
            }

            return { ...state, userFavorites: newFavorites };
        }
        case DELETE_FAVORITE: {
            newState = { ...state, photoFavorites: { ...state.photoFavorites } };
            delete newState.photoFavorites[action.favorite];
            return newState
        }
        default:
            return state
    }
}


export default favoriteReducer
