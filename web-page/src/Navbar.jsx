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
} from "@chakra-ui/react";
import { BiHomeAlt } from "react-icons/bi";

export default function Navbar() {
  const [queryString, setQueryString] = useState("");

  return (
    <Box boxShadow={"md"}>
      <Container maxW={"container.lg"}>
        <Flex align={"center"} height={"80px"}>
          <Link className="homeButton" href="/">
            <Icon
              className="homeButtonIcon"
              as={BiHomeAlt}
              color="black"
              isTruncated
            />
          </Link>

          <Spacer />

          <Input
            maxW={"md"}
            placeholder="Título del problema"
            onChange={(event) => setQueryString(event.target.value)}
          />

          <Spacer />

          <Link
            className="searchButton"
            href={"#/searchResults/" + queryString}
          >
            <Text color="white" isTruncated>
              Buscar
            </Text>
          </Link>

        </Flex>
      </Container>
    </Box>
  );
}
