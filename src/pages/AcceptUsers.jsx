import React, { useEffect, useState } from "react";
import { getAllUsers, updateUser } from "api/firebase";
import { hasLoggedIn } from "context/AuthContext";
import Error from "components/Error";
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

export default function AcceptUsers() {
  const [pendingUsers, setPendingUsers] = useState([]);
  const [acceptedUsers, setAcceptedUsers] = useState([]);
  const [rejectedUsers, setRejectedUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  async function fetchAllUsers() {
    const data = await getAllUsers();
    setPendingUsers([]);
    setAcceptedUsers([]);
    setRejectedUsers([]);

    for (const user of data) {
      console.log(user);
      if (user.pending) {
        setPendingUsers((pendingUsers) => [...pendingUsers, user]);
      } else {
        if (user.accepted) {
          setAcceptedUsers((acceptedUsers) => [...acceptedUsers, user]);
        } else {
          setRejectedUsers((rejectedUsers) => [...rejectedUsers, user]);
        }
      }
    }

    setLoading(false);
  }

  useEffect(() => {
    setLoading(true);
    fetchAllUsers();
  }, []);

  const handleAccept = async (user) => {
    await updateUser(user.id, {
      ...user,
      accepted: true,
      pending: false,
    });
    fetchAllUsers();
    console.log("Accepting ", user);
  };

  const handleReject = async (user) => {
    await updateUser(user.id, {
      ...user,
      accepted: false,
      pending: false,
    });
    fetchAllUsers();
    console.log("Rejecting ", user);
  };

  if (!hasLoggedIn()) {
    return <Error text={"No tienes permisos para estar aquí."} />;
  }

  return (
    <Box w="100%">
      <VStack w="100%">
        <Text as="b" fontSize="2xl">
          Usuarios en espera de ser aceptados ({pendingUsers.length})
        </Text>

        <TableContainer>
          <Table variant="striped">
            {loading ? (
              <Tbody />
            ) : (
              <Tbody>
                {pendingUsers.map((user) => {
                  return (
                    <Tr>
                      <Td>{user.email}</Td>
                      <Td>
                        <button onClick={() => handleAccept(user)}>
                          Aceptar
                        </button>
                      </Td>
                      <Td>
                        <button onClick={() => handleReject(user)}>
                          Rechazar
                        </button>
                      </Td>
                    </Tr>
                  );
                })}
              </Tbody>
            )}
          </Table>
        </TableContainer>

        <Text as="b" fontSize="2xl">
          Usuarios aceptados ({acceptedUsers.length})
        </Text>

        <TableContainer>
          <Table variant="striped">
            {loading ? (
              <Tbody />
            ) : (
              <Tbody>
                {acceptedUsers.map((user) => {
                  return (
                    <Tr>
                      <Td>{user.email}</Td>
                      <Td>
                        <button onClick={() => handleReject(user)}>
                          Rechazar
                        </button>
                      </Td>
                    </Tr>
                  );
                })}
              </Tbody>
            )}
          </Table>
        </TableContainer>

        <Text as="b" fontSize="2xl">
          Usuarios rechazados ({rejectedUsers.length})
        </Text>

        <TableContainer>
          <Table variant="striped">
            {loading ? (
              <Tbody />
            ) : (
              <Tbody>
                {rejectedUsers.map((user) => {
                  return (
                    <Tr>
                      <Td>{user.email}</Td>
                      <Td>
                        <button onClick={() => handleAccept(user)}>
                          Aceptar
                        </button>
                      </Td>
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
