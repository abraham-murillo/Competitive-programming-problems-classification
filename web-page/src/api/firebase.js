import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

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
const analytics = getAnalytics(app);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

export { analytics, auth, firestore, storage }