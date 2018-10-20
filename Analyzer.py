from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
import re

token = Tokenizer()
auxiliary_filters = [POSKeepFilter(['助動詞'])]
auxiliary_analyzer = Analyzer([], token, auxiliary_filters)
noun_filters = [POSKeepFilter(['名詞'])]
noun_analyzer = Analyzer([], token, noun_filters)


def GetAllKeyword(text):  # 文章全体のkeyword
    _nouns = [token.surface.split(',')[0]
              for token in noun_analyzer.analyze(text)]
    nouns = list(set(_nouns))  # check dubled
    return nouns


def GetKeyword(array_description):  # それぞれの文章に含まれるkeywordを検索
    res = []
    for desc in array_description:
        _keywords = GetAllKeyword(desc)
        happy_set = {
            'keyword': _keywords,
            'description': desc
        }
        res.append(happy_set)
    return res


def SplitDescription(text):
    _auxiliaries = [token.surface.split(',')[0]
                    for token in auxiliary_analyzer.analyze(text)]
    auxiliaries = list(set(_auxiliaries))  # check doubled
    pos = []  # 助動詞の位置, 複数ある場合はまだ想定していない
    for auxiliary in auxiliaries:
        for i, auxiliary_position in enumerate(re.finditer(auxiliary, text)):
            pos.append(auxiliary_position.end() + i)  # 句点を入れる分，文字列の総数が多くなるので+i
    for per_pos in pos:
        text = text[:per_pos] + '.' + text[per_pos:]
    splited_text = text.split('.')
    return GetKeyword(splited_text)


def AnalyzedDescription(file=''):
    if not file:
        return None
    f = open(file)
    desc = f.read()
    f.close()
    response = {
        'per_narration': SplitDescription(desc),
        'keywords': GetAllKeyword(desc)
    }
    return response
