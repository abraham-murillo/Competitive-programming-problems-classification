import React from "react";

import { Container, Text, Button, VStack, Box } from "@chakra-ui/react";
import { CSVLink } from "react-csv";
import { useAppContext } from "App";
import { FiDownload as Download } from "react-icons/fi";
import { CanvaSlides } from "CanvaSlides";

export default function MainPage() {
  const { problems } = useAppContext();
  const headers = [
    { label: 'Título', key: 'title' },
    { label: 'Historia', key: 'history' },
    { label: 'Categorías', key: 'topics' },
    { label: 'Url', key: 'url' },
  ];

  return (
    <Container maxW={"container.lg"} mt={2} h={"90vh"} padding={"0"}>
      <VStack
        width="100%"
        height="100%">
        <Text
          as='b'
          fontSize="2xl">
          Clasificador inteligente de problemas de programación competitiva
        </Text>

        <Text pb={5}>
          El objetivo de este sitio es proporcionar a la comunidad de programación competitiva una forma sencilla y eficiente de clasificar problemas, lo anterior con la finalidad de saber qué técnicas podrían ser necesarias de aprender o simplemente para poder clasificar los problemas que un concurso vaya a albergar y garantizar la diversidad de temas.
        </Text>

        <div
          width="100%"
          height="0%"
          overflow="hidden"
          willChange="transform"
        >
          <CanvaSlides />
        </div>

        <Box
          pos="fixed"
          right={10}
          bottom={5}>
          <CSVLink
            data={problems}
            headers={headers}
            filename={"cp-problem-classification-dataset.csv"}
            target="_blank">
            <Button
              leftIcon={<Download />}
              colorScheme='blue'>
              Descargar dataset
            </Button>
          </CSVLink>
        </Box>
      </VStack>
    </Container >
  );
}
