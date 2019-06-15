# English to Katakana Transcription GraphQL Endpoint

This repository is a GraphQL Endpoint for an Englih to Katakana Transcription developed
in another repository,
[https://github.com/yokolet/transcript](https://github.com/yokolet/transcript).
For a deployment purpose, this repository contains a logic of the English to Katakana
transcription. However, the transcription itself is being developed in the other repository.
For details about transcription itslef, see [transcript](https://github.com/yokolet/transcript) repo.


The transcription finds a way to read English words in Japanese style.
The goal is to generate so-called Japanese English sound. If the Katakana sounds natrual as Japanese, the result is considered good. It is off from a native speaker-ish pronounciation,
and not for English study.


## GraphQL

At this moment, the GraphQL supports two types o queries only.

- transcript

Transcript a single word(case insensitive). The result is an array of Katakan or an error code.

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

Transcript multiple words(case insensitive) give in an array. The result is an array of array contains Katakana
or an error code.

Example:

```
query {
  transcripts(words: ["where", "amazon", "apple", "facebook", "google", "microsoft", "twitter"]) {
    english,
    katakana
  }
}
```

#### Error code
- E_DIC: the given word is not in the original IPA phonetics dictionary.

- E_KEY: the error occured while processing.


## URL

The app is live at:

[https://agile-plateau-86972.herokuapp.com/graphql](https://agile-plateau-86972.herokuapp.com/graphql)

Use GraphQL client such as [Insomnia](https://insomnia.rest/graphql/) or other and make a query.


## Credits

Yoko Harada (@yokolet)

## License

The MIT License (MIT)

Copyright (c) 2019 Yoko Harada

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.