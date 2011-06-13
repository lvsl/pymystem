# import public api here

'''
design:

                              +----------+
                              | document |
                              +----+-----+
                                   |
                                   |
                           +-------+--------+
                           |                |
                           |                |
                       +---+----+       +---+----+
                       | word#1 | . . . | word#N |
                       +---+----+       +--------+
                           |
                           |
                  +--------+--------+
                  |                 |
                  |                 |
             +----+----+       +----+----+
             | lemma#1 | . . . | lemma#N |
             +----+----+       +---------+
                  |
                  |
       +----------+---------+
       |                    |
       |                    |
+------+-----+       +------+-----+
| grammeme#1 | . . . | grammeme#N |
+------------+       +------------+



API is similar to lxml and nltk
flow:
mystem -> Parser -> Document -> Word -> Lemma -> Grammeme

***

== API TODO: ==
Top-level fucntions:
  mystem.parse()
  mystem.fromstring()
  mystem.tosting()
  mystem.sentinize()
  mystem.tokenize()
  mystem.serialize()

Top-level classes:
  mystem.Parser
  mystem.Document
  mystem.Word
  mystem.Lemma
  mystem.Grammeme

Top-level modules:
  mystem.util

Environment variables:
  MYSTEM_PATH

***

== API OF THE CLASSES: ==
Parser:
  Parser.parse()

Document:
  Document().docid
  Document().words
  Document().text
  Document().__contains__()
  Document().__len__()
  Document().__str__()
  Document().__repr__()

Word:
  Word().orig
  Word().lemmas
  Word().lemmas_list
  Word().parent_doc
  Word().__eq__()
  Word().__contains__()
  Word().__str__()
  Word().__repr__()

Lemma:
  Lemma().ipc
  Lemma().lemma
  Lemma().parent_word
  Lemma().grammems
  Lemma().gr_list
  Lemma().is_bound_to_word()
  Lemma().gr_list2str()
  Lemma().__str__()
  Lemma().__repr__()
  Lemma().__eq__()
  Lemma().__contains__()

Grammeme:
  Grammeme.PARTS_OF_SPEECH
  Grammeme.TENSE
  Grammeme.CASE
  Grammeme.NUMBER
  Grammeme.INCLANSION
  Grammeme.ADJ_FORM
  Grammeme.COMP_DEGR
  Grammeme.PERSON
  Grammeme.GENDER
  Grammeme.ASPECT
  Grammeme.ANINIMATION
  Grammeme.TRANSITION
  Grammeme.OTHER
  Grammeme.get_attr_kind()
  Grammeme().tag
  Grammeme().attrs
  Grammeme().parent_lemma
  Grammeme().__eq__()
  Grammeme().__contains__()
  Grammeme().__str__()
  Grammeme().__repr__()

'''

from mystem._grammeme import Grammeme
from mystem._lemma import Lemma
from mystem._word import Word
from mystem._document import Document
from mystem._parser import Parser
