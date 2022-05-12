import { collection, getDocs, addDoc, query, where, doc, getDoc } from "firebase/firestore";
import { firestore } from "./firebase";

const rawProblems = collection(firestore, "rawProblems");

function extractData(data) {
  return data.docs.map((doc) => ({
    ...doc.data(),
    id: doc.id
  }));
}

export async function getRawProblems() {
  return await getDocs(rawProblems).then(response => {
    return extractData(response);
  }).catch(error => {
    console.log(error.message)
  });
}

export async function getProblem(id) {
  const problem = await getDoc(doc(rawProblems, id));
  return problem.data();
}

export async function addProblem(data) {
  return addDoc(rawProblems, data)
    .then((response) => {
      // console.log(response);
      return true;
    })
    .catch((error) => {
      // console.log(error);
      return false;
    })
}