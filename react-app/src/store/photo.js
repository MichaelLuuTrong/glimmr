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
        })

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
        const res = await fetch(`/api/photos/${photoId}`)

        if (res.ok) {
            const photo = await res.json();
            dispatch(getPhoto(photo))
            return photo
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getUserPhotosThunk = (user_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/user/${user_id}`)

        if (res.ok) {
            const userPhotos = await res.json()
            dispatch(getUserPhotos(userPhotos))
            return userPhotos
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getAllPhotosThunk = () => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos`)

        if (res.ok) {
            const allPhotos = await res.json();
            dispatch(getAllPhotos(allPhotos))
            return allPhotos
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const patchPhotoThunk = (photo, photoId) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/${photoId}/update`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(photo)
        })

        if (res.ok) {
            const updatedPhoto = await res.json();
            dispatch(patchPhoto(updatedPhoto))
            return updatedPhoto
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const deletePhotoThunk = (photo_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/photos/delete/${photo_id}`, {
            method: "DELETE"
        })

        if (res.ok) {
            dispatch(deletePhoto(photo_id))
            return
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

//reducer
const initialState = {
    photos: {},

}

const photoReducer = (state = initialState, action) => {
    let newState = {}
}



export default photoReducer
