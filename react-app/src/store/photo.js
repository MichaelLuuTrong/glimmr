//constants
const POST_PHOTO = "photo/POST_PHOTO"
const GET_PHOTO = "photo/GET_PHOTO"
const GET_USER_PHOTOS = "photo/GET_USER_PHOTOS"
const GET_ALL_PHOTOS = "photo/GET_ALL_PHOTOS"
const PATCH_PHOTO = "photo/PATCH_PHOTO"
const DELETE_PHOTO = "photo/DELETE_PHOTO"

//action creators
const postPhoto = (photo) => ({
    type: POST_PHOTO,
    photo
});

const getPhoto = (photo) => ({
    type: GET_PHOTO,
    photo
})

const getUserPhotos = (photos) => ({
    type: GET_USER_PHOTOS,
    photos
})

const getAllPhotos = (photos) => ({
    type: GET_ALL_PHOTOS,
    photos
})

const patchPhoto = (photo) => ({
    type: PATCH_PHOTO,
    photo
})

const deletePhoto = (photo_id) => ({
    type: DELETE_PHOTO,
    photo_id
})

//thunks
export const postPhotoThunk = (photo, user) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/${user.id}/photos`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(photo)
        });

        if (res.ok) {
            const newPhoto = await res.json();
            dispatch(postPhoto(newPhoto));
            return newPhoto
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getPhotoThunk = (photoId) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/${photoId}`);

        if (res.ok) {
            const photo = await res.json();
            dispatch(getPhoto(photo));
            return photo
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getUserPhotosThunk = (user_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/user/${user_id}`);

        if (res.ok) {
            const userPhotos = await res.json();
            dispatch(getUserPhotos(userPhotos));
            return userPhotos
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getAllPhotosThunk = () => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos`);

        if (res.ok) {
            const allPhotos = await res.json();
            dispatch(getAllPhotos(allPhotos));
            return allPhotos
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const patchPhotoThunk = (photo, photoId) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/${photoId}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(photo)
        })

        if (res.ok) {
            const updatedPhoto = await res.json();
            dispatch(patchPhoto(updatedPhoto));
            return updatedPhoto
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const deletePhotoThunk = (photo_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/${photo_id}`, {
            method: "DELETE"
        });

        if (res.ok) {
            dispatch(deletePhoto(photo_id));
            return
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

//reducer
const initialState = { allPhotos: {}, singlePhoto: {}, userPhotos: {} }

const photoReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case POST_PHOTO: {
            newState = { ...state, userPhotos: { ...state.userPhotos } }
            newState.singlePhoto = action.photo
            return newState
        }
        case GET_PHOTO: {
            newState = { ...state, singlePhoto: { ...state.singlePhoto } }
            newState.singlePhoto = action.photo
            return newState
        }
        case GET_USER_PHOTOS: {
            newState = { ...state, userPhotos: { ...state.userPhotos } }
            newState.userPhotos = action.photos
            return newState
        }
        case GET_ALL_PHOTOS: {
            newState = { ...state, allPhotos: {} }
            action.photos.photos.forEach((photo) => {
                newState.allPhotos[photo.id] = photo
            })
            return newState
        }
        case PATCH_PHOTO: {
            newState = { ...state, allPhotos: { ...state.allPhotos }, userPhotos: { ...state.userPhotos } }
            const updatedPhoto = action.photo
            newState.allPhotos[updatedPhoto.id] = updatedPhoto;
            if (newState.userPhotos[updatedPhoto.id]) {
                newState.userPhotos[updatedPhoto.id] = { ...newState.userPhotos[updatedPhoto.id], ...updatedPhoto };
            }
            return newState
        }
        case DELETE_PHOTO: {
            newState = { ...state, userPhotos: { ...state.userPhotos } }
            delete newState.userPhotos[action.photo_id]
            return newState
        }
        default:
            return state
    }
}

export default photoReducer
