import React, { useState } from "react";

import { Button, Box, HStack, Text, VStack } from "@chakra-ui/react";
import TextareaAutosize from "components/TextareaAutosize";
import { CustomTag } from "components/TagsBox";
import axios from "axios";

const problem1 = "You are given a simple undirected graph, consisting of 𝑛 vertices and 𝑚 edges. The vertices are numbered from 1 to 𝑛. The 𝑖-th vertex has a value 𝑎𝑖 written on it. You will be removing vertices from that graph. You are allowed to remove vertex 𝑖 only if its degree is equal to 𝑎𝑖. When a vertex is removed, all edges incident to it are also removed, thus, decreasing the degree of adjacent non-removed vertices. A valid sequence of removals is a permutation 𝑝1,𝑝2,…,𝑝𝑛 (1≤𝑝𝑖≤𝑛) such that the 𝑖-th vertex to be removed is 𝑝, and every removal is allowed. A pair (𝑥,𝑦) of vertices is nice if there exist two valid sequences of removals such that 𝑥 is removed before 𝑦 in one of them and 𝑦 is removed before 𝑥 in the other one. Count the number of nice pairs (𝑥,𝑦) such that 𝑥<𝑦";

const problem2 = "Abraham fed up with seeing so too many AC's decided to make a problem difficult enough so no one is able to solve it, prove him is wrong. Given n positive integers order them as follows: If a has fewer divisors than b then a must go before b. If the numbers tie in number of divisors these should be ordered from highest to lowest.";

export default function DetectTopics() {
  const [text, setText] = useState(problem2);
  const [predictedTopics, setPredictedTopics] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    const backend = process.env.REACT_APP_BACKEND.concat('/predictedTopics');
    const local = 'http://127.0.0.1:5000/predictedTopics';
    const url = backend;

    axios.post(url, { text: text })
      .then(response => {
        if (response !== undefined && response.data.predictedTopics.length > 0) {
          setPredictedTopics(response.data.predictedTopics);
        } else {
          setPredictedTopics([]);
        }
      })
      .catch(error => console.log(error));
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
