import React from "react"
import {
  Box,
  Center,
  Image,
  Text,
  VStack,
} from "@chakra-ui/react";

import sloth from "assets/images/sad.png";

export default function Error(props) {
  const { text } = props;

  return (
    <Center h="80vh">
      <VStack>
        <Center w="50%" h="50%">
          <Image src={sloth} w="90%" />

          {/* <a href="http://www.freepik.com"> Designed by pch.vector </a> */}
        </Center>

        <Text
          fontSize="2xl"
          fontWeight="bold">
          Algo salió mal :(
        </Text>

        <Text>
          {text}
        </Text>
      </VStack>
    </Center>
  )
}