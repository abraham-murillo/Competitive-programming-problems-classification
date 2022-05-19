import { React, useState } from "react";
import {
  Text,
  Link,
  Input,
  Box,
  Spacer,
  Flex,
  Container,
  Icon,
  Tooltip,
} from "@chakra-ui/react";
import { BiHomeAlt, BiCodeCurly, BiCodeBlock } from "react-icons/bi";

export default function Navbar() {
  const [queryString, setQueryString] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    window.location.href = "/#/searchResults/" + queryString;
  }

  return (
    <Box boxShadow={"md"}>
      <Container maxW={"container.lg"}>
        <Flex align={"center"} height={"80px"}>
          <Tooltip label="Ir al menú principal">
            <Link className="homeButton" href="/">
              <Icon
                className="homeButtonIcon"
                as={BiHomeAlt}
                color="black"
                isTruncated
              />
            </Link>
          </Tooltip>

          <Tooltip label="Crear JSON">
            <Link
              ml={5}
              href="#/createJSON">
              <Icon
                className="homeButtonIcon"
                as={BiCodeCurly}
                color="black"
                isTruncated
              />
            </Link>
          </Tooltip>

          <Tooltip label="Analizar problema">
            <Link
              ml={5}
              href="#/detectTopics">
              <Icon
                className="homeButtonIcon"
                as={BiCodeBlock}
                color="black"
                isTruncated
              />
            </Link>
          </Tooltip>

          <Spacer />

          <Tooltip label="Buscar un problema">
            <form onSubmit={handleSubmit}>
              <Input
                w="30vw"
                placeholder="Título del problema"
                onChange={(event) => setQueryString(event.target.value)}
                onSubmit={handleSubmit}
              />
            </form>
          </Tooltip>
        </Flex>
      </Container>
    </Box>
  );
}