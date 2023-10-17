import { useSelector } from "react-redux"
import { NavLink } from 'react-router-dom'
import ProfileButton from "./ProfileButton"
import './Header.css'



function Header({ isLoaded }) {
    const sessionUser = useSelector(state => state.session.user)

    return (
        <div className='headerFull'>
            <div className='headerBackground'></div>
            <div className='headerLeftSide'>
                <NavLink className='landingLinkImage' exact to="/">
                    <img className='landingLinkImageImg' src="https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmr+resources/glimmrlogo2.png
" alt="glimmr icon" />
                </NavLink>
                <NavLink className='landingLinkLogo' exact to="/">
                    <img className='landingLinkLogoImg' src="https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmr+resources/glimmrlogowhite.png" alt="glimmr logo" />
                </NavLink>
                {sessionUser && <NavLink className='headerNavLink' exact to={`/photos/${sessionUser.id}/photostream`}>
                    <div className='headerYouDiv'>You</div>
                </NavLink>}
                <NavLink className='headerNavLink' exact to="/explore">
                    <div className='headerExploreDiv'>Explore</div>
                </NavLink>
            </div>
            <div className='headerRightSide'>
                {sessionUser && <NavLink className='uploadNavLink' exact to={`/photos/upload`}>
                    <img className='uploadIcon' src="https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmr+resources/uploadicon.png" alt="upload icon" />
                </NavLink>}
                {sessionUser && <ProfileButton />}
                {!sessionUser && <NavLink className='headerNavLink' exact to={`/log-in`}>
                    <div className='headerLoginDiv'>Log In</div>
                </NavLink>}
                {!sessionUser && <NavLink className='headerNavLink' exact to={`/sign-up`}>
                    <div className='headerSignupDiv'>Sign Up </div>
                </NavLink>}
            </div>
        </div >
    )
}

export default Header
