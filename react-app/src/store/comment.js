//constants
const POST_COMMENT = "comment/POST_COMMENT"
const GET_COMMENT = "comment/GET_COMMENT"
const GET_PHOTO_COMMENTS = "comment/GET_PHOTO_COMMENTS"
const PATCH_COMMENT = "comment/PATCH_COMMENT"
const DELETE_COMMENT = "comment/DELETE_COMMENT"

//action creators
const postComment = (comment) => ({
    type: POST_COMMENT,
    comment
})

const getPhotoComments = (comments) => ({
    type: GET_PHOTO_COMMENTS,
    comments
})

const getComment = (comment) => ({
    type: GET_COMMENT,
    comment
})

const patchComment = (comment) => ({
    type: PATCH_COMMENT,
    comment
})

const deleteComment = (comment) => ({
    type: DELETE_COMMENT,
    comment
})

//thunks
export const postCommentThunk = (photo_id, user_id, comment) => async (dispatch) => {
    try {
        const res = await fetch(`/api/comments/${photo_id}/${user_id}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(comment)
        });

        if (res.ok) {
            const newComment = await res.json();
            dispatch(postComment(newComment));
            return newComment
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const getCommentThunk = (comment_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/comments/comment/${comment_id}`)
        if (res.ok) {
            const comment = await res.json();
            dispatch(getComment(comment));
            return comment;
        }
    } catch (err) {
        const errors = err.json();
        return errors;
    }
}

export const getPhotoCommentsThunk = (photo_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/comments/${photo_id}`)
        if (res.ok) {
            const photoComments = await res.json();
            dispatch(getPhotoComments(photoComments.comments));
            return photoComments.comments
        }
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const patchCommentThunk = (comment, comment_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/comments/${comment_id}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(
                { text: comment }),
        });

        if (res.ok) {
            const updatedComment = await res.json();
            dispatch(patchComment(updatedComment));
            return updatedComment
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

export const deleteCommentThunk = (comment_id) => async (dispatch) => {
    const res = await fetch(`/api/comments/${comment_id}`, {
        method: "DELETE"
    });

    if (res.ok) {
        dispatch(deleteComment(comment_id));
        return
    }
};


//reducer
const initialState = { photoComments: {}, singleComment: {} }

const commentReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case POST_COMMENT: {
            newState = { ...state, photoComments: { ...state.photoComments } };
            newState.photoComments[action.comment.id] = action.comment;
            return newState
        }
        case GET_COMMENT: {
            newState = { ...state, singleComment: { ...state.singleComment } };
            newState.singleComment = action.comment;
            return newState;
        }
        case GET_PHOTO_COMMENTS: {
            if (action.comments.length === 0) {
                return { ...state, photoComments: {} }
            }
            newState = { ...state, photoComments: {} };
            action.comments.forEach((comment) => {
                newState.photoComments[comment.id] = comment;
            });
            return newState;
        }
        case PATCH_COMMENT: {
            newState = { ...state, singleComment: { ...state.singleComment } };
            const updatedComment = action.comment;
            return { ...state, singleComment: { ...updatedComment } }
        }
        case DELETE_COMMENT: {
            newState = { ...state, photoComments: { ...state.photoComments } };
            delete newState.photoComments[action.comment];
            return newState
        }
        default:
            return state
    }
}

export default commentReducer
