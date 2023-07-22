import { useParams } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { getUserThunk } from "../../store/user"
import "./About.css"



function About() {
    const dispatch = useDispatch()
    const { userId } = useParams
    const userObj = useSelector(state => state.userReducer.user)
    useEffect(() => {
        if (userId) {
            dispatch(getUserThunk(userId))
        }
    }, [dispatch, userId])

    return (
        <div className='userBioBackground'>
            <div className='userBio'>
                <div className='userBioText'>
                    {userObj.bio}
                </div>
            </div>
        </div>
    )
}

export default About
