import React, { useEffect, useState } from "react";
import { UserAuth } from "context/AuthContext";
import waiting from "assets/images/sad.png";
import Information from "components/Information";

import {
  Box,
  FormLabel,
  FormControl,
  FormErrorMessage,
  Input,
  VStack,
  Button,
  HStack,
  Text,
  useToast,
  TableContainer,
  Table,
  TableCaption,
  Thead,
  Tr,
  Th,
  Tbody,
  Td,
  Tooltip,
  Link,
  Icon,
  Spacer,
} from "@chakra-ui/react";

import { FiExternalLink as ExternalLink } from "react-icons/fi";

import { getAllProblemsNotAccepted, getAllUsers } from "api/firebase";
import { CustomTag } from "components/TagsBox";
import { hasLoggedIn } from "context/AuthContext";
import Error from "components/Error";
import isUrl from "is-url";

export default function AcceptContributions() {
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [acceptedUsers, setAcceptedUsers] = useState([]);
  const [acceptedUser, setAcceptedUser] = useState(false);
  const { user } = UserAuth();

  async function fetchAllUsers() {
    const data = await getAllUsers();
    setAcceptedUsers([]);

    for (const user of data) {
      if (!user.pending && user.accepted) {
        setAcceptedUsers((acceptedUsers) => [...acceptedUsers, user]);
      }
    }

    setLoading(false);
  }

  useEffect(() => {
    for (const someUser of acceptedUsers) {
      if (someUser.email == user.email) {
        setAcceptedUser(true);
        return;
      }
    }
    setAcceptedUser(false);
  }, [acceptedUsers]);

  useEffect(() => {
    async function fetchAllProblemsNotAccepted() {
      const data = await getAllProblemsNotAccepted();
      setProblems(data);
      setLoading(false);
    }

    setLoading(true);
    fetchAllProblemsNotAccepted();
    fetchAllUsers();
  }, []);

  if (!hasLoggedIn()) {
    return <Error text={"No tienes permisos para estar aquí."} />;
  }

  if (!acceptedUser) {
    return (
      <Information
        title={"No tienes permiso para estar aquí :("}
        text={
          <div style={{ textAlign: "center" }}>
            <p>No has sido aceptado por uno de nuestros admins todavía.</p>
          </div>
        }
        img={waiting}
      />
    );
  }

  return (
    <Box w="100%">
      <VStack w="100%">
        <Text as="b" fontSize="2xl">
          Problemas en espera de ser aceptados para contribución (
          {problems.length})
        </Text>

        <TableContainer>
          <Table variant="striped">
            <Thead>
              <Tr>
                <Th> Ver </Th>
                <Th> Título </Th>
                <Th> Historia del problema </Th>
                <Th> Temas </Th>
                {/* <Th> Estado </Th> */}
              </Tr>
            </Thead>

            {loading ? (
              <Tbody />
            ) : (
              <Tbody>
                {problems.map((problem) => {
                  return (
                    <Tr key={problem.id}>
                      <Td>
                        <Tooltip label="Ver problema detalladamente">
                          <Link href={`#/problem/${problem.id}`}>
                            <Icon
                              className="homeButtonIcon"
                              as={ExternalLink}
                              color="black"
                              isTruncated
                            />
                          </Link>
                        </Tooltip>
                      </Td>

                      <Td>
                        {isUrl(problem.url) ? (
                          <a href={problem.url}>
                            <Text as="u">{problem.title}</Text>
                          </a>
                        ) : (
                          <> {problem.title}</>
                        )}
                      </Td>

                      <Td>{problem.history.substring(0, 35) + "..."}</Td>

                      <Td>
                        {problem.topics.map((topic, index) => {
                          console.log(topic, index);
                          if (index > 0 && index % 3 === 0) {
                            return (
                              <>
                                <Spacer mt={2} />
                                <CustomTag tag={topic} />
                              </>
                            );
                          } else {
                            return <CustomTag tag={topic} />;
                          }
                        })}
                      </Td>

                      {/* <Td>
                            {problem.accepted ? "Aceptado" : "En espera"}
                          </Td> */}
                    </Tr>
                  );
                })}
              </Tbody>
            )}
          </Table>
        </TableContainer>
      </VStack>
    </Box>
  );
}
