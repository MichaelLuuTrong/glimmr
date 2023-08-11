import { useState, useEffect } from "react";
import { patchPhotoThunk, getPhotoThunk, deletePhotoThunk } from "../../store/photo";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import "./PhotoEdit.css";

import Resizer from "react-image-file-resizer"

const resizeFile = async (file) =>
    new Promise((resolve) => {
        Resizer.imageFileResizer(
            file, //file
            9000, //maxWidth
            400, //maxHeight,
            "JPEG", //compressFormat
            100, //quality
            0, //rotation
            async (uri) => {
                const binaryData = atob(uri.split(',')[1]);
                const blob = new Blob([new Uint8Array([...binaryData].map(char => char.charCodeAt(0)))]);
                const resizedFile = new File([blob], `thumbnail_${file.name}`, {
                    type: 'image/jpeg', // Adjust the MIME type if needed
                    lastModified: file.lastModified,
                });

                resolve(resizedFile);
            },
            "base64"
        );
    });

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
    // const [imageLoading, setImageLoading] = useState(false);
    const [oldPhoto, setOldPhoto] = useState({})

    useEffect(() => {
        const fetchData = async () => {
            const photoData = await dispatch(getPhotoThunk(photoId));
            if (!photoData) {
                return;
            }
            setUser_id(photoData.user_id)
            setPhoto(photoData.photo);
            setOldPhoto(photoData.photo)
            setTitle(photoData.title);
            setDescription(photoData.description);
            // Check if photoData.taken_at is a valid date string
            const dateObject = new Date(photoData.taken_at);
            if (isNaN(dateObject.getTime())) {
                // Invalid date string, set taken_at to an empty string
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
        const errorArray = [];
        if (!title.length) errorArray.title = "Title is required";
        if (title.length > 50) errorArray.title = 'Title must be less than 50 characters'
        if (!description.length) errorArray.description = "Description is required";
        if (description.length > 2000) errorArray.description = 'Description can be a maximum of 2000 characters.'
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
        const responses = new FormData()
        if (photo) responses.append("photo", photo)
        responses.append("title", title)
        responses.append("description", description)
        responses.append("taken_at", taken_at)
        responses.append("updated_at", (new Date().toISOString()))

        try {
            const thumbnailPhoto = await resizeFile(photo)
            responses.append("thumbnail_photo", thumbnailPhoto)

            if (!Object.values(errors).length) {
                let updatedPhoto = await dispatch(
                    patchPhotoThunk(responses, photoId)
                );
                if (updatedPhoto) {
                    history.push(`/photos/${updatedPhoto.id}`);
                } else {
                    setResponseErrors("Error: there was an issue editing your photo.");
                }
            }

        } catch (error) {
            console.error("Error:", error)
        }
    };

    const handleDelete = async (e) => {
        e.preventDefault();
        setConfirmDelete(true);
    };

    const handleConfirmDelete = async (e) => {
        e.preventDefault();
        await dispatch(deletePhotoThunk(photoId));
        history.push(`/photos/${user_id}/photostream`);
    };

    return (
        <div className="formDiv">
            {sessionUser && sessionUser.id === user_id ? (
                <form
                    onSubmit={formSubmit}
                    className="editPhotoForm"
                    encType="multipart/form-data"
                >
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
                        <div className='editPhotoResponseErrors'>{Object.values(responseErrors)}</div>
                    ) : null}
                    <div className='photoInputDiv'>
                        {submitted ? <div className='validationError'>{errors.photo}</div> : null}
                        <div className="aboveFieldText">Photo</div>
                        <div className="aboveFieldText">(Leave Empty to Keep Current Photo)</div>
                        <input
                            className='photoField'
                            type='file'
                            accept="image/*"
                            name='photo'
                            onChange={(e) => setPhoto(e.target.files[0])}
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
                        <textarea
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
                        <button className="cancelUpdatePhotoButton" onClick={() => history.push(`/photos/${sessionUser.id}/photostream`)}>
                            Cancel Update
                        </button>
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
