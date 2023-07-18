import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch, Redirect } from "react-router-dom";
import { authenticate } from "./store/session";
import LoginFormPage from "./components/LoginFormPage"
import SignupFormPage from "./components/SignupFormPage";
import Header from "./components/Header"
import Explore from "./components/Explore"
import { useSelector } from "react-redux";
import PhotoPage from "./components/PhotoPage";
import PhotoUpload from "./components/PhotoUpload";
import UserPageTop from "./components/UserPageTop";
import Photostream from "./components/Photostream";
import About from "./components/About"

function App() {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user)
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {isLoaded && (
        <Switch>
          <Route exact path='/photos/:userId/photostream'>
            {/* User - Photostream Page */}
            <Header />
            <UserPageTop />
            <Photostream />
          </Route>

          <Route exact path='/photos/:userId/albums'>
            {/* User - Albums Page */}
            <Header />
            <UserPageTop />
          </Route>

          <Route exact path='/photos/:userId/favorites'>
            {/* User - Favorites Page */}
            <Header />
            <UserPageTop />
          </Route>

          <Route exact path='/people/:userId/'>
            {/* User - About Page */}
            <Header />
            <UserPageTop />
            <About />
          </Route>

          <Route exact path='/photos/upload'>
            {/* Upload Photos Page - COMPLETED*/}
            <Header />
            <PhotoUpload />
          </Route>

          <Route exact path='/photos/:photoId'>
            <PhotoPage />
            <Header />
          </Route>

          <Route exact path="/sign-up">
            {/* Sign-Up Page */}
            <SignupFormPage />
          </Route>

          <Route exact path="/log-in">
            {/* Log-In Page */}
            <LoginFormPage />
          </Route>

          <Route exact path="/explore">
            {/* Explore Page - COMPLETED*/}
            <Header />
            <Explore />
          </Route>

          <Route exact path="/">
            {/* Landing Page */}
            {sessionUser ? <Redirect to="/explore" /> : null}
          </Route>

          <Route exact path='/photos/:userId/:albumsId'>
            {/* Album Page */}
            <Header />
          </Route>

        </Switch >
      )}
    </>
  );
}

export default App;
