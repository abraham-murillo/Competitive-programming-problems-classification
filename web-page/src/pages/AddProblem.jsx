import React, { useState } from "react";
import {
  FormLabel,
  FormControl,
  Input,
  VStack,
  Button,
  useDisclosure
} from "@chakra-ui/react";

import TextareaAutosize from "components/TextareaAutosize";
import TagsBox from "components/TagsBox";
import topics from "information/omegaupTopics.json";

export default function AddProblem() {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [history, setHistory] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [topics, setTopics] = useState([]);
  const [suggestions, setSuggestions] = useState(topics.data);

  const createNewProblem = useDisclosure();

  function handleSubmit(e) {
    // Subir el json a un firebase
  }

  return (
    <form>
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
        onClick={(e) => handleSubmit(e)}>
        Crear problema
      </Button>
    </form >
  );
}