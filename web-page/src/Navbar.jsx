import React from "react";
import { Box, Spacer, Flex, Image, Text, Container } from "@chakra-ui/react";

export default function Navbar() {
  return (
    <Box boxShadow={"md"}>
      <Container>
        <Flex align={"center"} height={"38px"}>
          <Box w={"86px"}>
            {/* <Image w={"100px"} src={logo} /> */}
          </Box>

          <Text> Competitive programming problem clasificator </Text>
          <Spacer />

        </Flex>
      </Container>
    </Box>
  );
};

