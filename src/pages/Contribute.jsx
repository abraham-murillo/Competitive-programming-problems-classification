import React, { useState } from "react";
import {
  Box,
  FormLabel,
  FormControl,
  FormErrorMessage,
  Input,
  VStack,
  Button,
  HStack,
  Text,
  useToast,
} from "@chakra-ui/react";

import TextareaAutosize from "components/TextareaAutosize";
import { addProblem } from "api/firebase";
import { toastBoth } from "utils/toastBoth";
import { useAppContext } from "App";
import ReactTags from 'react-tag-autocomplete'
import { flattenTags, kTopicsSuggestions } from "information/topics"

export default function Contribute() {
  const { addLocalProblem } = useAppContext();

  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("Own problem");
  const [history, setHistory] = useState("");
  const [topics, setTopics] = useState([]);
  const toast = useToast();

  function isEmptyString(str) {
    return str === undefined || str.trim() === '';
  }

  function problemHasNotTopics() {
    return topics.length === 0;
  }

  async function handleSubmit(e) {
    e.preventDefault();

    if (isEmptyString(title) || isEmptyString(url) || isEmptyString(history) || problemHasNotTopics()) {
      return;
    }

    const problemData = {
      title,
      url,
      history,
      topics: flattenTags(topics),
      accepted: false,
    };

    const problemId = await addProblem(problemData);

    if (problemId !== undefined) {
      addLocalProblem({
        ...problemData,
        id: problemId,
      });
    }

    toastBoth({
      status: problemId !== undefined,
      success: "Problema agregado exitosamente (este será revisado por un moderador).",
      failure: "Hubo un error al agregar el problema, inténtelo más tarde.",
      toast,
    });
  }

  return (
    <form>
      <Box
        h="70vh">
        <VStack >
          <Text
            fontWeight='bold'
            fontSize="2xl">
            Contribuir con un problema
          </Text>
          <Text
            fontSize="m">
            ¡Muchas gracias por contribuir!, este problema formará parte de nuestro dataset pero primero tendrá que pasar por una revisión con alguno de nuestros moderadores para determinar la calidad del problema contribuido.
          </Text>

          <FormControl
            isRequired
            isInvalid={isEmptyString(title)}>
            <FormLabel fontWeight="bold" fontSize="xl">
              Título del problema
            </FormLabel>

            <Input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />

            <FormErrorMessage>
              El título no puede ser vacío.
            </FormErrorMessage>
          </FormControl>

          <FormControl
            mt={5}
            isInvalid={isEmptyString(url)}>
            <FormLabel fontWeight="bold" fontSize="xl">
              Url
            </FormLabel>

            <Input
              type={"url"}
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />

            <FormErrorMessage>
              La url no puede ser vacía, deje el default en caso de ser un problema propio.
            </FormErrorMessage>
          </FormControl>

          <FormControl
            mt={5}
            isRequired
            isInvalid={isEmptyString(history)}>
            <FormLabel fontWeight="bold" fontSize="xl">
              Historia
            </FormLabel>

            <TextareaAutosize
              minRows={5}
              value={history}
              onChange={setHistory} />

            <FormErrorMessage>
              La historia del problema no puede ser vacía.
            </FormErrorMessage>
          </FormControl>

          <FormControl
            mt={5}
            isRequired
            isInvalid={problemHasNotTopics()}>
            <FormLabel fontWeight="bold" fontSize="xl">
              Temas
            </FormLabel>

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

            <FormErrorMessage>
              El problema debe de tener al menos un tema.
            </FormErrorMessage>
          </FormControl>
        </VStack>

        <Button
          // zIndex={-1}
          colorScheme="green"
          isFullWidth
          mt={10}
          onClick={(e) => handleSubmit(e)}>
          Agregar problema
        </Button>
      </Box>
    </form >
  );
}
