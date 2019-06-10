import graphene

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
            "katakana": ["カタカナ"]
        }

    def resolve_transcripts(self, info, words):
        return {
            "english": words,
            "katakana": [["カタカナ"], ["イングィッシュ", "イングリッシュ"]]
        }

schema = graphene.Schema(query=Query)