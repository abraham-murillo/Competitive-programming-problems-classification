import React, { useEffect, useState } from "react";
import { Spacer, VStack, Container, Link } from "@chakra-ui/react";
import { useParams } from "react-router-dom";
import editDistance from "utils/editDistance";
import { useAppContext } from "App";
import Error from "components/Error";

const topK = 20;

export default function SearchResults() {
  const { problems } = useAppContext();
  const { queryString } = useParams();
  const [top, setTop] = useState([]);

  useEffect(() => {
    setTop(problems
      .sort((a, b) => {
        const x = editDistance(queryString, a.title);
        const y = editDistance(queryString, b.title);
        return x > y ? 1 : x < y ? -1 : 0;
      })
      .slice(0, topK));
  }, [queryString]);

  return (
    <Container maxW={"container.lg"} mt={2} h={"90vh"} padding={"0"}>
      <VStack>
        {top.map((title) => (
          <Container maxW={"container.lg"} mt={2} h={"5vh"}>
            <Link href={`#/problem/${title.id}`}>
              {title.title}
            </Link>
          </Container>
        ))}
        <Spacer />
      </VStack >
    </Container >
  );
}
