import React from "react";

import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore, setDoc } from "firebase/firestore";
import { getStorage } from "firebase/storage";
import {
  collection,
  getDocs,
  getDoc,
  addDoc,
  deleteDoc,
  updateDoc,
  doc,
  query,
  where,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: process.env.REACT_APP_apiKey,
  authDomain: process.env.REACT_APP_authDomain,
  projectId: process.env.REACT_APP_projectId,
  storageBucket: process.env.REACT_APP_storageBucket,
  messagingSenderId: process.env.REACT_APP_messagingSenderId,
  appId: process.env.REACT_APP_appId,
  measurementId: process.env.REACT_APP_measurementId,
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

// Data bases collections
const contributionProblems = collection(firestore, "contributionProblems");
const pendingUsers = collection(firestore, "pendingUsers");

export async function getAllProblems() {
  return await getDocs(contributionProblems)
    .then((response) => {
      return response.docs.map((doc) => ({
        ...doc.data(),
        id: doc.id,
      }));
    })
    .catch((error) => {
      console.log(error.message);
    });
}

export async function getProblem(id) {
  const problem = await getDoc(doc(contributionProblems, id));
  return problem.data();
}

export async function addProblem(data) {
  return await addDoc(contributionProblems, data)
    .then((response) => {
      return response.id;
    })
    .catch((error) => {
      return undefined;
    });
}

export async function addUser(data) {
  return await addDoc(pendingUsers, data)
    .then((response) => {
      return response.id;
    })
    .catch((error) => {
      return undefined;
    });
}

export async function eraseProblem(id) {
  return await deleteDoc(doc(contributionProblems, id))
    .then(() => {
      return true;
    })
    .catch((error) => {
      return false;
    });
}

export async function updateProblem(id, data) {
  const docRef = doc(contributionProblems, id);
  return await updateDoc(docRef, data)
    .then(() => {
      return true;
    })
    .catch((error) => {
      return false;
    });
}

export async function updateUser(id, data) {
  const docRef = doc(pendingUsers, id);
  return await updateDoc(docRef, data)
    .then(() => {
      return true;
    })
    .catch((error) => {
      return false;
    });
}

export async function getAllProblemsNotAccepted() {
  const queryProblemsNotAccepted = query(
    contributionProblems,
    where("accepted", "==", false)
  );

  return await getDocs(queryProblemsNotAccepted)
    .then((response) => {
      return response.docs.map((doc) => ({
        ...doc.data(),
        id: doc.id,
      }));
    })
    .catch((error) => {
      console.log(error.message);
    });
}

export async function getAllUsers() {
  const queryUsers = query(pendingUsers);

  return await getDocs(queryUsers)
    .then((response) => {
      return response.docs.map((doc) => ({
        ...doc.data(),
        id: doc.id,
      }));
    })
    .catch((error) => {
      console.log(error.message);
    });
}
