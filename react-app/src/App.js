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
          <Route exact path="/">
            {/* Landing Page */}
            {sessionUser ? <Redirect to="/explore" /> : null}
          </Route>
          <Route path="/sign-up">
            {/* Sign-Up Page */}
            <SignupFormPage />
          </Route>
          <Route path="/log-in">
            {/* Log-In Page */}
            <LoginFormPage />
          </Route>
          <Route path="/explore">
            {/* Explore Page */}
            <Header />
            <Explore />
          </Route>
          <Route path='/photos/upload'>
            {/* Upload Photos Page */}
          </Route>
          <Route exact path='/photos/:photoId'>
            <PhotoPage />
            <Header />
          </Route>
          <Route path='/photos/:userId/:albumsId'>
            {/* Album Page */}
            <Header />
          </Route>
          <Route path='/people/:userId/'>
            {/* User - About Page */}
            <Header />
          </Route>
          <Route path='/photos/:userId/photostream'>
            {/* User - Photostream Page */}
            <Header />
          </Route>
          <Route path='/photos/:userId/albums'>
            {/* User - Albums Page */}
            <Header />
          </Route>
          <Route path='/photos/:userId/favorites'>
            {/* User - Favorites Page */}
            <Header />
          </Route>
        </Switch >
      )
      }
    </>
  );
}

export default App;
