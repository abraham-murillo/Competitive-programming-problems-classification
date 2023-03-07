import { React, useState } from "react";
import {
  Link,
  Input,
  Box,
  Spacer,
  Flex,
  Container,
  Icon,
  Tooltip,
} from "@chakra-ui/react";

import {
  BiHomeAlt as Home,
  // BiCodeCurly as Contribute,
  BiCodeBlock as DetectTopics,
  BiUserCheck as AcceptUsers,
} from "react-icons/bi";

import { AiOutlineFileAdd as Contribute } from "react-icons/ai";

import { BsUiChecks as AcceptContributions } from "react-icons/bs";

import { UserAuth } from "context/AuthContext";

export default function Navbar() {
  const [queryString, setQueryString] = useState("");
  const { user, logOut } = UserAuth();

  function handleSubmit(e) {
    e.preventDefault();
    window.location.href = "/#/searchResults/" + queryString;
  }

  return (
    <Box boxShadow={"md"}>
      <Container maxW={"container.lg"}>
        <Flex align={"center"} height={"80px"}>
          <Tooltip label="Ir al menú principal">
            <Link className="homeButton" href="/">
              <Icon
                className="homeButtonIcon"
                as={Home}
                color="black"
                isTruncated
              />
            </Link>
          </Tooltip>

          <Tooltip label="Contribuir">
            <Link ml={5} href="#/contribute">
              <Icon
                className="homeButtonIcon"
                as={Contribute}
                color="black"
                isTruncated
              />
            </Link>
          </Tooltip>

          <Tooltip label="Analizar problema">
            <Link ml={5} href="#/detectTopics">
              <Icon
                className="homeButtonIcon"
                as={DetectTopics}
                color="black"
                isTruncated
              />
            </Link>
          </Tooltip>

          {user?.displayName ? (
            <Tooltip label="Aceptar contribuciones">
              <Link ml={5} href="#/acceptContributions">
                <Icon
                  className="homeButtonIcon"
                  as={AcceptContributions}
                  color="black"
                  isTruncated
                />
              </Link>
            </Tooltip>
          ) : null}

          {user?.displayName ? (
            <Tooltip label="Aceptar usuarios">
              <Link ml={5} href="#/acceptUsers">
                <Icon
                  className="homeButtonIcon"
                  as={AcceptUsers}
                  color="black"
                  isTruncated
                />
              </Link>
            </Tooltip>
          ) : null}

          <Spacer />

          {/* <Tooltip label="Buscar un problema">
            <form onSubmit={handleSubmit}>
              <Input
                w="30vw"
                placeholder="Título del problema"
                onChange={(event) => setQueryString(event.target.value)}
                onSubmit={handleSubmit}
              />
            </form>
          </Tooltip> */}

          {user?.photoURL ? (
            <Tooltip label={user.displayName}>
              <img
                style={{
                  borderRadius: "100%",
                  width: "40px",
                  marginRight: "20px",
                }}
                src={user.photoURL}
              />
            </Tooltip>
          ) : null}

          <Tooltip label="Iniciar sesión">
            {user?.displayName ? (
              <div>
                <p>Bienvenido, {user.displayName.split(" ")[0]}!</p>
                <button ml={5} onClick={logOut}>
                  Cerrar sesión
                </button>
              </div>
            ) : (
              <Link ml={5} href="#/logIn">
                Iniciar sesión
              </Link>
            )}
          </Tooltip>
        </Flex>
      </Container>
    </Box>
  );
}
