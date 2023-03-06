import React, { useEffect, useState } from "react";
import "styles/App.css";

import { ChakraProvider, theme, Container } from "@chakra-ui/react";
import { HashRouter, Routes, Route } from "react-router-dom";
import { AuthContextProvider } from "context/AuthContext";

import Navbar from "Navbar";
import MainPage from "MainPage";
import SearchResults from "pages/SearchResults";
import ProblemPage from "pages/problem/ProblemPage";
import Contribute from "pages/Contribute";
import DetectTopics from "pages/DetectTopics";
import AcceptContributions from "pages/AcceptContributions";
import AcceptUsers from "pages/AcceptUsers";
import Login from "pages/Login";
import { kTopics } from "information/topics";

import { getAllProblems } from "api/firebase";

export const AppContext = React.createContext(null);

export function useAppContext() {
  return React.useContext(AppContext);
}

export default function App() {
  const [problems, setProblems] = useState([]);

  useEffect(() => {
    async function getTitles() {
      const allProblems = await getAllProblems();
      console.log(allProblems);
      setProblems(allProblems);
    }

    getTitles();
  }, []);

  function eraseLocalProblem(problemId) {
    setProblems(problems.filter((problem) => problem.id !== problemId));
  }

  function addLocalProblem(newProblem) {
    setProblems([...problems, newProblem]);
  }

  return (
    <ChakraProvider theme={theme}>
      <AuthContextProvider>
        <AppContext.Provider
          value={{
            kTopics,
            problems,
            setProblems,
            eraseLocalProblem,
            addLocalProblem,
          }}
        >
          <Navbar />

          <Container maxW={"container.lg"} mt={10} h={"100%"}>
            <HashRouter>
              <Routes>
                <Route exact path="/" element={<MainPage />} />

                <Route path="/contribute" element={<Contribute />} />

                <Route path="/detectTopics" element={<DetectTopics />} />

                <Route path="/login" element={<Login />} />

                <Route
                  path="/acceptContributions"
                  element={<AcceptContributions />}
                />

                <Route path="/acceptUsers" element={<AcceptUsers />} />

                <Route
                  path="/searchResults/:queryString"
                  element={<SearchResults />}
                />

                <Route path="/problem/:problemId" element={<ProblemPage />} />
              </Routes>
            </HashRouter>
          </Container>
        </AppContext.Provider>
      </AuthContextProvider>
    </ChakraProvider>
  );
}
