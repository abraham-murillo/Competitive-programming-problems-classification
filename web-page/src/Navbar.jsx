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

  function handleSubmit(e) {
    e.preventDefault();
    window.location.href = "/#/searchResults/" + queryString;
  }

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

          <form onSubmit={handleSubmit}>
            <Input
              w="30vw"
              placeholder="Título del problema"
              onChange={(event) => setQueryString(event.target.value)}
              onSubmit={handleSubmit}
            />
          </form>
        </Flex>
      </Container>
    </Box>
  );
}
