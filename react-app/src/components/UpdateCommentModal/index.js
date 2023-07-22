import { useDispatch } from "react-redux"
import { useModal } from "../../context/Modal"
import { patchCommentThunk, getCommentThunk, getPhotoCommentsThunk } from "../../store/comment"
import { useState, useEffect } from "react"
import "./UpdateCommentModal.css"

const UpdateCommentModal = ({ comment_id, comment_text, photo_id }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const [comment, setComment] = useState(comment_text)

    const handleUpdateComment = async (e) => {
        e.preventDefault()
        await dispatch(patchCommentThunk(comment, comment_id,))
        await dispatch(getPhotoCommentsThunk(photo_id))
        closeModal()
    }

    useEffect(() => {
        dispatch(getCommentThunk(comment_id));
    }, [dispatch, comment_id]);

    return (
        <div className="updateCommentDiv">
            <div className="updateCommentText">Update Comment
            </div>
            {comment.length === 500 &&
                <div className="errorContainer">
                    <div className="commentTooLongError">
                        You have reached the maximum comment length.
                    </div>
                </div>
            }
            <form onSubmit={handleUpdateComment}>
                <textarea
                    className="updateCommentTextInput"
                    type="text"
                    placeholder="Edit your comment"
                    value={comment}
                    maxLength={500}
                    onChange={(e) => setComment(e.target.value)}
                    required
                >
                </textarea>
                <div className="bothButtonsDiv">
                    <div className="cancelUpdateButton">
                        <button onClick={closeModal}>
                            Cancel
                        </button>
                    </div>
                    <div className="confirmUpdateButton">
                        <button type='submit'>
                            Submit
                        </button>
                    </div>
                </div>
            </form>
        </div>
    )
}

export default UpdateCommentModal
