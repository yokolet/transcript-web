import graphene
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'eng_to_kana'))
from eng_to_kana import EngToKana

etk = EngToKana()

class Transcription(graphene.ObjectType):
    english = graphene.String()
    katakana = graphene.List(graphene.String)

class Transcriptions(graphene.ObjectType):
    english = graphene.List(graphene.String)
    katakana = graphene.List(graphene.List(graphene.String))

class Query(graphene.ObjectType):
    transcript = graphene.Field(Transcription, word=graphene.String(required=True))
    transcripts = graphene.Field(Transcriptions, words=graphene.List(graphene.String))

    def resolve_transcript(self, info, word):
        return {
            "english": word,
            "katakana": etk.transcript(word)
        }

    def resolve_transcripts(self, info, words):
        return {
            "english": words,
            "katakana": etk.fromWordList(words)
        }

schema = graphene.Schema(query=Query)