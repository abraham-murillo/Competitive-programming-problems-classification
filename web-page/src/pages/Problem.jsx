import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Spacer, VStack, Container, Link } from "@chakra-ui/react";
import { getProblem } from "api/functions";

export default function Problem() {
  const { problemId } = useParams();
  const [data, setData] = useState({});

  // useEffect(async () => {
  //   const rawData = await getProblem(problemId);

  //   console.log(rawData);
  //   setData(rawData);
  // }, []);

  return (
    <>
      <h1> {problemId} </h1>

      {data.name && (
        <h2>{data.name}</h2>
      )}
    </>
  )
}