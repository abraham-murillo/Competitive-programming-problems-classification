import React from "react";
import {
  Button,
  ButtonGroup,
  Input,
  Box,
  Spacer,
  Flex,
  Container,
} from "@chakra-ui/react";
import { BiCodeCurly, BiCodeBlock } from "react-icons/bi";

export default function Navbar() {
  return (
    <Box boxShadow={"md"}>
      <Container>
        <Flex align={"center"} height={"80px"}>
          <Box w={"86px"}>{/* <Image w={"100px"} src={logo} /> */}</Box>
          <Input placeholder="Título del problema" />
          <Button marginLeft={3} colorScheme="teal" size="md">
            Buscar
          </Button>
          <Spacer />
        </Flex>
      </Container>
    </Box>
  );
}
