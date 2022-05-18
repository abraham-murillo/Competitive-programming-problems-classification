import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
import {
  collection,
  getDocs, getDoc,
  addDoc, deleteDoc,
  doc,
  query, where,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "process.env.REACT_APP_apiKey",
  authDomain: "process.env.REACT_APP_authDomain",
  projectId: "process.env.REACT_APP_projectId",
  storageBucket: "process.env.REACT_APP_projectId.appspot.com",
  messagingSenderId: "process.env.REACT_APP_messagingSenderId",
  appId: "1:process.env.REACT_APP_messagingSenderId:web:839d990106c8987711a8c1",
  measurementId: "process.env.REACT_APP_measurementId"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

// Data bases collections
const rawProblems = collection(firestore, "rawProblems");

export async function getAllProblems() {
  return await getDocs(rawProblems)
    .then(response => {
      return response.docs.map((doc) => ({
        ...doc.data(),
        id: doc.id
      }));
    })
    .catch(error => {
      console.log(error.message)
    });
}

export async function getProblem(id) {
  const problem = await getDoc(doc(rawProblems, id));
  return problem.data();
}

export async function addProblem(data) {
  return await addDoc(rawProblems, data)
    .then((response) => {
      return response.id
    })
    .catch((error) => {
      return undefined;
    })
}

export async function eraseProblem(id) {
  return await deleteDoc(doc(rawProblems, id))
    .then(() => {
      return true;
    })
    .catch((error) => {
      return false;
    })
}