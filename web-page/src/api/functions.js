import { collection, getDocs } from "firebase/firestore";
import { firestore } from "./firebase";

const rawProblems = collection(firestore, "rawProblems");

export async function getRawProblems() {
  return await getDocs(rawProblems).then(response => {
    return response.docs.map(problem => ({
      ...problem.data(),
      id: problem.id
    }));
  }).catch(error => {
    console.log(error.message)
  });
}

export async function getProblemTitles() {
  const problemsData = await getRawProblems();

  return problemsData.map(problem => ({
    name: problem.name.toLowerCase(),
    id: problem.id
  }));
}

// export async function getProblem(id) {


// }
