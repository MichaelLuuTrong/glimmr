//constant
const GET_ALL_USERS = "/user/GET_ALL_USERS"

//action creator
const getAllUsers = (users) => ({
    type: GET_ALL_USERS,
    users
})

//thunk
export const getAllUsersThunk = () => async (dispatch) => {
    try {
        const res = await fetch(`/api/users`);

        if (res.ok) {
            const allUsers = await res.json();
            dispatch(getAllUsers(allUsers));
            return allUsers
        };
    } catch (err) {
        const errors = await err.json();
        return errors
    }
}

//reducer
const initialState = { allUsers: {} }
const userReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case GET_ALL_USERS: {
            newState = { ...state, allUsers: {} }
            action.users.users.forEach((user) => {
                newState.allUsers[user.id] = user
            })
            return newState
        }
        default:
            return state
    }
}

export default userReducer
