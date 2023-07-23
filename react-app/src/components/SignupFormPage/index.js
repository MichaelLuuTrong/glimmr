import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, NavLink } from "react-router-dom";
import { signUp, login } from "../../store/session";
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
  // const [imageLoading, setImageLoading] = useState(false);

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

    if (last_name.length < 2) err.last_name = 'Please provide your last name.';
    if (last_name.length > 20) err.last_name = 'Please shorten your last name to 20 characters or fewer.'

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
      const responses = new FormData();
      responses.append("username", username);
      responses.append("email", email);
      responses.append("password", password);
      responses.append("first_name", first_name);
      responses.append("last_name", last_name);
      responses.append("bio", bio);
      responses.append("profile_photo", profile_photo);
      responses.append("cover_photo", cover_photo)
      // const responses = {
      //   username,
      //   email,
      //   password,
      //   first_name,
      //   last_name,
      //   bio,
      //   profile_photo,
      //   cover_photo
      // }
      // setImageLoading(true)
      await dispatch(signUp(responses));
    }
  }

  const handleDemoUser = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"))
    if (data) {
      setErrors(data);
    }
  }

  if (sessionUser) return <Redirect to="/explore" />;

  return (
    <>
      <div className="signupHeaderDiv">
        <div className="signupLogoAndTextDiv">
          <NavLink className='loginLogoImage' exact to="/">
            <img className='loginLogoImageImg' src="https://i.imgur.com/CN01U69.png" alt="glimmr icon" />
          </NavLink>
          <NavLink className='loginLogoLogo' exact to="/">
            <img className='loginLogoImg' src="https://i.imgur.com/b9YTbxQ.png" alt="glimmr logo" />
          </NavLink>
        </div>
        <div className="signupHeaderBackground"></div>
      </div>
      <div className="backgroundPhotoCredit">033120190455 by Henry , CC BY</div>
      <div className="backgroundDiv">
        <div className="mainSignUpFormDiv">
          <img
            className="signupGlimmrLogo"
            src="https://i.imgur.com/CN01U69.png"
            alt=""
          />
          <div className="signUpHeader">Sign up for Glimmr</div>
          {/* <ul>
            {errors.map((error, idx) => <li key={idx}>{error}</li>)}
          </ul> */}
          <form
            onSubmit={handleSubmit}
            encType="multipart/form-data">
            <div className="firstNameInput">
              {submitted && errors.first_name && <div className="signupError">{errors.first_name}</div>}
              <label className='signupLabel'>
                First Name
                <input
                  className='firstNameInputField'
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
              <label className='signupLabel'>
                Last Name
                <input
                  className='lastNameInputField'
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
              <label className='signupLabel'>
                Email
                <input
                  className='emailInputField'
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
              <label className='signupLabel'>
                Username
                <input
                  className='usernameInputField'
                  maxLength={30}
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </label></div>
            <div className="profilePhotoInput">
              {submitted && errors.profile_photo && <div className="signupError">{errors.profile_photo}</div>}
              <label className='signupLabel'>
                Profile Photo
                <input
                  className='profilePhotoInputField'
                  type="file"
                  accept="image/*"
                  onChange={(e) => setprofile_photo(e.target.files[0])}
                  required
                />
              </label>
            </div>
            <div className="coverPhotoInput">
              {submitted && errors.cover_photo && <div className="signupError">{errors.cover_photo}</div>}
              <label className='signupLabel'>
                Cover Photo
                <input
                  className='coverPhotoInputField'
                  type="file"
                  accept="image/*"
                  onChange={(e) => setcover_photo(e.target.files[0])}
                  required
                />
              </label>
            </div>
            <div className="bioInput">
              {submitted && errors.bio && <div className="signupError">{errors.bio}</div>}
              <label className='signupLabel'>
                Bio
                <textarea
                  className='bioInputField'
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
              <label className='signupLabel'>
                Password
                <input
                  className='passwordInputField'
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
              <label className='signupLabel'>
                Confirm Password
                <input
                  className='passwordConfirmationInputField'
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
            <button className={Object.values(errors).length ? 'signupButtonDisabled' : 'signupButtonEnabled'} type="submit">Sign Up</button>
            <div className='demoUserDiv'>
              <button className="signupDemoUserButton changeCursor"
                onClick={handleDemoUser}>
                Log in as Demo User
              </button>
            </div>
          </form>
          <div className="seperatorDiv"></div>
          <div className="notAGlimmrMemberText">Already a Glimmr member?
            <NavLink exact to='/log-in'> Log in here.</NavLink>
          </div >
        </div>
      </div>
    </>
  );
}

export default SignupFormPage;
