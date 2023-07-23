import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, NavLink } from "react-router-dom";
import './LoginForm.css';

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/explore" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleDemoUser = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"))
    if (data) {
      setErrors(data);
    }
  }

  return (
    <>
      <div className="loginHeaderDiv">
        <div className="loginLogoAndTextDiv">
          <NavLink className='loginLogoImage' exact to="/">
            <img className='loginLogoImageImg' src="https://i.imgur.com/CN01U69.png" alt="glimmr icon" />
          </NavLink>
          <NavLink className='loginLogoLogo' exact to="/">
            <img className='loginLogoImg' src="https://i.imgur.com/b9YTbxQ.png" alt="glimmr logo" />
          </NavLink>
        </div>
        <div className="loginHeaderBackground"></div>
      </div>
      <div className="backgroundPhotoCredit">033120190455 by Henry , CC BY</div>
      <div className="backgroundDiv">

        <div className="centralFormDiv">
          <img
            className="loginGlimmrLogo"
            src="https://i.imgur.com/CN01U69.png"
            alt=""
          />
          <div className="logInText">Log in to Glimmr</div>
          <form className="loginForm" onSubmit={handleSubmit}>
            {errors.toString().includes('email') &&
              <div className="nonCenteringDiv">
                <div className="errorMessage">
                  Email is incorrect.
                </div>
              </div>
            }
            <input
              className="emailAddressField"
              type="text"
              placeholder="Email Address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            {errors.toString().includes('password') &&
              <div className="nonCenteringDiv">
                <div className="errorMessage">
                  Password is incorrect.
                </div>
              </div>
            }
            <input
              className="passwordField"
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <button className="signInSubmitButton" type="submit">Sign In</button>
            <div className='demoUserDiv'>
              <button className="demoUserButton changeCursor"
                onClick={handleDemoUser}>
                Log in as Demo User
              </button>
            </div>
          </form>
          <div className="seperatorDiv"></div>
          <div className="notAGlimmrMemberText">Not a Glimmr member?
            <NavLink exact to='/sign-up'> Sign up here.</NavLink>
          </div >
        </div >
      </div >
    </>
  );
}

export default LoginFormPage;
