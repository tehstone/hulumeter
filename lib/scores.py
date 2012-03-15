import memcache
from pybing import Bing


class Searcher:
    def _num_results_for(self, term):
        if term == 'good':
            return  123
        elif term == 'bad':
            return 103
        else:
            return 0

    def get_scores(self, *terms):
        scores = {}
        for term in terms:
            scores[term] = self._num_results_for(term)
        return scores


class BingSearcher(Searcher):
    def __init__(self, app_id):
        self.bing = Bing(app_id)

    def _num_results_for(self, term):
        response = self.bing.search_web(term)
        return response['SearchResponse']['Web']['Total']

class ScoreViewer():
    _mc = memcache.Client(['localhost:11211'])
    def get_scores(self, *terms):
        scores = {}
        for term in terms:
            scores[term] = ScoreViewer._mc.get(term)
        return scores
