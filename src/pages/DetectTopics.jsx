import React, { useState } from "react";

import { Button, Box, HStack, Text, VStack } from "@chakra-ui/react";
import { getPredictedTopics } from "api/flask";
import TextareaAutosize from "components/TextareaAutosize";
import { CustomTag } from "components/TagsBox";

export default function DetectTopics() {
  const [text, setText] = useState("");
  const [predictedTopics, setPredictedTopics] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    // console.log(text)
    const response = await getPredictedTopics(text);
    console.log(response)

    if (response && response.predictedTopics.length > 0) {
      setPredictedTopics(response.predictedTopics);
    } else {
      setPredictedTopics(["No c :,("]);
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

            <TextareaAutosize minRows={5} value={text} onChange={setText} />

            <Text fontWeight="bold" fontSize="xl">
              Temas predecidos
            </Text>

            <HStack mb={15}>
              {predictedTopics.length > 0 &&
                predictedTopics.map((element) =>
                  <CustomTag
                    tag={element.topic + " " + element.probability + "%"}
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
