import React, { useState } from "react";
import {
  FormLabel,
  FormControl,
  Input,
  VStack,
  Button,
  useDisclosure,
  useToast
} from "@chakra-ui/react";

import TextareaAutosize from "components/TextareaAutosize";
import TagsBox from "components/TagsBox";
import topics from "information/omegaupTopics.json";
import { addProblem } from "api/functions";

export default function AddProblem() {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [history, setHistory] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [topics, setTopics] = useState([]);

  const [suggestions, setSuggestions] = useState(topics.data);
  const toast = useToast();

  async function handleSubmit(e) {
    e.preventDefault();

    const success = await addProblem({
      title,
      url,
      history,
      input,
      output,
      topics
    })

    if (success) {
      toast({
        title: 'Problema creado exitosamente.',
        status: 'success',
        duration: 9000,
        isClosable: true,
      })
    } else {
      toast({
        title: 'Hubo un error al crear el problema, inténtelo más tarde.',
        status: 'error',
        duration: 9000,
        isClosable: true,
      })
    }
  }

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <VStack >
        <FormControl isRequired >
          <FormLabel>
            Título del problema
          </FormLabel>

          <Input
            value={title}
            onChange={(e) => setTitle(e.target.value)} />
        </FormControl>

        <FormControl mt={5}>
          <FormLabel>
            Url
          </FormLabel>

          <Input
            type={"url"}
            value={url}
            onChange={(e) => setUrl(e.target.value)} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Historia
          </FormLabel>

          <TextareaAutosize
            value={history}
            onChange={setHistory} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Entrada
          </FormLabel>

          <TextareaAutosize
            value={input}
            onChange={setInput} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Salida
          </FormLabel>

          <TextareaAutosize
            value={output}
            onChange={setOutput} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Tags
          </FormLabel>

          <TagsBox
            tags={topics}
            setTags={setTopics}
            suggestions={suggestions}
            placeholderText={"Ingresa los temas a los que corresponde el problema"}
            noSuggestionsText={"No hay temas parecidos al tuyo :("}
          />
        </FormControl>

      </VStack>

      <Button
        colorScheme="green"
        isFullWidth
        mt={10}
        type="submit">
        Crear problema
      </Button>
    </form >
  );
}