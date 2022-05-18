import React, { useEffect, useState } from "react";
import "styles/App.css";

import { ChakraProvider, theme, Text, Container } from "@chakra-ui/react";
import { HashRouter, Routes, Route } from "react-router-dom";

import Navbar from "Navbar";
import MainPage from "MainPage";
import SearchResults from "pages/SearchResults";
import Problem from "pages/problem/Problem";
import { getAllProblems } from "api/firebase";
import AddProblem from "pages/AddProblem";
import DetectTopics from "pages/DetectTopics";

export const AppContext = React.createContext(null);

export function useAppContext() {
  return React.useContext(AppContext);
}

export default function App() {
  const [problems, setProblems] = useState([]);

  useEffect(() => {
    async function getTitles() {
      const allProblems = await getAllProblems();
      setProblems(allProblems);
    }

    getTitles();
  }, []);

  function eraseLocalProblem(problemId) {
    setProblems(problems.filter((problem) => problem.id !== problemId))
  }

  function addLocalProblem(newProblem) {
    setProblems([...problems, newProblem])
  }

  return (
    <ChakraProvider theme={theme}>
      <AppContext.Provider value={{
        problems, setProblems,
        eraseLocalProblem,
        addLocalProblem
      }}>
        <Navbar />

        <Container maxW={"container.lg"} mt={10} h={"100%"}>

          <HashRouter>
            <Routes>
              <Route
                exact path="/"
                element={<MainPage />}
              />

              <Route
                path="/createJSON"
                element={<AddProblem />}
              />

              <Route
                path="/detectTopics"
                element={<DetectTopics />}
              />

              <Route
                path="/searchResults/:queryString"
                element={<SearchResults />}
              />

              <Route
                path="/problem/:problemId"
                element={<Problem />}
              />
            </Routes>
          </HashRouter>
        </Container>

      </AppContext.Provider>
    </ChakraProvider >
  );
}
