export async function getTokens(text) {
  return await fetch("/tokenizer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(text),
  })
    .then((response) => response.json())
    .catch((error) => error);
}

export async function getFilteredText(text) {
  return await fetch("/filteredText", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(text),
  })
    .then((response) => response.json())
    .catch((error) => error);
}

export async function getPredictedTopics(text) {
  return await fetch("/predictedTopics", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(text),
  })
    .then((response) => response.json())
    .catch((error) => error);
}
