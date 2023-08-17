import { useParams, NavLink, useHistory } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"
import { getPhotoThunk } from "../../store/photo"
import { getPhotoCommentsThunk, postCommentThunk } from "../../store/comment"
import { getAllUsersThunk } from "../../store/user"
import { postFavoriteThunk, deleteFavoriteThunk, getUserFavoritesThunk } from "../../store/favorite"
import "./PhotoPage.css"
import OpenModalButton from "../OpenModalButton"
import DeleteCommentModal from "../DeleteCommentModal"
import UpdateCommentModal from "../UpdateCommentModal"

function timeSinceCommentDate(commentDate) {
    const now = new Date();
    const past = new Date(commentDate);
    const timeDifference = now - past - 86400000;
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
    date.setDate(date.getDate() + 1) //Adds one day to account for timezone issue
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
    const userFavorites = useSelector(state => state.favoriteReducer.userFavorites)
    const [commentText, setCommentText] = useState("")

    const handleFavorite = async (e) => {
        e.preventDefault();
        await dispatch(postFavoriteThunk(photoId, user.id));
        await dispatch(getUserFavoritesThunk(user.id))
        await dispatch(getPhotoThunk(photoId));
    };

    const handleUnfavorite = async (e) => {
        e.preventDefault();
        await dispatch(deleteFavoriteThunk(photoId, user.id));
        await dispatch(getUserFavoritesThunk(user.id))
        await dispatch(getPhotoThunk(photoId));
    };

    const handleSubmit = (e) => {
        e.preventDefault()
        let commentObject = {
            text: commentText
        }
        dispatch(postCommentThunk(photoId, user.id, commentObject))
        dispatch(getPhotoCommentsThunk(photoId))
        dispatch(getPhotoThunk(photoId))
        setCommentText("")
    }

    useEffect(() => {
        dispatch(getPhotoThunk(photoId))
        dispatch(getUserFavoritesThunk(user.id))
        dispatch(getPhotoCommentsThunk(photoId))
        dispatch(getAllUsersThunk())
    }, [dispatch, photoId])

    return (
        <div className='entirePageDiv'>
            <div className="wholePhotoDiv">
                <div className='mainPhotoDiv'>
                    <img className='mainPhoto' src={photoObj.photo} alt='Main' />
                    <div
                        onClick={handleFavorite}
                        className='favoriteButton'>
                        Favorite Button
                    </div>
                    <div
                        onClick={handleUnfavorite}
                        className='unfavoriteButton'>
                        Unfavorite Button
                    </div>
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
                                    <img className="commentUserProfilePhoto changeCursor" src={comment.user.profile_photo} onClick={() => history.push(`/photos/${comment.user.id}/photostream`)}
                                        alt='Commenter Profile'
                                    />
                                    <div className='commentUserNameandTimeAndComment'>
                                        <div className="commentUserNameAndTime">
                                            <NavLink className="commentUserNameDiv" exact to={`/photos/${comment.user.id}/photostream`}>
                                                {comment.user.first_name} {comment.user.last_name}
                                            </NavLink>
                                            <div className="timeSinceComment" >{timeSinceCommentDate(comment.created_at)}</div>
                                        </div>
                                        <div className="commentTextDiv">{comment.text}</div>
                                    </div>
                                    {(user) && comment.user_id === user.id && (
                                        <div className="editAndDeleteButtonsWrapper">
                                            <div className="editAndDeleteButtons">
                                                <OpenModalButton
                                                    buttonImage="Delete"
                                                    modalComponent={
                                                        <DeleteCommentModal
                                                            comment_id={comment.id}
                                                            photo_id={photoId}

                                                        />
                                                    }
                                                />
                                                <OpenModalButton
                                                    buttonImage="Edit"
                                                    modalComponent={
                                                        <UpdateCommentModal
                                                            comment_id={comment.id}
                                                            comment_text={comment.text}
                                                            photo_id={photoId}
                                                        />
                                                    }
                                                />
                                            </div>
                                        </div>
                                    )}
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
                                        {commentText.length > 300 && commentText.length < 500 &&
                                            <div className="errorContainer">
                                                <div className="commentTooLongError">
                                                    Characters: {commentText.length}/500
                                                </div>

                                            </div>
                                        }
                                        {commentText.length === 500 &&
                                            <div className="errorContainer">
                                                <div className="commentTooLongError">
                                                    You have reached the maximum comment length.
                                                </div>
                                            </div>
                                        }
                                        <textarea
                                            maxlength={500}
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
        </div>
    )
}

export default PhotoPage
