import { React } from "react";
import { Link } from "@chakra-ui/react";
import {
  Button,
  ButtonGroup,
  Input,
  Box,
  Spacer,
  Flex,
  Container,
} from "@chakra-ui/react";
import { BiSearchAlt } from "react-icons/bi";

export default function Navbar() {
  return (
    <Box boxShadow={"md"}>
      <Container>
        <Flex align={"center"} height={"80px"}>
          <Box w={"86px"}>{/* <Image w={"100px"} src={logo} /> */}</Box>
          <Input placeholder="Título del problema" />
          <Link marginLeft={3} href="#/searchResults">
            Buscar
          </Link>
          <Spacer />
        </Flex>
      </Container>
    </Box>
  );
}
