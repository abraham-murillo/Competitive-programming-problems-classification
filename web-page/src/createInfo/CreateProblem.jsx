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
import MakeModal from "../components/MakeModal";
import TagsPool from "../components/TagsPool";


export default function CreateProblem() {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [history, setHistory] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");


  const createNewProblem = useDisclosure();

  function handleSubmit(e) {

  }

  return (
    // <MakeModal
    //   title={"Agregar problema"}
    //   isOpen={createNewProblem.isOpen}
    //   onClose={createNewProblem.onClose}
    // >
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

          <TagsPool />
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

    // </MakeModal>
  );
}