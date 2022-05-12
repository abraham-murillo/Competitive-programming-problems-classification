import React, { useEffect, useState } from "react";
import { Spacer, VStack, Container, Link } from "@chakra-ui/react";
import { useParams } from "react-router-dom";
import editDistance from "utils/editDistance";
import { useAppContext } from "App";

const topK = 20;

export default function SearchResults() {
  const { titles } = useAppContext();
  const { queryString } = useParams();
  const [top, setTop] = useState(titles.slice(0, topK));

  useEffect(() => {
    let newTop = titles;

    newTop
      .sort((a, b) => {
        const x = editDistance(queryString, a.title);
        const y = editDistance(queryString, b.title);
        return x > y ? 1 : x < y ? -1 : 0;
      })
      .slice(0, topK);

    setTop(newTop);
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
