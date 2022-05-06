import React from "react";
import { useEffect, useRef, useState } from "react";
import {
  Button,
  Divider,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
} from "@chakra-ui/react";

export default function MakeModal(props) {
  const { title, isOpen, onClose } = props;

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />

      <ModalContent>
        <ModalHeader> {title} </ModalHeader>
        <Divider />

        <ModalCloseButton />

        <ModalBody m={2}>
          {props.children}
        </ModalBody>
      </ModalContent>
    </Modal>
  );
};