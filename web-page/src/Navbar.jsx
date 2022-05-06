import { React, useState } from "react";
import { Link } from "react-router-dom";
import { Input, Box, Spacer, Flex, Container } from "@chakra-ui/react";

export default function Navbar() {
  const [queryString, setQueryString] = useState("");

  return (
    <Box boxShadow={"md"}>
      <Container>
        <Flex align={"center"} height={"80px"}>
          <Box w={"86px"}>{/* <Image w={"100px"} src={logo} /> */}</Box>
          <Input
            placeholder="Título del problema"
            onChange={(event) => setQueryString(event.target.value)}
          />
          <Link to={"/searchResults/" + queryString}>Buscar</Link>
          <Spacer />
        </Flex>
      </Container>
    </Box>
  );
}
