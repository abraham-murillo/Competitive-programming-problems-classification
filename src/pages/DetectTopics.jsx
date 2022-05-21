import React, { useState } from "react";

import { Button, Box, HStack, Text, VStack } from "@chakra-ui/react";
import { getFilteredText } from "api/flask";
import TextareaAutosize from "components/TextareaAutosize";
import TagsBox from "components/TagsBox";

export default function DetectTopics() {
  const [text, setText] = useState("");
  const [topics, setTopics] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();
    console.log(text);
    const response = await getFilteredText(text);
    console.log(response.fileteredText);
  }

  return (
    <Box>
      <VStack w="100%">
        <Text fontWeight="bold" fontSize="2xl">
          Analizar problema
        </Text>

        <HStack w="100%">
          <Box w="50%">
            <Text fontWeight="bold" fontSize="xl">
              Problema
            </Text>

            <TextareaAutosize minRows={20} value={text} onChange={setText} />
          </Box>

          <Box w="50%">
            <Text fontWeight="bold" fontSize="xl">
              Temas
            </Text>

            <TagsBox tags={topics} setTags={setTopics} />
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
