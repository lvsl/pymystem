# coding: utf-8

import itertools

from mystem.util import MystemError

class Grammeme(object):
    # Taken from http://company.yandex.ru/technology/mystem/help.xml
    # Часть речи
    PARTS_OF_SPEECH = (
        'A',     # прилагательное
        'ADV',   # наречие
        'ADVPRO',# местоименное наречие
        'ANUM',  # порядковое числительное
        'APRO',  # местоименное прилагательное
        'COM',   # часть композита (первая часть сложных слов)
        'CONJ',  # союз
        'INTJ',  # междометие
        'NUM',   # числительное
        'PART',  # частица
        'PR',    # предлог
        'S',     # существительное
        'SPRO',  # местоимение
        'V',     # глагол
    )

    # Время (глаголов)
    TENSE = (
        'наст',   # настоящее
        'непрош', # непрошедшее
        'прош',   # прошедшее
    )

    # Падеж
    CASE = (
        'им',   # именительный
        'род',  # родительный
        'дат',  # дательный
        'вин',  # винительный
        'твор', # творительный
        'пр',   # предложный
        'парт', # партитив (второй родительный)
        'местн',# местный (второй предложный)
        'зват', # звательный
    )

    # Число
    NUMBER = (
        "ед",  # единственное
        "мн",  # множественное
    )

    # Репрезентация и наклонение глагола
    INCLANSION = (
        "деепр", # деепричастие
        "инф",   # инфинитив
        "прич",  # причастие
        "изъяв", # изьявительное наклонение
        "пов",   # повелительное наклонение
    )

    # Форма прилагательных
    ADJ_FORM = (
        'кр',     # краткая
        'полн',   # полная
        'притяж', # притяжательная
    )

    # Степень сравнения
    COMP_DEGR = (
        'прев', # превосходная
        'срав', # сравнительная
    )

    # Лицо глагола
    PERSON = (
        '1-л', # 1-е лицо
        '2-л', # 2-е лицо
        '3-л', # 3-е лицо
    )

    # Род
    GENDER = (
        'жен',  # женский
        'муж',  # мужской
        'сред', # средний
    )

    # Вид (аспект) глагола
    ASPECT = (
        'сов',   # совершенный
        'несов', # несовершенный
    )

    # Залог
    VOICE = (
        'действ', # действительный
        'страд',  # страдательный
    )

    # Одушевленность
    ANINIMATION = (
        'од',     # одушевленное
        'неод',   # неодушевленное
    )

    # Переходность
    TRANSITION = (
        'пе', # переходный глагол
        'нп', # непереходный глагол
    )

    # Прочие обозначения
    OTHER = (
        'вводн', # вводное слово
        'гео',   # географическое название
        'затр',  # образование формы затруднено
        'имя',   # имя собственное
        'искаж', # искаженная форма
        'мж',    # общая форма мужского и женского рода
        'обсц',  # обсценная лексика
        'отч',   # отчество
        'прдк',  # предикатив
        'разг',  # разговорная форма
        'редк',  # редко встречающееся слово
        'сокр',  # сокращение
        'устар', # устаревшая форма
        'фам',   # фамилия
    )

    ALL_ATTRS = tuple(itertools.chain(
        TENSE,
        CASE,
        NUMBER,
        INCLANSION,
        ADJ_FORM,
        COMP_DEGR,
        PERSON,
        GENDER,
        ASPECT,
        VOICE,
        ANINIMATION,
        TRANSITION,
        OTHER,
    ))

    def __init__(self, tag, *attrs):
        if tag not in self.PARTS_OF_SPEECH:
            raise MystemError("Unknown grammeme: %s" % tag)
        for a in attrs:
            if not isinstance(a, basestring):
                raise MystemError("Attributs must be instances of basestring"
                                  " not %s: %s" % (type(a), a))
            if a not in self.ALL_ATTRS:
                raise MystemError("Unknown attribute: '%s'" % a)
        self.parent_lemma = None
        self.tag = tag
        self.attrs = attrs

    @property
    def is_bound_to_lemma(self):
        return self.parent_lemma is not None

    @classmethod
    def get_attr_kind(cls, value):
        if value in cls.TENSE: return 'TENSE'
        if value in cls.CASE: return 'CASE'
        if value in cls.NUMBER: return 'NUMBER'
        if value in cls.INCLANSION: return 'INCLANSION'
        if value in cls.ADJ_FORM: return 'ADJ_FORM'
        if value in cls.COMP_DEGR: return 'COMP_DEGR'
        if value in cls.PERSON: return 'PERSON'
        if value in cls.GENDER: return 'GENDER'
        if value in cls.ASPECT: return 'ASPECT'
        if value in cls.VOICE: return 'VOICE'
        if value in cls.ANINIMATION: return 'ANINIMATION'
        if value in cls.TRANSITION: return 'TRANSITION'
        if value in cls.OTHER: return 'OTHER'

        raise MystemError("attr of an unknown kind: %s" % value)

    def __eq__(self, other):
        if (isinstance(other, self.__class__) and
                self.tag == other.tag and
                self.attrs == other.attrs):
            return True
        else:
            return False

    def __contains__(self, item):
        return item in self.attrs

    def __str__(self):
        s = '<%s instance. Tag: %s. %s>' % (
            self.__class__.__name__,
            self.tag,
            '. '.join(["%s: '%s'" % (self.get_attr_kind(a), a) for a in self.attrs])
        )
        return s

    def __repr__(self):
        s = '<%s instance at %s. Tag: %s. %s>' % (
            self.__class__.__name__,
            hex(id(self)),
            self.tag,
            '. '.join(["%s: '%s'" % (self.get_attr_kind(a), a) for a in self.attrs])
        )
        return s

