import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  Text,
  Box,
  Button,
  useToast,
  VStack,
  Container,
  HStack,
  Show,
} from "@chakra-ui/react";
import { getProblem, eraseProblem, updateProblem } from "api/firebase";
import { toastBoth } from "utils/toastBoth";
import { useAppContext } from "App";
import ReactTags from 'react-tag-autocomplete'
import isUrl from 'is-url';

import Error from "components/Error";
import Loading from "components/Loading";
import { createTags, flattenTags, kTopicsSuggestions } from "information/topics";
import { hasLoggedIn } from "context/AuthContext";

export default function ProblemPage() {
  const { problemId } = useParams();
  const { eraseLocalProblem, addLocalProblem } = useAppContext();
  const [problem, setProblem] = useState({});
  const [loading, setLoading] = useState(true);
  const [topics, setTopics] = useState([]);
  const toast = useToast();

  async function handleEraseProblem(e) {
    e.preventDefault();

    const success = await eraseProblem(problemId)

    if (success) {
      eraseLocalProblem(problemId);
    }

    toastBoth({
      status: success,
      success: 'Problema rechazado exitosamente.',
      failure: 'Hubo un error al rechazar el problema, inténtelo más tarde.',
      toast
    });
  }

  async function handleUpdateProblem(e) {
    e.preventDefault();

    const success = await updateProblem(problemId, {
      ...problem,
      topics: flattenTags(topics),
      accepted: true,
    })

    if (success) {
      eraseLocalProblem(problemId);
      addLocalProblem({
        ...problem,
        topics: flattenTags(topics),
      })
    }

    toastBoth({
      status: success,
      success: 'Problema aceptado exitosamente.',
      failure: 'Hubo un error al aceptar el problema, inténtelo más tarde.',
      toast
    });
  }

  useEffect(() => {
    async function fetchProblem() {
      const data = await getProblem(problemId);
      setProblem(data);
      if (data) {
        setTopics(createTags(data.topics));
      }
      setLoading(false);
    }

    setLoading(true);
    fetchProblem();
  }, [problemId]);

  if (loading) {
    return <Loading />
  } else {
    if (problem === undefined) {
      return <Error text="No se encontró el problema" />
    } else {
      return (
        <>
          <Box
            h="70vh"
            alignContent="left">

            {problem && (
              <VStack>
                {
                  isUrl(problem.url)
                    ?
                    <a href={problem.url}>
                      <Text
                        fontWeight='bold'
                        fontSize="2xl">
                        {problem.title}
                      </Text>
                    </a>
                    :
                    <Text
                      fontWeight='bold'
                      fontSize="2xl">
                      {problem.title}
                    </Text>
                }

                <Box
                  w="100%"
                  maxW="container.lg"
                  alignContent="left">
                  <Text as='b'>
                    Historia del problema
                  </Text>

                  <Text
                    textAlign="left">
                    {problem.history}
                  </Text>
                </Box>

                <Box
                  w="100%"
                  alignContent="left"
                  mt={10}>
                  <Text
                    as='b'
                    textAlign="left">
                    Temas asignados por el contribuidor, (asegúrese de que sean correctos o corríjalos).
                  </Text>

                  <ReactTags
                    tags={topics}
                    suggestions={kTopicsSuggestions}
                    onDelete={(i) => {
                      setTopics(topics.filter((topic, index) => index !== i));
                    }}
                    onAddition={(newTopic) => {
                      const newTopicLowerCase = newTopic.name.toLowerCase();
                      for (let topic of topics) {
                        if (topic.name === newTopicLowerCase) {
                          return;
                        }
                      }
                      setTopics([...topics, newTopic]);
                    }}
                  />
                </Box>
              </VStack>
            )}
          </Box>

          {hasLoggedIn() && (
            <HStack mt={10}>
              <Button
                colorScheme="blue"
                isFullWidth
                onClick={(e) => handleUpdateProblem(e)}>
                Aceptar problema
              </Button>

              <Button
                colorScheme="red"
                isFullWidth
                onClick={(e) => handleEraseProblem(e)}>
                Rechazar problema
              </Button>
            </HStack>
          )}
        </>
      );
    }
  }
}