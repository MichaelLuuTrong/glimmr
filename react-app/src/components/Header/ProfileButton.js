import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from 'react-redux';
import * as sessionActions from '../../store/session';
import { useHistory } from 'react-router-dom'
import "./Header.css"

function ProfileButton() {
    const dispatch = useDispatch();
    const [showMenu, setShowMenu] = useState(false);
    const history = useHistory()
    const ulRef = useRef();
    const sessionUser = useSelector(state => state.session.user)

    const openMenu = () => {
        if (showMenu) return;
        setShowMenu(true)
    };

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = (e) => {
            // Check if ulRef.current exists before accessing the 'contains' method
            if (ulRef.current && !ulRef.current.contains(e.target)) {
                setShowMenu(false);
            }
        };

        document.addEventListener("click", closeMenu);

        return () => document.removeEventListener("click", closeMenu)
    }, [showMenu]);

    const closeMenu = () => setShowMenu(false);

    const logout = (e) => {
        e.preventDefault();
        dispatch(sessionActions.logout());
        closeMenu();
        history.push("/");
    };

    const yourPhotos = (e) => {
        e.preventDefault();
        closeMenu();
        history.push(`/photos/${sessionUser.id}/photostream`)
    }

    const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

    return (
        <>
            <img src={sessionUser.profile_photo} onClick={openMenu} className="headerProfilePicture changeCursor" alt="profile" />
            <div className={ulClassName} ref={ulRef}>
                <div className="profileMenu">
                    <div className="hiUser">Hi, {sessionUser.first_name} {sessionUser.last_name}!</div>
                    <div className='headerDividerDiv'></div>
                    <div className="logOut changeCursor" onClick={logout}>Log Out</div>
                    <div className="yourPhotos changeCursor" onClick={yourPhotos}>Your Photos</div>
                </div>
            </div>
        </>
    )


}

export default ProfileButton
