import React, { useState } from "react";

import { Box, HStack } from "@chakra-ui/react";
import TextareaAutosize from "components/TextareaAutosize";
import TagsBox from "components/TagsBox";

export default function DetectTopics() {
  const [text, setText] = useState("");
  const [topics, setTopics] = useState([]);


  return (
    <Box>
      <HStack>
        <Box w="50%">
          <TextareaAutosize
            value={text}
            onChange={setText} />
        </Box>

        <Box w="50%">
          <TagsBox
            tags={topics}
            setTags={setTopics} />
        </Box>
      </HStack>

    </Box >
  )
}