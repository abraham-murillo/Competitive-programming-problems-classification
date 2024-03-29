import React, { useCallback, useRef, useState } from "react";
import {
  Tag,
  TagCloseButton,
  TagLabel
} from "@chakra-ui/react";

import "styles/TagsBox.css"

export function CustomTag({ tag }) {
  return (
    <Tag
      ml={1}
      borderRadius="full"
      size="lg"
      colorScheme="blue">
      <TagLabel> {tag} </TagLabel>
    </Tag>
  );
}

export default function TagsBox(props) {
  const { tags, setTags, suggestions } = props;

  function handleDelete(deleteIndex) {
    setTags(tags.filter((tag, index) => index !== deleteIndex));
  };

  function handleAddition(tag) {
    let exists = false
    tags.forEach(element => {
      if (element.id === tag.id) {
        exists = true;
        return
      }
    });

    if (!exists) {
      setTags([...tags, tag]);
    }
  };

  return (
    // <ReactTags
    //   tags={tags}
    //   delimiters={[',', '\n']}
    //   suggestions={suggestions}
    //   onDelete={handleDelete}
    //   onAddition={handleAddition}
    //   tagComponent={CustomTag}
    //   {...props}
    //   minQueryLength={2}
    //   inputFieldPosition="bottom"
    // />
    <>
      {tags.map((tag) => (
        <CustomTag tag={tag} />
      ))}
    </>
  );
}
