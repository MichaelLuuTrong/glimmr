import { useState, useEffect } from "react";
import { patchPhotoThunk, getPhotoThunk, deletePhotoThunk } from "../../store/photo";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import "./PhotoEdit.css";

function PhotoEdit() {
    const { photoId } = useParams();
    const [photo, setPhoto] = useState({});
    const [title, setTitle] = useState("");
    const [user_id, setUser_id] = useState("")
    const [description, setDescription] = useState("");
    const [taken_at, setTaken_at] = useState("");
    const [submitted, setSubmitted] = useState(false);
    const [errors, setErrors] = useState({});
    const [responseErrors, setResponseErrors] = useState({});
    const sessionUser = useSelector((state) => state.session.user);
    const dispatch = useDispatch();
    const history = useHistory();
    const [confirmDelete, setConfirmDelete] = useState(false)

    useEffect(() => {
        const fetchData = async () => {
            const photoData = await dispatch(getPhotoThunk(photoId));
            if (!photoData) {
                return;
            }
            setUser_id(photoData.user_id)
            setPhoto(photoData.photo);
            setTitle(photoData.title);
            setDescription(photoData.description);
            // Check if photoData.taken_at is a valid date string
            const dateObject = new Date(photoData.taken_at);
            if (isNaN(dateObject.getTime())) {
                // Invalid date string, set taken_at to an empty string or some default value
                setTaken_at("");
            } else {
                // Valid date string, format it
                const formattedTakenAtDate = dateObject.toISOString().split('T')[0];
                setTaken_at(formattedTakenAtDate);
            }
        };
        fetchData();
    }, [dispatch, photoId]);

    useEffect(() => {
        if (!photo) return;
        const errorArray = [];
        if (!photo.length) errorArray.photo = 'Photo is required'
        if (!title.length) errorArray.title = "Title is required";
        if (!description.length) errorArray.description = "Description is required";
        if (!taken_at.length) errorArray.taken_at = "Taken at date is required";

        const currentDate = new Date();
        const selectedDate = new Date(taken_at);
        if (selectedDate > currentDate) {
            errorArray.taken_at = "Taken at date must be before the current date";
        }
        setErrors(errorArray);
    }, [photo, title, description, taken_at]);

    const formSubmit = async (e) => {
        e.preventDefault();
        setSubmitted(true);
        setResponseErrors({});
        const responses = {
            photo,
            title,
            description,
            taken_at,
            updated_at: new Date().toISOString(),
        };

        if (!Object.values(errors).length) {
            let updatedPhoto = await dispatch(
                patchPhotoThunk(responses, photoId)
            );
            console.log(updatedPhoto)
            if (!updatedPhoto.errors) {
                history.push(`/photos/${updatedPhoto.id}`);
            } else {
                setResponseErrors(updatedPhoto.errors);
            }
        }
    };

    const handleDelete = async (e) => {
        e.preventDefault();
        setConfirmDelete(true);
    };

    const handleConfirmDelete = async (e) => {
        e.preventDefault();
        let deletedPhoto = await dispatch(deletePhotoThunk(photoId));
        history.push(`/photos/${user_id}/photostream`);
    };

    return (
        <div className="formDiv">
            {sessionUser && sessionUser.id === user_id ? (
                <form onSubmit={formSubmit} className="editPhotoForm" noValidate>
                    <div className="deleteButtonContainer">
                        {!confirmDelete ? (
                            <button className="deleteButton" onClick={handleDelete}>
                                Delete Photo Permanently
                            </button>
                        ) : (
                            <button className="deleteButton confirm" onClick={handleConfirmDelete}>
                                Confirm Deletion
                            </button>
                        )}
                    </div>
                    <div className="topMiddleDiv">
                        <img
                            className="photoFormGlimmrLogo"
                            src="https://i.imgur.com/CN01U69.png"
                            alt=""
                        />
                        <div className="editPhotoText">Edit a Photo</div>
                    </div>
                    {submitted && Object.values(responseErrors).length ? (
                        <div>{Object.values(responseErrors)}</div>
                    ) : null}
                    <div className='photoInputDiv'>
                        {submitted ? <div className='validationError'>{errors.photo}</div> : null}
                        <div className="aboveFieldText">Photo</div>
                        <input
                            className='photoField'
                            type='text'
                            name='photo'
                            placeholder='Photo'
                            value={photo}
                            onChange={(e) => setPhoto(e.target.value)}
                        />
                    </div>
                    <div className="titleInputDiv">
                        {submitted ? <div className="validationError">{errors.title}</div> : null}
                        <div className="aboveFieldText">Title</div>
                        <input
                            className="titleField"
                            type="text"
                            name="title"
                            placeholder="Title"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                    </div>
                    <div className="descriptionInputDiv">
                        {submitted ? (
                            <div className="validationError">{errors.description}</div>
                        ) : null}
                        <div className="aboveFieldText">Description</div>
                        <input
                            className="descriptionField"
                            type="text"
                            name="description"
                            placeholder="Description"
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                        />
                    </div>
                    <div className="takenAtInputDiv">
                        {submitted ? <div className="validationError">{errors.taken_at}</div> : null}
                        <div className="aboveFieldText">Taken At</div>
                        <input
                            className="takenAtField"
                            type="date"
                            name="taken_at"
                            value={taken_at}
                            onChange={(e) => setTaken_at(e.target.value)}
                        />
                    </div>
                    <div className="updatePhotoButtonDiv">
                        <button className="updatePhotoButton" type="submit">
                            Update Photo
                        </button>
                    </div>
                </form>
            ) :
                <div className='badUserDiv'>Photo could not be found</div>}
        </div>
    );
}

export default PhotoEdit;
