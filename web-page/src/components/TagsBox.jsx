import React, { useCallback, useRef, useState } from "react";
import {
  Tag,
  TagCloseButton,
  TagLabel
} from "@chakra-ui/react";

import "styles/TagsBox.css"
import ReactTags from 'react-tag-autocomplete'

export function CustomTag({ tag, onDelete }) {
  return (
    <Tag
      borderRadius="full"
      size="lg"
      colorScheme="blue"
      onClick={onDelete}>
      <TagLabel> {tag.name} </TagLabel>
      <TagCloseButton />
    </Tag>
  );
}

export default function TagsBox(props) {
  const { tags, setTags, suggestions } = props;

  function handleDelete(deleteIndex) {
    setTags(tags.filter((tag, index) => index !== deleteIndex));
  };

  function handleAddition(tag) {
    setTags([...tags, tag]);
  };

  return (
    <ReactTags
      tags={tags}
      delimiters={[',', '\n']}
      suggestions={suggestions}
      onDelete={handleDelete}
      onAddition={handleAddition}
      tagComponent={CustomTag}
      {...props}
      minQueryLength={2}
      inputFieldPosition="bottom"
    />
  );
}
