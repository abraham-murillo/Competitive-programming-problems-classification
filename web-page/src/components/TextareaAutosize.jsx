import React, { useEffect, useState } from "react";
import { Textarea } from "@chakra-ui/react";

export default function TextareaAutosize(props) {
  const { value, onChange } = props;
  const [rows, setRows] = useState(1);

  function getEndOfLinesCount(text) {
    let cnt = 0;
    for (let ch of text)
      if (ch === '\n') cnt++;
    return cnt + 1;
  }

  useEffect(() => {
    setRows(getEndOfLinesCount(value));
  }, [value]);

  return (
    <Textarea
      rows={rows}
      resize={'vertical'}
      value={value}
      onChange={(e) => onChange(e.target.value)} />
  );
}
