import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
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
          </Route>
          <Route path="/sign-up">
            {/* Sign-Up Page */}
          </Route>
          <Route path="/log-in">
            {/* Log-In Page */}
          </Route>
          <Route path="/explore">
            {/* Explore Page */}
          </Route>
          <Route path='/photos/upload'>
            {/* Upload Photos Page */}
          </Route>
          <Route path='/photos/:photoId'>
            {/* Photo Page */}
          </Route>
          <Route path='/photos/:userId/:albumsId'>
            {/* Album Page */}
          </Route>
          <Route path='/people/:userId/'>
            {/* User - About Page */}
          </Route>
          <Route path='/photos/:userId/photostream'>
            {/* User - Photostream Page */}
          </Route>
          <Route path='/photos/:userId/albums'>
            {/* User - Albums Page */}
          </Route>
          <Route path='/photos/:userId/favorites'>
            {/* User - Favorites Page */}
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
