import React, { useEffect } from "react";
import { VStack, Container } from "@chakra-ui/react";

export default function SearchResults() {
  const queryString = "palo";
  const INF = 1e9;

  const titles = [
    "cat",
    "calo",
    "dog",
    "palo",
    "perro",
    "cato",
    "gato",
    "wtf",
    "xd",
    "ca lo",
  ];

  function editDistance(a, b, i = 0, j = 0) {
    if (i == a.length) return b.length - j;

    if (j == b.length) return a.length - i;

    let mn = INF;

    // Insert character
    mn = Math.min(mn, editDistance(a, b, i, j + 1) + 1);

    // Delete character
    mn = Math.min(mn, editDistance(a, b, i + 1, j) + 1);

    // Replace character
    mn = Math.min(mn, editDistance(a, b, i + 1, j + 1) + 1);

    // Skip
    if (a[i] == b[j]) mn = Math.min(mn, editDistance(a, b, i + 1, j + 1));

    return mn;
  }

  useEffect(() => {
    // Fetch titles when database is up
    titles.forEach((element) => console.log(element));
  }, [titles]);

  titles.sort((a, b) => {
    const x = editDistance(queryString, a);
    const y = editDistance(queryString, b);
    return x > y ? 1 : x < y ? -1 : 0;
  });

  return (
    <Container maxW={"container.lg"} mt={2} h={"90vh"} padding={"0"}>
      <VStack>
        {titles.map((title) => (
          <Container>{title}</Container>
        ))}
      </VStack>
    </Container>
  );
}
