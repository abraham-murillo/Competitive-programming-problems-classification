import React, { useEffect } from "react";
import "./App.css";

import { ChakraProvider, theme } from "@chakra-ui/react";
import { HashRouter, Routes, Route } from "react-router-dom";

import Navbar from "./Navbar";
import MainPage from "./MainPage";
import SearchResults from "./SearchResults";

export const AppContext = React.createContext(null);

export function useAppContext() {
  return React.useContext(AppContext);
}

export default function App() {
  return (
    <ChakraProvider theme={theme}>
      <AppContext.Provider value={{}}>
        <>
          <HashRouter>
            <Navbar />
            <Routes>
              <Route exact path="/" element={<MainPage />} />
              <Route path="/searchResults" element={<SearchResults />} />
            </Routes>
          </HashRouter>
        </>
      </AppContext.Provider>
    </ChakraProvider>
  );
}
