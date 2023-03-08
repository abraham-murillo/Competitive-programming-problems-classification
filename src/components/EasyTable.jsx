import React from "react"
import { TableContainer, Table, Thead, Tbody, Tr, Th, Td, Text } from "@chakra-ui/react";

export default function EasyTable(props) {
  const { headers, values } = props;

  function getProperties(value) {
    if (headers) {
      return headers;
    }

    let properties = []
    for (const property in value)
      properties.push(property)
    return properties;
  }

  function getHeaders() {
    return headers ? headers : getProperties(values[0]);
  }

  // console.log("headers:", headers, "values:", values);

  return (
    <TableContainer>
      <Table size='sm'>
        <Thead>
          <Tr>
            {getHeaders().map((header) => <Th> {header} </Th>)}
          </Tr>
        </Thead>

        <Tbody>
          {values.length && (
            values.map((value, index) =>
              <Tr key={index}>
                {getProperties(value).map((prop, index) =>
                  <Td key={index}> {value[prop].toString()} </Td>
                )}
              </Tr>
            )
          )}
        </Tbody>
      </Table>
    </TableContainer>
  )
}