import { useParams, NavLink, useHistory } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"
import { getPhotoThunk } from "../../store/photo"
import { deleteCommentThunk, getPhotoCommentsThunk, postCommentThunk } from "../../store/comment"
import { getAllUsersThunk } from "../../store/user"
import "./PhotoPage.css"

function timeSinceCommentDate(commentDate) {
    const now = new Date();
    const past = new Date(commentDate);
    const timeDifference = now - past;
    const millisecondsPerDay = 1000 * 60 * 60 * 24;
    const millisecondsPerMonth = millisecondsPerDay * 30;
    const millisecondsPerYear = millisecondsPerDay * 365;

    //I would do hours but my current implementation of datetime using datetime.now() does not include
    //time, just year, month, and days.

    if (timeDifference < millisecondsPerDay) {
        return "Today";
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
    const usersObj = useSelector(state => state.userReducer.allUsers)
    const usersArray = Object.values(usersObj)
    const user = useSelector(state => state.session.user)
    const [commentText, setCommentText] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        let commentObject = {
            text: commentText
        }
        dispatch(postCommentThunk(photoId, user.id, commentObject))
        setCommentText("")
    }

    useEffect(() => {
        dispatch(getPhotoThunk(photoId))
        dispatch(getPhotoCommentsThunk(photoId))
        dispatch(getAllUsersThunk())
    }, [dispatch, photoId])

    const handleDeleteComment = (commentId) => {
        dispatch(deleteCommentThunk(commentId))
    };

    return (
        <div className="wholePhotoDiv">
            <div className='mainPhotoDiv'>
                <img className='mainPhoto' src={photoObj.photo} />
            </div >
            <div className='photoInfoAndCommentsDiv'>
                <div className='photoInfoTop'>
                    <div className="photoMainInfoDiv">
                        <div className="photoMainInfoDivLeft">
                            <div className="photographerPhotoProfileImgAndHoverTransparency">
                                <div className="photographerPhotoProfileHoverTransparency"></div>
                                <img
                                    onClick={() => history.push(`/photos/${photoObj.user_id}/photostream`)}
                                    className="photographerPhotoProfilePhotoImg changeCursor"
                                    src={getProfilePhotoById(usersArray, photoObj.user_id)}
                                    alt="Photographer" />
                            </div>
                            <div className='photoImportantInfoDiv'>
                                <NavLink className="photoPhotographerName" exact to={`/photos/${photoObj.user_id}/photostream`}>
                                    {getFirstNameById(usersArray, photoObj.user_id)} {getLastNameById(usersArray, photoObj.user_id)}
                                </NavLink>
                                <div className="photoTitle">
                                    {photoObj.title}
                                </div>
                                <div className="photoDescription">
                                    {photoObj.description}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="photoMainInfoDivRight">
                        <div className='mainInfoDivInfo'>
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
                        <div className="grayBorder"></div>
                    </div>
                </div>
                <div className='commentsSection'>
                    <div className="allCommentsDiv">
                        {(Object.values(commentsObj)).map(comment => (
                            <div className="wholeCommentDiv" key={comment.id}>
                                {comment.user_id === user.id &&
                                    <div className="deleteCommentButtonIcon"
                                        onClick={() => handleDeleteComment(comment.id)}>
                                        <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512"><path d="M170.5 51.6L151.5 80h145l-19-28.4c-1.5-2.2-4-3.6-6.7-3.6H177.1c-2.7 0-5.2 1.3-6.7 3.6zm147-26.6L354.2 80H368h48 8c13.3 0 24 10.7 24 24s-10.7 24-24 24h-8V432c0 44.2-35.8 80-80 80H112c-44.2 0-80-35.8-80-80V128H24c-13.3 0-24-10.7-24-24S10.7 80 24 80h8H80 93.8l36.7-55.1C140.9 9.4 158.4 0 177.1 0h93.7c18.7 0 36.2 9.4 46.6 24.9zM80 128V432c0 17.7 14.3 32 32 32H336c17.7 0 32-14.3 32-32V128H80zm80 64V400c0 8.8-7.2 16-16 16s-16-7.2-16-16V192c0-8.8 7.2-16 16-16s16 7.2 16 16zm80 0V400c0 8.8-7.2 16-16 16s-16-7.2-16-16V192c0-8.8 7.2-16 16-16s16 7.2 16 16zm80 0V400c0 8.8-7.2 16-16 16s-16-7.2-16-16V192c0-8.8 7.2-16 16-16s16 7.2 16 16z" /></svg>
                                    </div>
                                }
                                <img className="commentUserProfilePhoto changeCursor" src={comment.user.profile_photo} onClick={() => history.push(`/photos/${comment.user.id}/photostream`)} />
                                <div className='commentUserNameandTimeAndComment'>
                                    <div className="commentUserNameAndTime">
                                        <NavLink className="commentUserNameDiv" exact to={`/photos/${comment.user.id}/photostream`}>
                                            {comment.user.first_name} {comment.user.last_name}
                                        </NavLink>
                                        <div className="timeSinceComment" >{timeSinceCommentDate(comment.created_at)}</div>
                                    </div>
                                    <div className="commentTextDiv">{comment.text}</div>
                                </div>
                            </div>
                        ))}
                        {user && <div className="newCommentDiv">
                            <form onSubmit={handleSubmit}
                                className="commentForm">
                                <img className="commentUserProfilePhoto"
                                    src={getProfilePhotoById(usersArray, user.id)}
                                    alt="User Profile"
                                />
                                <div className="commentFormRightSide">
                                    <textarea
                                        className="commentTextInput"
                                        type="text"
                                        placeholder="Add a comment"
                                        value={commentText}
                                        onChange={(e) => setCommentText(e.target.value)}
                                    />
                                    {/* The trim below makes sure the comment has text in it */}
                                    {commentText.trim() !== "" && (
                                        < button className="submitCommentButton" type="submit">
                                            Comment
                                        </button>
                                    )}
                                </div>
                            </form>
                        </div>
                        }
                    </div>
                </div>
            </div >
        </div >
    )
}

export default PhotoPage
