import { useEffect } from "react"
import "./Explore.css"
import { useDispatch, useSelector } from "react-redux"
import { getAllPhotosThunk } from "../../store/photo"
import { getAllUsersThunk } from "../../store/user"
import { useHistory } from "react-router-dom"

function Explore() {
    const photosObj = useSelector(state => state.photoReducer.allPhotos);
    const usersObj = useSelector(state => state.userReducer.allUsers)
    const photosArray = Object.values(photosObj)
    const usersArray = Object.values(usersObj)
    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(() => {
        dispatch(getAllPhotosThunk())
        dispatch(getAllUsersThunk())
    }, [dispatch]);

    function getFirstNameById(usersArray, id) {
        const user = usersArray.find(user => user.id === id);
        return user ? user.first_name : null;
    }

    function getLastNameById(usersArray, id) {
        const user = usersArray.find(user => user.id === id);
        return user ? user.last_name : null;
    }

    function sortByCreatedAt(array) {
        return array.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
    }

    return (
        <>
            <div className='spacerDiv'></div>
            <div className='fullExplorePage'>
                <h1 className='exploreHeader'>Explore</h1>
                <div className='masonryDiv'>
                    {sortByCreatedAt(photosArray).reverse().map((photo, id) => {
                        return (
                            <div onClick={() =>
                                history.push(`/photos/${photo.id}`)} key={id}
                                className="photoWithHoverDiv changeCursor">
                                <div className='divOverPhotoExplore'>
                                    <div className='leftSideHoverInfo'>
                                        <div className='hoverPhotoTitle'>
                                            {photo.title}</div>
                                        <div className='hoverPhotoTakerName'>
                                            by {getFirstNameById(usersArray, photo.user_id)}
                                            {" "}
                                            {getLastNameById(usersArray, photo.user_id)}
                                        </div>
                                    </div>
                                    <div className='rightSideHoverInfo'>
                                        <div className='hoverFavoriteCount'>
                                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.6 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z" /></svg>
                                            {photo.favorites_count}</div>
                                        <div className='hoverCommentCount'>
                                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><path d="M123.6 391.3c12.9-9.4 29.6-11.8 44.6-6.4c26.5 9.6 56.2 15.1 87.8 15.1c124.7 0 208-80.5 208-160s-83.3-160-208-160S48 160.5 48 240c0 32 12.4 62.8 35.7 89.2c8.6 9.7 12.8 22.5 11.8 35.5c-1.4 18.1-5.7 34.7-11.3 49.4c17-7.9 31.1-16.7 39.4-22.7zM21.2 431.9c1.8-2.7 3.5-5.4 5.1-8.1c10-16.6 19.5-38.4 21.4-62.9C17.7 326.8 0 285.1 0 240C0 125.1 114.6 32 256 32s256 93.1 256 208s-114.6 208-256 208c-37.1 0-72.3-6.4-104.1-17.9c-11.9 8.7-31.3 20.6-54.3 30.6c-15.1 6.6-32.3 12.6-50.1 16.1c-.8 .2-1.6 .3-2.4 .5c-4.4 .8-8.7 1.5-13.2 1.9c-.2 0-.5 .1-.7 .1c-5.1 .5-10.2 .8-15.3 .8c-6.5 0-12.3-3.9-14.8-9.9c-2.5-6-1.1-12.8 3.4-17.4c4.1-4.2 7.8-8.7 11.3-13.5c1.7-2.3 3.3-4.6 4.8-6.9c.1-.2 .2-.3 .3-.5z" /></svg>
                                            {photo.comments_count}</div>
                                    </div>
                                </div>
                                <img
                                    className='displayPhoto'
                                    src={photo.photo}
                                    style={{ height: 250 }}
                                    alt=''
                                />
                            </div>
                        );
                    })}
                </div>
            </div >
        </>
    )
}

export default Explore
