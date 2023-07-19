import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal"
import { deleteCommentThunk } from "../../store/comment";
import './DeleteCommentModal.css'
import { getPhotoThunk } from "../../store/photo";

const DeleteCommentModal = ({ comment_id, photo_id }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDeleteComment = async (e) => {
        e.preventDefault()
        await dispatch(deleteCommentThunk(comment_id))
        await dispatch(getPhotoThunk(photo_id))
        closeModal()
    }

    return (
        <div className="deleteCommentDiv">
            <div className="deleteCommentText">Delete Comment</div>
            <div className="areYouSureText">Are you sure you want to delete this comment?</div>
            <form onSubmit={handleDeleteComment}>
                <div className="bothButtonsDiv">
                    <div className="cancelDeleteButton">
                        <button onClick={closeModal}>
                            Cancel
                        </button>
                    </div>
                    <div className="confirmDeleteButton">
                        <button type='submit'>
                            Delete
                        </button>
                    </div>
                </div>
            </form>
        </div>
    )
}

export default DeleteCommentModal
