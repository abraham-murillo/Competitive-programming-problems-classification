export const kTopics = [
  "data structures",
  "geometry",
  "graphs",
  "greedy",
  "math",
  "number theory",
  "sortings",
  "strings",
]

export function createTags(topics) {
  return topics.map(topic => {
    return {
      id: topic,
      name: topic
    };
  });
}

export function flattenTags(topics) {
  return topics.map(topic => topic.name);
}

export const kTopicsSuggestions = createTags(kTopics);