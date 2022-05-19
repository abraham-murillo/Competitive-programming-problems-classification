import React, { useEffect, useState } from "react";

import { Container, HStack, Kbd } from "@chakra-ui/react";
import { Tabs, TabList, Tab, TabPanels, TabPanel, Icon } from "@chakra-ui/react";

function PrettyTab(props) {
  const { icon, text, command } = props;

  return (
    <Tab>
      <HStack>
        {icon}

        <p>{text}</p>

        {command && (
          <span>
            <Kbd>Ctrl</Kbd>+<Kbd>{command}</Kbd>
          </span>
        )}
      </HStack>
    </Tab>
  );
}

export default function EasyTabs(props) {
  const { children } = props;
  const [tabIndex, setTab] = useState(0);

  useEffect(() => {
    window.addEventListener("keyup", handleShorcuts);
    return () => {
      window.removeEventListener("keyup", handleShorcuts);
    };
  }, []);

  function handleShorcuts(key) {
    if (key.ctrlKey) {
      // console.log(key.which);
      if (49 <= key.which && key.which <= 49 + children.length - 1) {
        setTab(key.which - 49);
      }
    }
  }

  const tabs = children.map((child, index) =>
    <PrettyTab key={index}
      text={child.props.text}
      icon={child.props.icon}
    // command={index + 1}
    />
  )

  const panels = children.map((child, index) =>
    <TabPanel>
      {child}
    </TabPanel>
  );

  return (
    <Tabs
      variant="enclosed"
      size="sm"
      index={tabIndex}
      onChange={(e) => setTab(e)}>
      <TabList>
        {tabs}
      </TabList>

      <TabPanels>
        {panels}
      </TabPanels>
    </Tabs>
  )
}