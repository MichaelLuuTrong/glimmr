import { useState, useEffect } from "react"
import { postPhotoThunk } from "../../store/photo"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom";
import "./PhotoUpload.css"

function PhotoUpload() {
    const [photo, setPhoto] = useState('')
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [taken_at, setTaken_at] = useState('')

    const [submitted, setSubmitted] = useState(false)
    const [errors, setErrors] = useState({})
    const [responseErrors, setResponseErrors] = useState({})

    const sessionUser = useSelector((state) => state.session.user)

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(() => {
        const errorArray = [];
        if (!photo.length) errorArray.photo = 'Photo is required'
        if (!title.length) errorArray.title = 'Title is required'
        if (!description.length) errorArray.description = 'Description is required'
        if (!taken_at.length) errorArray.taken_at = 'Taken at date is required'

        const currentDate = new Date();
        const selectedDate = new Date(taken_at);
        if (selectedDate > currentDate) {
            errorArray.taken_at = 'Taken at date must be before the current date';
        }
        setErrors(errorArray)
    }, [photo, title, description, taken_at])

    const formSubmit = async (e) => {
        e.preventDefault();
        setSubmitted(true);
        setResponseErrors({});
        const responses = {
            photo,
            title,
            description,
            taken_at,
            created_at: new Date().toISOString()
        };

        if (!Object.values(errors).length) {
            let createdPhoto = await dispatch(postPhotoThunk(responses, sessionUser));
            if (!createdPhoto.errors) {
                history.push(`/photos/${createdPhoto.id}`);
            } else {
                setResponseErrors(createdPhoto.errors);
            }
        }
    };

    return (
        <div onSubmit={formSubmit} className='formDiv' noValidate>
            <form className='newPhotoForm'>
                <div className='topMiddleDiv'>
                    <img className='photoFormGlimmrLogo' src='https://i.imgur.com/CN01U69.png' />
                    <div className='postAPhotoText'>Post a Photo</div>
                </div>
                {submitted && (Object.values(responseErrors).length) ? <div>{Object.values(responseErrors)}</div> : null}
                <div className='photoInputDiv'>
                    {submitted ? <div className='validationError'>{errors.photo}</div> : null}
                    <input
                        className='photoField'
                        type='text'
                        name='photo'
                        placeholder='Photo'
                        value={photo}
                        onChange={(e) => setPhoto(e.target.value)}
                    />
                </div>
                <div className='titleInputDiv'>
                    {submitted ? <div className='validationError'>{errors.title}</div> : null}
                    <input
                        className='titleField'
                        type='text'
                        name='title'
                        placeholder='Title'
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                </div>
                <div className='descriptionInputDiv'>
                    {submitted ? <div className='validationError'>{errors.description}</div> : null}
                    <input
                        className='descriptionField'
                        type='text'
                        name='description'
                        placeholder='Description'
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </div>
                <div className='takenAtInputDiv'>
                    {submitted ? <div className='validationError'>{errors.taken_at}</div> : null}
                    <input
                        className='takenAtField'
                        type='date'
                        name='taken_at'
                        value={taken_at}
                        onChange={(e) => setTaken_at(e.target.value)}
                    />
                </div>
                <div className='postPhotoButtonDiv'>
                    <button className="postPhotoButton" type='submit'>Post Photo</button>
                </div>
            </form>
        </div>
    )
}

export default PhotoUpload
