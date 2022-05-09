import React, { useEffect, useState } from "react";
import {
  Box,
  HStack,
  EditableInput,
  Editable,
  EditablePreview,
  EditableTextarea,
  FormLabel,
  Flex,
  FormControl,
  Input,
  FormHelperText,
  VStack,
  Button,
  Textarea,
  useDisclosure
} from "@chakra-ui/react";

import TextareaAutosize from "../components/TextareaAutosize";
import { v4 as uuid } from "uuid";
import TagsBox from "../components/TagsBox";
import allTopics from "../information/allTopics.json";

export default function CreateProblem() {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [history, setHistory] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [tags, setTags] = useState([]);
  const [suggestions, setSuggestions] = useState(allTopics.data);

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
            text={history}
            setText={setHistory} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Entrada
          </FormLabel>

          <TextareaAutosize
            text={input}
            setText={setInput} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Salida
          </FormLabel>

          <TextareaAutosize
            text={output}
            setText={setOutput} />
        </FormControl>

        <FormControl mt={5} isRequired>
          <FormLabel>
            Tags
          </FormLabel>

          <TagsBox
            tags={tags}
            setTags={setTags}
            suggestions={suggestions}
            placeholderText="Ingresa los temas a los que corresponde el problema"
            noSuggestionsText="No hay temas parecidos al tuyo :("
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