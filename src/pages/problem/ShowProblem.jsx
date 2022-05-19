import React from "react";
import { Text, Box, Button, useToast, VStack, Container, HStack } from "@chakra-ui/react";
import { useAppContext } from "App";
import { useProblemContext } from "./ProblemPage";
import { eraseProblem } from "api/firebase"
import { toastBoth } from "utils/toastBoth";
import { CustomTag } from "components/TagsBox";

export default function ShowProblem(props) {
  const { eraseLocalProblem } = useAppContext();
  const { problemId, problem, setProblem } = useProblemContext();
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

  console.log("problem", problem)

  return (
    <>
      <Box
        h="70vh"
        alignContent="left">

        {problem && (
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
                maxW="container.lg"
                alignContent="left">
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
        )}
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
    </>
  )
}