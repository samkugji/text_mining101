import pickle
import random

from hello import SayHelloType, say_hello
from intention import Requests, intention_classifier
from ner import named_entity_extractor


class MovieBot:

    def __init__(self, param_fname):
        with open(param_fname, "rb") as f:
            params = pickle.load(f)

        self.actor2id = params["actor2id"]
        self.actor2movie = params["actor2movie"]
        self.movie2actor = params["movie2actor"]
        self.id2movie = params["id2movie"]
        self.id2actor = params["id2actor"]

        self.dummy_message = ["자세히 말씀해 주시겠어요?", "음...", "?"]
        self.recommend_movies_message = ["추천해요", "보는게 어떨까요?", "어때요?"]
        self.fail_moive_search_message = ["잘 못찾겠어요", "마땅한 영화가 없네요"]

    def get_movie_from_actor(self, actor):
        return 0

    def recommend_movie_by_actor(self, actor):
        return 0

    def get_dummy(self):
        return random.choice(self.dummy_message)

    def process(self, query, user_name=None, condition=None):
        query = query.split()

        return self.get_dummy()
