import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Text, Box, Button, useToast, VStack, Container, HStack, Show } from "@chakra-ui/react";
import { Tabs, TabList, Tab, TabPanels, TabPanel } from "@chakra-ui/react";

import { getProblem } from "api/firebase";

import Error from "components/Error";
import Loading from "components/Loading";
import ShowProblem from "./ShowProblem";
import Tokenizer from "./Tokenizer";
import EasyTabs from "components/EasyTabs";

import { BiBookBookmark, BiClipboard } from "react-icons/bi";

export const ProblemContext = React.createContext(null);

export function useProblemContext() {
  return React.useContext(ProblemContext);
}

export default function ProblemPage() {
  const { problemId } = useParams();
  const [problem, setProblem] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchProblem() {
      const data = await getProblem(problemId);
      console.log(data);
      setProblem(data);
      setLoading(false);
    }

    setLoading(true);
    setTimeout(() => {
      fetchProblem();
    }, 2000);
  }, [problemId]);

  if (loading) {
    return <Loading />
  } else {
    if (problem === undefined) {
      return <Error text="No se encontró el problema" />
    } else {
      return (
        <ProblemContext.Provider value={{
          problemId,
          problem, setProblem,
        }}>
          <Container maxW="container.lg">
            <EasyTabs>
              <ShowProblem
                text={"Mostrar problema"}
                icon={<BiBookBookmark />}
              />
              <Tokenizer
                text={"Tokenizador"}
                icon={<BiClipboard />}
              />
            </EasyTabs>
          </Container >
        </ProblemContext.Provider>
      )
    }
  }
}