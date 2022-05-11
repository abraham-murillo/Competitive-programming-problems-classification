import React, { useEffect } from "react";
import "styles/App.css";

import { ChakraProvider, theme } from "@chakra-ui/react";
import { HashRouter, Routes, Route } from "react-router-dom";

import Navbar from "Navbar";
import MainPage from "MainPage";
import SearchResults from "pages/SearchResults";
import Problem from "pages/Problem";

export const AppContext = React.createContext(null);

export function useAppContext() {
  return React.useContext(AppContext);
}

export default function App() {
  return (
    <ChakraProvider theme={theme}>
      <AppContext.Provider value={{}}>
        <>
          <Navbar />

          <HashRouter>
            <Routes>
              <Route
                exact path="/"
                element={<MainPage />}
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
        </>
      </AppContext.Provider>
    </ChakraProvider>
  );
}
