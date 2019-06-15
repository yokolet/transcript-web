# English to Katakana Transcription GraphQL Endpoint

This repository is for a GraphQL Endpoint to add a web feature to
[https://github.com/yokolet/transcript](https://github.com/yokolet/transcript).
For a deployment purpose, this repository contains main logic of the transcript repo.
However, the transcription itself is being developed in the other repository.

The transcription means to create a Katakana (how to read in Japanese way) from English word.
The goal is to generate so-called Japanese English, so this is not for studying English.
The purpose is to find a clue how to pronounce English words sound like natural Japanese.

## GraphQL

At this moment, the GraphQL supports two types o queries only.

- transcript

Example:

```
query {
  transcript(word: "english") {
    english,
    katakana
  }
}
```

- transcripts

Example:

```
query {
  transcripts(words: ["where", "amazon", "apple", "facebook", "google", "microsoft", "twitter"]) {
    english,
    katakana
  }
}
```

## URL

The app is live at:

[https://agile-plateau-86972.herokuapp.com/graphql](https://agile-plateau-86972.herokuapp.com/graphql)

Use GraphQL client such as [Insomnia](https://insomnia.rest/graphql/) or other and make a query.