// import React, { useEffect, useState } from "react";
// import { Text, Box, Button, useToast, VStack, Container, HStack } from "@chakra-ui/react";
// import { useProblemContext } from "./ProblemPage";
// import { getTokens } from "api/flask";
// import EasyTable from "components/EasyTable";

// export default function Tokenizer(props) {
//   const { problemId, problem } = useProblemContext();
//   const [tokens, setTokens] = useState(null);

//   useEffect(() => {
//     async function fetchTokens(text) {
//       const response = await getTokens(text);
//       setTokens(response.tokens);
//       console.log(response)
//     }

//     setTimeout(() => {
//       const allText = "" + problem.history + " " + problem.input + " " + problem.output;
//       fetchTokens(allText);
//     }, 2000);
//   }, []);

//   return (
//     <Box h="70vh">
//       <Text
//         fontWeight='bold'
//         fontSize="2xl">
//         Tokenizador
//       </Text>

//       {tokens && (
//         <>
//           <Text>
//             Hay {tokens.length} tokens diferentes
//           </Text>

//           <Box mt={10}>
//             <EasyTable
//               // headers={["pos", "dep", "lemma"]}
//               values={tokens}
//             />
//           </Box>
//         </>
//       )}
//     </Box>
//   )
// }