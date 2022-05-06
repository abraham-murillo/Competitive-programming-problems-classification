import React from "react";

import { Container, HStack, Kbd } from "@chakra-ui/react";
import { Tabs, TabList, TabPanels, Tab, TabPanel } from "@chakra-ui/react";

import { BiCodeCurly, BiCodeBlock } from "react-icons/bi";
import CreateProblem from "./createInfo/CreateProblem";

function PrettyTab(props) {
  const { icon, text, command } = props;

  return (
    <Tab>
      <HStack>
        {icon}
        <p>{text}</p>
        <span>
          <Kbd>Ctrl</Kbd>+<Kbd>{command}</Kbd>
        </span>
      </HStack>
    </Tab>
  );
}

export default function MainPage() {
  const [tabIndex, setTab] = React.useState(0);

  React.useEffect(() => {
    window.addEventListener("keyup", handleShorcuts);
    return () => {
      window.removeEventListener("keyup", handleShorcuts);
    };
  }, []);

  function handleShorcuts(key) {
    if (key.ctrlKey) {
      // console.log(key.which);
      if (49 <= key.which && key.which <= 52) {
        setTab(key.which - 49);
      }
    }
  }

  return (
    <Container maxW={"container.lg"} mt={2} h={"90vh"} padding={"0"}>
      <Tabs
        variant={"enclosed"}
        size={"sm"}
        index={tabIndex}
        onChange={(e) => setTab(e)}>
        <TabList>
          <PrettyTab
            text={"Analizar código"}
            icon={<BiCodeBlock />}
            command={1} />

          <PrettyTab
            text={"Crear JSON"}
            icon={<BiCodeCurly />}
            command={2} />
        </TabList>

        <TabPanels>
          {/* <TabPanel>
            <WritingWindow />
          </TabPanel> */}

          <TabPanel>
            <CreateProblem />
          </TabPanel>
        </TabPanels>

      </Tabs>
    </Container>
  );
}