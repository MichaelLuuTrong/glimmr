import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import { getAllUsersThunk } from "../../store/user"
import validator from 'validator'
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [first_name, setfirst_name] = useState("")
  const [last_name, setlast_name] = useState("")
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [bio, setBio] = useState("")
  const [profile_photo, setprofile_photo] = useState("")
  const [cover_photo, setcover_photo] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const usersObj = useSelector(state => state.userReducer.allUsers)
  const usersArray = Object.values(usersObj)
  const usernamesArray = usersArray.map((user) => user.username)
  const emailsArray = usersArray.map((user) => user.email)

  useEffect(() => {
    const err = {};
    if (username.length < 4) err.username = 'Username must be more than 4 characters in length.';
    if (username.length > 30) err.username = 'Username must be less than 30 characters in length';
    if (usernamesArray.includes(username)) err.username = 'Username is taken.'

    if (email.length < 4) err.email = 'Email must be more than 5 characters in length';
    if (email.length > 30) err.email = 'Email must be less than 30 characters in length';
    if (!validator.isEmail(email)) err.email = 'Email is invalid.';
    if (emailsArray.includes(email)) err.email = 'Email is taken.'

    if (password.length < 6) err.password = 'Password must be more than 6 characters in length.';

    if (first_name.length < 2) err.first_name = 'Please provide your first name.';
    if (first_name.length > 20) err.first_name = 'Please shorten your first name to 20 characters or fewer.'

    if (last_name.length < 2) err.first_name = 'Please provide your last name.';
    if (first_name.length > 20) err.first_name = 'Please shorten your last name to 20 characters or fewer.'

    if (bio.length < 10) err.bio = "Please provide at least 10 characters of information. Don't be shy!"
    if (bio.length < 1) err.bio = 'Please provide information you would like others to know about you.';

    if (profile_photo.length < 1) err.profile_photo = 'Please provide a profile picture.';

    if (cover_photo.length < 1) err.cover_photo = 'Please provide a cover photo.';

    if (password !== confirmPassword) err.confirmPassword = 'Your password is not the same in both fields.'
    setErrors(err)

  }, [username, email, password, first_name, last_name, bio, profile_photo, cover_photo])

  useEffect(() => {
    dispatch(getAllUsersThunk())
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true)
    if (Object.values(errors).length < 1) {
      setErrors({})
      await dispatch(signUp(
        username,
        email,
        password,
        first_name,
        last_name,
        bio,
        profile_photo,
        cover_photo));
    }
  }

  if (sessionUser) return <Redirect to="/explore" />;

  return (
    <>
      <div className="mainSignUpFormDiv">
        <div className="signUpHeader">Sign Up</div>
        {/* <ul>
            {errors.map((error, idx) => <li key={idx}>{error}</li>)}
          </ul> */}
        <form onSubmit={handleSubmit}>
          <div className="firstNameInput">
            {submitted && errors.first_name && <div className="signupError">{errors.first_name}</div>}
            <label>
              First Name
              <input
                maxLength={30}
                type="text"
                value={first_name}
                onChange={(e) => setfirst_name(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="lastNameInput">
            {submitted && errors.last_name && <div className="signupError">{errors.last_name}</div>}
            <label>
              Last Name
              <input
                maxLength={30}
                type="text"
                value={last_name}
                onChange={(e) => setlast_name(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="emailInput">
            {submitted && errors.email && <div className="signupError">{errors.email}</div>}
            <label>
              Email
              <input
                maxLength={30}
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="usernameInput">
            {submitted && errors.username && <div className="signupError">{errors.username}</div>}
            <label>
              Username
              <input
                maxLength={30}
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </label></div>
          <div className="profilePhotoInput">
            {submitted && errors.profile_photo && <div className="signupError">{errors.profile_photo}</div>}
            <label>
              Profile Photo
              <input
                type="text"
                value={profile_photo}
                onChange={(e) => setprofile_photo(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="coverPhotoInput">
            {submitted && errors.cover_photo && <div className="signupError">{errors.cover_photo}</div>}
            <label>
              Cover Photo
              <input
                type="text"
                value={cover_photo}
                onChange={(e) => setcover_photo(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="bioInput">
            {submitted && errors.bio && <div className="signupError">{errors.bio}</div>}
            <label>
              Bio
              <input
                maxLength={2000}
                type="text"
                value={bio}
                onChange={(e) => setBio(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="passwordInput">
            {submitted && errors.password && <div className="signupError">{errors.password}</div>}
            <label>
              Password
              <input
                maxLength={30}
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="confirmPasswordInput">
            {submitted && errors.confirmPassword && <div className="signupError">{errors.confirmPassword}</div>}
            <label>
              Confirm Password
              <input
                maxLength={30}
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
            </label>
          </div>
          {/* <div>{Object.values(errors)}</div> */}
          {/* <div>{Object.keys(errors)}</div> */}
          <button className={Object.values(errors).length ? 'signupButtonDisabled' : 'signupButton changeCursor'} type="submit">Sign Up</button>
        </form>
      </div>
    </>
  );
}

export default SignupFormPage;
