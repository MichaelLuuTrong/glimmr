//constants
const GET_ALL_USERS = "/user/GET_ALL_USERS"
const GET_USER = "/user/GET_USER"

//action creators
const getAllUsers = (users) => ({
    type: GET_ALL_USERS,
    users
})

const getUser = user => ({
    type: GET_USER,
    user
})

//thunks
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

export const getUserThunk = (user_id) => async (dispatch) => {
    try {
        const res = await fetch(`/api/users/${user_id}`)
        if (res.ok) {
            const user = await res.json()
            dispatch(getUser(user))
            return user
        }
    } catch (err) {
        return err
    }
}

//reducers
const initialState = { allUsers: {}, user: {} }
const userReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case GET_USER: {
            return { ...state, user: action.user }; // Update user in the state with action.user
        }
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
