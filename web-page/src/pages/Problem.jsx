import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useToast } from "@chakra-ui/react";
import { getProblem } from "api/functions";

export default function Problem() {
  const { problemId } = useParams();
  const [problem, setProblem] = useState({});

  useEffect(() => {
    async function updateProblem() {
      const data = await getProblem(problemId);
      setProblem(data);
    }

    updateProblem();
  }, [problemId]);


  const toast = useToast();

  // async function deleteProblem(e) {
  //   e.preventDefault();

  //   const success = await addProblem({
  //     title,
  //     url,
  //     history,
  //     input,
  //     output,
  //     topics
  //   })

  //   if (success) {
  //     toast({
  //       title: 'Problema creado exitosamente.',
  //       status: 'success',
  //       duration: 9000,
  //       isClosable: true,
  //     })
  //   } else {
  //     toast({
  //       title: 'Hubo un error al crear el problema, inténtelo más tarde.',
  //       status: 'error',
  //       duration: 9000,
  //       isClosable: true,
  //     })
  //   }
  // }

  return (
    <>
      <h1>{problem.title}</h1>

      <h2>{problem.history}</h2>
    </>
  )
}