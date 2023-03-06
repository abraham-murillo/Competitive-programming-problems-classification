import { addUser, getAllUsers } from "api/firebase";
import { useAppContext } from "App";
import {
  GoogleAuthProvider,
  onAuthStateChanged,
  signInWithPopup,
  signOut,
} from "firebase/auth";
import { createContext, useContext, useEffect, useState } from "react";

import { auth } from "../api/firebase";

const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const [user, setUser] = useState({});
  const [newUser, setNewUser] = useState(false);

  const googleSignIn = async () => {
    const allUsers = await getAllUsers();
    console.log(allUsers);
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider)
      .then(function (result) {
        var user = result.user;
        var isNewUser = true;

        for (const someUser of allUsers) {
          if (someUser.email == user.email) {
            console.log(someUser);
            isNewUser = false;
          }
        }

        setNewUser(isNewUser);

        if (isNewUser) {
          console.log(
            "User " + user.email + " is a new user! User not accepted yet"
          );
          const newUser = {
            email: user.email,
            accepted: false,
            pending: true,
          };
          addUser(newUser);
        }
      })
      .catch(function (error) {
        console.log(error);
      });

    if (newUser) {
      logOut();
    }

    return newUser;
  };

  const logOut = () => {
    signOut(auth);
  };

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
      console.log("User", currentUser);
    });

    return () => {
      unsubscribe();
    };
  }, []);

  return (
    <AuthContext.Provider value={{ googleSignIn, logOut, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const UserAuth = () => {
  return useContext(AuthContext);
};

export function hasLoggedIn() {
  const { user } = UserAuth();
  return user?.displayName ? true : false;
}
