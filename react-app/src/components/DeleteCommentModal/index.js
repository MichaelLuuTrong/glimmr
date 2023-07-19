import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal"
import { deleteCommentThunk } from "../../store/comment";
import { getPhotoCommentsThunk } from "../../store/comment";
import { useEffect } from "react";
import '/DeleteCommentModal.css'

const DeleteCommentModal = ({ comment_id, photo_id }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal()

    const deletePressed = async () => {
        await dispatch(deleteCommentThunk(comment_id))
        closeModal()
    }

    useEffect(() => {
        dispatch(getPhotoCommentsThunk(photo_id))
    }, [dispatch, photo_id])

    return (
        <div className="deleteCommentDiv">
            <div className="deleteCommentText">
                Delete Comment
            </div>
            <div className="areYouSureText">
                Are you sure you want to delete this comment?
            </div>
            <div className='optionButtons'>
                <button className='deleteOptionButton changeCursor' onClick={() => deletePressed()}>Delete</button>
                <button className='cancelOptionButton changeCursor' onClick={() => closeModal()}>Cancel</button>
            </div>
        </div>
    )
}

export default DeleteCommentModal
