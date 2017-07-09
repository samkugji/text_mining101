import random

from enum import Enum


class SayHelloType(Enum):
    GENENERAL = 0
    FIRST_VISIT = 1
    REVISIT = 2
    WHEN_TIME_MORNING = 3
    WHEN_TIME_NIGHT = 4

say_hello_templates = {
        SayHelloType.GENENERAL: ("<NAME>", ("ㅎㅇ", "안녕하세요?", "안녕!!", "뇽안~")),
        SayHelloType.FIRST_VISIT: (("처음뵙겠습니다", "반갑습니다. 잘 부탁드려요", "반가워"), "<NAME>"),
        SayHelloType.REVISIT: ("<NAME>", ("잘 지냈어?", "또 대화걸어줘서 고마워")),
        SayHelloType.WHEN_TIME_MORNING: (("좋은 아침", "굿모닝"), "<NAME>"),
        SayHelloType.WHEN_TIME_NIGHT: ("<NAME>", ("오늘도 밤은 기분이 좋네", "불타는 이 밤 어떻게 보내고 있어?")),
}


def say_hello(say_hello_type=None, user_name=None):
    if say_hello_type is None or type(say_hello_type) is not SayHelloType:
        say_hello_type =SayHelloType.GENENERAL

    templates = say_hello_templates[say_hello_type]
    sentence = []
    for term in templates:
        if type(term) is str:
            if (term == '<NAME>') and (user_name is not None):
                sentence.append(user_name)
                continue

        if(type(term) is tuple):
            sentence.append(random.choice(term))

    return " ".join(sentence)

# if __name__ == "__main__":
#     a = say_hello(say_hello_type=SayHelloType.WHEN_TIME_NIGHT, user_name="그대여")
#     print(a)