import React from "react";
import {
  Divider,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
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