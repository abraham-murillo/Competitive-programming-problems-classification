import React, { useEffect, useState } from "react";
import { Spacer, VStack, Container, Link } from "@chakra-ui/react";
import { useParams } from "react-router-dom";
import { getProblemTitles } from "api/functions";
import editDistance from "tools/editDistance";

export default function SearchResults() {
  const { queryString } = useParams();
  const [titles, setTitles] = useState([]);

  useEffect(() => {
    getProblemTitles().then(titles => {
      titles.sort((a, b) => {
        const x = editDistance(queryString, a.name);
        const y = editDistance(queryString, b.name);
        return x > y ? 1 : x < y ? -1 : 0;
      });

      return titles;
    }).then(sortedTitles => {
      return sortedTitles.slice(0, 20);
    }).then(top20 => {
      setTitles(top20);
    });
  }, [queryString]);

  return (
    <Container maxW={"container.lg"} mt={2} h={"90vh"} padding={"0"}>
      <VStack>
        {titles.map((title) => (
          <Container maxW={"container.lg"} mt={2} h={"5vh"}>
            <Link href={`#/problem/${title.id}`}>
              {title.name}
            </Link>
          </Container>
        ))
        }
        <Spacer />
      </VStack >
    </Container >
  );
}
