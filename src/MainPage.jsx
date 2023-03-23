import React, { useEffect } from "react";

import { Container, Text, Button, VStack, Box } from "@chakra-ui/react";
import { CSVLink } from "react-csv";
import { useAppContext } from "App";
import { FiDownload as Download } from "react-icons/fi";
import { CanvaSlides } from "CanvaSlides";

import { codeforces } from "codeforces"

export default function MainPage() {
  const { problems } = useAppContext();
  const headers = [
    { label: 'title', key: 'title' },
    { label: 'history', key: 'history' },
    { label: 'topics', key: 'topics' },
    { label: 'url', key: 'url' },
  ];

  // const miniCodeforces = codeforces.slice(0, 200);
  // console.log(miniCodeforces)

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
            data={[...codeforces, ...problems]}
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
