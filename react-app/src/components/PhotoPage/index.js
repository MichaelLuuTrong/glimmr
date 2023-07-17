import { useParams, NavLink, useHistory } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { getPhotoThunk } from "../../store/photo"
import { getPhotoCommentsThunk } from "../../store/comment"
import { getAllUsersThunk } from "../../store/user"
import "./PhotoPage.css"

function timeSinceCommentDate(commentDate) {
    const now = new Date();
    const past = new Date(commentDate);
    const timeDifference = now - past;
    const millisecondsPerHour = 1000 * 60 * 60;
    const millisecondsPerDay = millisecondsPerHour * 24;
    const millisecondsPerMonth = millisecondsPerDay * 30;
    const millisecondsPerYear = millisecondsPerDay * 365;

    if (timeDifference < millisecondsPerDay) {
        const hours = Math.floor(timeDifference / millisecondsPerHour);
        return hours + "h";
    } else if (timeDifference < millisecondsPerMonth) {
        const days = Math.floor(timeDifference / millisecondsPerDay);
        return days + "d";
    } else if (timeDifference < millisecondsPerYear * 2) {
        const months = Math.floor(timeDifference / millisecondsPerMonth);
        return months + "m";
    } else {
        const years = Math.floor(timeDifference / millisecondsPerYear);
        return years + "y";
    }
}

function convertDate(dateString) {
    const months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    const date = new Date(dateString);
    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear();

    return `${month} ${day}, ${year}`;
}

function getFirstNameById(usersArray, id) {
    const user = usersArray.find(user => user.id === id);
    return user ? user.first_name : null;
}

function getLastNameById(usersArray, id) {
    const user = usersArray.find(user => user.id === id);
    return user ? user.last_name : null;
}

function getProfilePhotoById(usersArray, id) {
    const user = usersArray.find(user => user.id === id);
    return user ? user.profile_photo : null;
}

function PhotoPage() {
    const history = useHistory()
    const dispatch = useDispatch()
    const { photoId } = useParams()
    const photoObj = useSelector(state => state.photoReducer.singlePhoto)
    const commentsObj = useSelector(state => state.commentReducer.photoComments)
    const commentsArray = Object.values(commentsObj)
    const usersObj = useSelector(state => state.userReducer.allUsers)
    const usersArray = Object.values(usersObj)
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(getPhotoThunk(photoId))
        dispatch(getPhotoCommentsThunk(photoId))
        dispatch(getAllUsersThunk())
    }, [dispatch, photoId])

    if (!photoObj) return null
    console.log("COMMENTS ARRAY:", commentsArray)
    console.log("photoObj:", photoObj)
    return (
        <div className="wholePhotoDiv">
            <div className='mainPhotoDiv'>
                <img className='mainPhoto' src={photoObj.photo} />
            </div >
            <div className="photoMainInfoDiv">
                <div className="photoMainInfoDivLeft">
                    <NavLink className="photoPhotographerName" exact to={`/photos/${photoObj.user_id}/photostream`}>
                        {getFirstNameById(usersArray, photoObj.user_id)} {getLastNameById(usersArray, photoObj.user_id)}
                    </NavLink>
                    <div className="photographerPhotoProfileImgAndHoverTransparency">
                        <div className="photographerPhotoProfileHoverTransparency"></div>
                        <img
                            onClick={() => history.push(`/photos/${photoObj.user_id}/photostream`)}
                            className="photographerPhotoProfilePhotoImg changeCursor"
                            src={getProfilePhotoById(usersArray, photoObj.user_id)}
                            alt="Photographer" />
                    </div>
                    <div className="photoTitle">
                        {photoObj.title}
                    </div>
                    <div className="photoDescription">
                        {photoObj.description}
                    </div>
                </div>
                <div className="photoMainInfoDivRight">
                    <div className="photoFavorites">
                        <div className="photoFavoritesCount">{photoObj.favorites_count}</div>
                        <div className="photoFavoritesText">
                            {photoObj.favorites_count === 1 ? 'Favorite' : 'Favorites'}
                        </div>
                    </div>
                    <div className="photoComments">
                        <div className="photoCommentsCount">{photoObj.comments_count}</div>
                        <div className="photoCommentsText">
                            {photoObj.comments_count === 1 ? 'Comment' : 'Comments'}
                        </div>
                    </div>
                    <div className="photoDates">
                        <div className="photoUploadDate">Uploaded on {convertDate(photoObj.created_at)}</div>
                        <div className="photoTakenDate">Taken on {convertDate(photoObj.taken_at)}</div>
                    </div>
                </div>
            </div>
            <div className="allCommentsDiv">
                {commentsArray.map(comment => (
                    <div className="wholeCommentDiv" key={comment.id}>
                        <NavLink exact to={`/ photos / ${comment.user.id} /photostream`}>
                            <div className="commentUserNameDiv">{comment.user.first_name} {comment.user.last_name}</div>
                        </NavLink>
                        <img className="commentUserProfilePhoto" src={comment.user.profile_photo} />
                        <div className="timeSinceComment" >{timeSinceCommentDate(comment.created_at)}</div>
                        <div className="commentTextDiv">{comment.text}</div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default PhotoPage
