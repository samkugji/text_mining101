ner_templates = [
    (('<ACTOR>', ('나온', '출연한', '출연')), 1),
    (('<ACTOR>', ('가', '이'), ('나온', '출연한', '출연')), 2),
    (('<DIRECTOR>', ('만든', '제작', '제작한', '감독', '감독한')), 1),
    (('<DIRECTOR>', ('가', '이'), ('만든', '제작', '제작한', '감독', '감독한')), 2)
]

def named_entity_extractor(tokens, verbose=True):
    def match(tokens, template, verbose=verbose):
        template_pattern = template[0]
        template_begin = template[1]
        template_end = len(template_pattern) - template_begin

        if verbose:
            print("<named_entity_extractor function>")
            print("template_pattern:", template_pattern)
            print("template_begin:", template_begin)
            print("template_end:", template_end)
            print()

        # NER을 뽑고자 하는 텍스트가 template보다 짧으면 판단불가
        if len(tokens) < template_begin:
            return {}

        matched_entities = {}
        for b in range(template_begin, (len(tokens) - template_end + 1)):
            e = b + template_end
            subtokens = tokens[b - template_begin: e]

            if verbose:
                print("<match function>")
                print("b:%d, e:%d" % (b, e))
                print("subtokens: ", subtokens)
                print()

            matched = True
            named_entity = None
            entity_type = None
            # subtokens와 template의 pattern들을 비교
            for token, template_term in zip(subtokens, template_pattern):
                if (template_term[0] == '<') and (template_term[-1] == '>'):
                    named_entity = token
                    entity_type = template_term
                    continue
                if (token in template_term) == False:
                    matched = False
                    break

            #TODO: ('가', '이') 제외필요

            if (matched) and (named_entity is not None) and (entity_type is not None):
                matched_entities[named_entity] = entity_type

        return matched_entities

    matched_entities = {}
    for template in ner_templates:
        matched_entities.update(match(tokens, template))

    return matched_entities