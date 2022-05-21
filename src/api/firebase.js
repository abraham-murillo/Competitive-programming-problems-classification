import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
import {
  collection,
  getDocs,
  getDoc,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyB6pU_T59b_Bd0E-PXF13y5Nauh5Hsz4DA",
  authDomain: "nlp-problems-classification.firebaseapp.com",
  projectId: "nlp-problems-classification",
  storageBucket: "nlp-problems-classification.appspot.com",
  messagingSenderId: "831064056148",
  appId: "1:831064056148:web:839d990106c8987711a8c1",
  measurementId: "G-6QGW6R4Y4Q",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

// Data bases collections
const rawProblems = collection(firestore, "rawProblems");

export async function getAllProblems() {
  return await getDocs(rawProblems)
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
  const problem = await getDoc(doc(rawProblems, id));
  return problem.data();
}

export async function addProblem(data) {
  return await addDoc(rawProblems, data)
    .then((response) => {
      return response.id;
    })
    .catch((error) => {
      return undefined;
    });
}

export async function eraseProblem(id) {
  return await deleteDoc(doc(rawProblems, id))
    .then(() => {
      return true;
    })
    .catch((error) => {
      return false;
    });
}
