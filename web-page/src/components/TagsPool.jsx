import React from "react";
import {
  Box,
  HStack,
  EditableInput,
  Editable,
  EditablePreview,
  EditableTextarea,
  FormLabel,
  Flex,
  FormControl,
  Input,
  FormHelperText,
  VStack,
  Button,
  Textarea,
  useDisclosure,
  Tag
} from "@chakra-ui/react";

function MyTag(props) {
  const { text } = props;

  return (
    <Tag
      colorScheme={"blue"}
      size={'lg'}>
      {text}
    </Tag>
  );
}

export default function TagsPool() {

  return (
    <>
      <MyTag text={"Binary search"} />
    </>
  );
}
