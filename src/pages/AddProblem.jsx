import React, { useState } from "react";
import {
  Box,
  FormLabel,
  FormControl,
  Input,
  VStack,
  Button,
  HStack,
  useDisclosure,
  Text,
  useToast,
} from "@chakra-ui/react";

import TextareaAutosize from "components/TextareaAutosize";
import { CustomTag } from "components/TagsBox";
import { codeforces } from "information/topics";
import { addProblem } from "api/firebase";
import { toastBoth } from "utils/toastBoth";
import { useAppContext } from "App";

export default function AddProblem() {
  const { addLocalProblem } = useAppContext();
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [history, setHistory] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [topics, setTopics] = useState(["set", "tree"]);
  const [suggestions, setSuggestions] = useState(codeforces);
  const toast = useToast();

  async function handleSubmit(e) {
    e.preventDefault();

    const problemData = {
      title,
      url,
      history,
      input,
      output,
      topics,
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
      success: "Problema creado exitosamente.",
      failure: "Hubo un error al crear el problema, inténtelo más tarde.",
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
            Agregar problema
          </Text>

          <FormControl isRequired>
            <FormLabel>Título del problema</FormLabel>

            <Input value={title} onChange={(e) => setTitle(e.target.value)} />
          </FormControl>

          <FormControl mt={5} isRequired>
            <FormLabel>Url</FormLabel>

            <Input
              type={"url"}
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </FormControl>

          <FormControl mt={5} isRequired>
            <FormLabel>Historia</FormLabel>

            <TextareaAutosize value={history} onChange={setHistory} />
          </FormControl>

          <FormControl mt={5} isRequired>
            <FormLabel>Entrada</FormLabel>

            <TextareaAutosize value={input} onChange={setInput} />
          </FormControl>

          <FormControl mt={5} isRequired>
            <FormLabel>Salida</FormLabel>

            <TextareaAutosize value={output} onChange={setOutput} />
          </FormControl>

          <FormControl mt={5} isRequired>
            <FormLabel>Temas</FormLabel>

            {topics.length > 0 && (
              <HStack>
                {topics.map((topic) => <CustomTag tag={topic} />)}
              </HStack>
            )}
          </FormControl>
        </VStack>

        <Button
          // zIndex={-1}
          colorScheme="green"
          isFullWidth
          mt={10}
          onClick={(e) => handleSubmit(e)}>
          Crear problema
        </Button>
      </Box>
    </form >
  );
}
