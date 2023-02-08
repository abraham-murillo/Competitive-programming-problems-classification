import React from "react";

import { Container, Text } from "@chakra-ui/react";

export default function MainPage() {

  return (
    <Container maxW={"container.lg"} mt={2} h={"90vh"} padding={"0"}>
      <Text>
        El objetivo de este sitio es proporcionar a la comunidad de programación competitiva una forma sencilla y eficiente de clasificar problemas esto para saber qué técnicas podrían ser necesarias de aprender o simplemente para poder clasificar los problemas que un concurso vaya a albergar y garantizar la diversidad de temas.
      </Text>
    </Container>
  );
}
