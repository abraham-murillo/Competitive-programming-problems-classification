import React from "react";
import { Box, Center, Image, Text, VStack } from "@chakra-ui/react";

export default function Information(props) {
  const { title, text, img } = props;

  return (
    <Center h="80vh">
      <VStack>
        <Center w="50%" h="50%">
          <Image src={img} w="90%" />

          {/* <a href="http://www.freepik.com"> Designed by pch.vector </a> */}
        </Center>

        <Text fontSize="2xl" fontWeight="bold">
          {title}
        </Text>

        <Text>{text}</Text>
      </VStack>
    </Center>
  );
}
