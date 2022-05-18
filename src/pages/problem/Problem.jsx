import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Text, Box, Button, useToast, VStack, Container, HStack } from "@chakra-ui/react";
import { getProblem, eraseProblem } from "api/firebase";
import Loading from "components/Loading";
import Error from "components/Error";
import { toastBoth } from "utils/toastBoth";
import { useAppContext } from "App";
import { CustomTag } from "components/TagsBox";

import Navbar from "../problem/Navbar";

export default function Problem() {
  const { eraseLocalProblem } = useAppContext();
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
    }, 500);
  }, [problemId]);

  const toast = useToast();

  async function handleEraseProblem(e) {
    e.preventDefault();

    const success = await eraseProblem(problemId)

    if (success) {
      eraseLocalProblem(problemId);
    }

    toastBoth({
      status: success,
      success: 'Problema eliminado exitosamente.',
      failure: 'Hubo un error al eliminar el problema, inténtelo más tarde.',
      toast
    });
  }

  if (loading) {
    return <Loading />
  } else {
    if (problem === undefined) {
      return <Error text="No se encontró el problema" />
    } else {
      return (
        <Container
          maxW="container.lg">
          <Box h="70vh">
            <VStack>
              <a href={problem.url}>
                <Text
                  fontWeight='bold'
                  fontSize="2xl">
                  {problem.title}
                </Text>
              </a>

              <Box
                w="100%"
                maxW="container.lg"
                alignContent="left">
                <Text
                  textAlign="left">
                  {problem.history}
                </Text>
              </Box>

              {problem.input && (
                <Box
                  w="100%"
                  maxW="container.lg"
                  alignContent="left">
                  <Text
                    fontWeight='bold'
                    fontSize="xl">
                    Input
                  </Text>

                  <Text
                    textAlign="left">
                    {problem.input}
                  </Text>
                </Box>
              )}

              {problem.output && (
                <Box
                  w="100%"
                  maxW="container.lg">
                  <Text
                    fontWeight='bold'
                    fontSize="xl">
                    Output
                  </Text>

                  <Text
                    textAlign="left">
                    {problem.output}
                  </Text>
                </Box>
              )}

              {problem.topics.length > 0 && (
                <HStack>
                  {problem.topics.map((topic) => <CustomTag tag={topic} />)}
                </HStack>
              )}

            </VStack>
          </Box>

          <HStack mt={10}>
            <Button
              colorScheme="blue"
              isFullWidth >
              Actualizar problema
            </Button>

            <Button
              colorScheme="red"
              isFullWidth
              onClick={(e) => handleEraseProblem(e)}>
              Eliminar problema
            </Button>
          </HStack>
        </Container >
      )
    }
  }
}