import { useParams, NavLink } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { getUserThunk } from "../../store/user"
import './UserPageTop.css'


function UserPageTop() {
    const dispatch = useDispatch()
    const { userId } = useParams()
    const userObj = useSelector(state => state.userReducer.user)
    useEffect(() => {
        if (userId) {
            dispatch(getUserThunk(userId))
        }
    }, [dispatch, userId])



    return (
        <>
            <div className="profileCoverDiv">
                <div
                    className="backgroundImageDiv"
                    style={{
                        backgroundImage: `url(${userObj.cover_photo})`,
                    }}
                />
                <img
                    className='profileCoverProfilePicture'
                    src={userObj.profile_photo}
                    alt='Profile'
                />
                <div className='profileCoverName'>
                    {userObj.first_name} {userObj.last_name}
                </div>
                <div className='profileCoverUsername'>
                    {userObj.username}
                </div>
            </div>
            <div className='navLinksDiv'>
                <NavLink
                    className='bannerNavLink bannerAboutNavLink'
                    exact
                    to={`/people/${userId}/`}
                >
                    About
                </NavLink>
                <NavLink
                    className='bannerNavLink bannerPhotostreamNavLink'
                    exact
                    to={`/photos/${userId}/photostream`}
                >
                    Photostream
                </NavLink>
                <NavLink
                    className='bannerNavLink bannerAlbumsNavLink'
                    exact
                    to={`/photos/${userId}/albums`}
                >
                    Albums
                </NavLink>
                <NavLink
                    className='bannerNavLink bannerFavoritesNavLink'
                    exact
                    to={`/photos/${userId}/favorites/`}
                >
                    Favorites
                </NavLink>
            </div >
        </>
    );
}

export default UserPageTop
