import React, { useEffect, useState } from "react";
import { Textarea } from "@chakra-ui/react";

export default function TextareaAutosize(props) {
  const { text, setText } = props;
  const [rows, setRows] = useState(1);

  function getEndOfLinesCount(text) {
    let cnt = 0;
    for (let ch of text)
      if (ch === '\n') cnt++;
    return cnt + 1;
  }

  useEffect(() => {
    setRows(getEndOfLinesCount(text));
  }, [text]);

  return (
    <Textarea
      rows={rows}
      resize={'vertical'}
      value={text}
      onChange={(e) => setText(e.target.value)} />
  );
}
