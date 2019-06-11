import os
import pickledb
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from vowel_converter import VowelConverter
from consonant_converter import ConsonantConverter
from epenthetic_vowel_handler import EpentheticVowelHandler
from morae_creator import MoraeCreator
from morae_kana_converter import MoraeKanaConverter

class EngToKana:
    def __init__(self):
        dbname = os.path.join(os.path.dirname(__file__), '..', 'cmu_dict', 'cmu_ipa.pickle')
        self.db = pickledb.load(dbname, False)
        self.vowel_fn = VowelConverter().convertVowel
        self.consonant_fn = ConsonantConverter().convertConsonant
        self.epenthetic_fn = EpentheticVowelHandler().addEpentheticVowel
        self.morae_fn = MoraeCreator().createMorae
        self.kana_fn = MoraeKanaConverter().convertMorae

    def transcript(self, word):
        word = word.lower()
        try:
            phs = self.db.get(word)
            if not phs:
                return ['E_DIC']
            phs1 = [self.vowel_fn(word, ph) for ph in phs]
            phs2 = [self.consonant_fn(word, ph) for ph in phs1]
            phs3 = [self.epenthetic_fn(ph) for ph in phs2]
            moraes = [self.morae_fn(ph) for ph in phs3]
            return [self.kana_fn(m) for m in moraes]
        except KeyError:
            return ['E_KEY']

    def fromWordList(self, words):
        return [self.transcript(w.lower()) for w in words]