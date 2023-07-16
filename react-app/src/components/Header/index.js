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
                    <img className='landingLinkImageImg' src="https://i.imgur.com/CN01U69.png" alt="glimmr icon" />
                </NavLink>
                <NavLink className='landingLinkLogo' exact to="/">
                    <img className='landingLinkLogoImg' src="https://i.imgur.com/b9YTbxQ.png" alt="glimmr logo" />
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
                    <img className='uploadIcon' src="https://i.imgur.com/3Q82U5t.png" alt="upload icon" />
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
