import React from "react"
import { Center, Box, Text } from "@chakra-ui/react"

export default function Loading() {
  return (
    <Box
      w="100%"
      maxW="container.lg">
      <Center w="50%" h="50%">
        <Text
          fontSize="2xl"
          fontWeight="bold">
          Cargando...
        </Text>
      </Center>
    </Box>
  )
}