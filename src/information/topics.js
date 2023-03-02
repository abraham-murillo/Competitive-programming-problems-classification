export const kTopics = [
  "sortings",
  "strings",
  "greedy",
  "number theory",
  "math",
  "graphs",
  "geometry",
  "data structures",
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