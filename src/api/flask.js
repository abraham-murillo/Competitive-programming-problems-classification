const PORT = "http://localhost:5000"

export async function getTokens(text) {
  return await fetch("/tokenizer", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(text)
  }).then((response) => response.json())
    .catch((error) => error);
}
