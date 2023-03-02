import React, { useState } from "react";

import { Button, Box, HStack, Text, VStack } from "@chakra-ui/react";
import TextareaAutosize from "components/TextareaAutosize";
import { CustomTag } from "components/TagsBox";
import axios from "axios";
import { kProblems } from "information/problems"

export default function DetectTopics() {
  const [text, setText] = useState(kProblems[0].history);
  const [predictedTopics, setPredictedTopics] = useState([]);

  function getHeuristicWordCount(str) {
    return str.trim().split(/\s+/).length;
  }

  const NOT_ENOUGH_CONTEXT = {
    topic: "Not enough context",
    probability: "",
  };

  async function handleSubmit(e) {
    e.preventDefault();

    const backend = process.env.REACT_APP_BACKEND.concat('/predictedTopics');
    const local = 'http://127.0.0.1:5000/predictedTopics';
    const url = backend;

    if (getHeuristicWordCount(text) <= 20) {
      setPredictedTopics([NOT_ENOUGH_CONTEXT]);
    } else {
      axios.post(url, {
        text: text
      }).then(response => {
        if (response !== undefined && response.data.predictedTopics.length > 0) {
          setPredictedTopics(response.data.predictedTopics);
        } else {
          setPredictedTopics([NOT_ENOUGH_CONTEXT]);
        }
      })
        .catch(error => console.log(error));
    }
  }

  return (
    <Box>
      <VStack w="100%">
        <Text fontWeight="bold" fontSize="2xl">
          Analizar problema
        </Text>

        <HStack w="100%">
          <Box w="100%">
            <Text fontWeight="bold" fontSize="xl">
              Problema
            </Text>

            <TextareaAutosize
              minRows={8}
              value={text}
              onChange={setText} />

            <Text fontWeight="bold" fontSize="xl">
              Temas predecidos
            </Text>

            <HStack mb={15}>
              {predictedTopics.length === 0 ?
                <Box p='4' />
                :
                predictedTopics.map((element) =>
                  <CustomTag
                    key={element.topic}
                    tag={element.topic + " " + (element.probability ? element.probability + "%" : "")}
                  />
                )
              }
            </HStack>
          </Box>

          <Box w="100%" hidden={true}>
            <Text fontWeight="bold" fontSize="xl">
              Temas
            </Text>
          </Box>
        </HStack>

        <Button
          // zIndex={-1}
          colorScheme="green"
          isFullWidth
          mt={10}
          type="submit | button"
          onClick={(e) => handleSubmit(e)}
        >
          Analizar problema
        </Button>
      </VStack>
    </Box>
  );
}
