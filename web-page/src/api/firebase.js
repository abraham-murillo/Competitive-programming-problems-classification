import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyB6pU_T59b_Bd0E-PXF13y5Nauh5Hsz4DA",
  authDomain: "nlp-problems-classification.firebaseapp.com",
  projectId: "nlp-problems-classification",
  storageBucket: "nlp-problems-classification.appspot.com",
  messagingSenderId: "831064056148",
  appId: "1:831064056148:web:839d990106c8987711a8c1",
  measurementId: "G-6QGW6R4Y4Q"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

export { analytics, auth, firestore, storage }