from bs4 import BeautifulSoup
import math


class Parser(object):
    def __init__(self):
        pass

    def parse(self, path):
        try:
            soup = BeautifulSoup(open(path, encoding='utf-8'), 'html.parser')
            # print("=" * 40)
            max_headers = 7
            title = ""
            title_score = 0
            for i in range(1, 7):
                candidates = [i.getText() for i in
                              soup.find(id='pf1').find_all(
                                  "div", {"class": "h{}".format(i)})]
                # if candidates:
                #     continue

                candidate_cnt = len(candidates)
                candidates_str = " ".join(candidates)
                candidate_len = len(candidates_str)
                candidate_alnum_len = sum([i.isalnum() for i in candidates_str])
                candidate_words = len(candidates_str.split())
                candidate_nospace_str = candidates_str.replace(' ', '')
                candidate_nospace_len = len(candidate_nospace_str)
                candidate_alpha_len = sum([i.isalpha() for i in candidate_nospace_str])

                if candidate_alnum_len and candidate_alpha_len:
                    caps_ratio = sum([i.isupper() for i in candidates_str]) / candidate_alnum_len

                    level_score = (max_headers - i) / max_headers
                    cnt_score = 1 / candidate_cnt # we prefer one line
                    candidate_norm_len = 1 - abs(math.tanh((80 - candidate_len) / 50)) # 100 average title len
                    candidate_word_ratio = 1 - abs(math.tanh((7 - candidate_words) / 5)) # 7 words
                    if caps_ratio > .6:
                        caps_score = 1
                    else:
                        caps_score = 0
                    at_penalization = -1 if '@' in candidates_str else 0
                    # print(candidate_nospace_len, candidate_alpha_len)
                    non_alnum_penalization = 4 * (1 - (candidate_nospace_len / candidate_alpha_len))

                    score = level_score + cnt_score + candidate_norm_len + caps_score + candidate_word_ratio + at_penalization + non_alnum_penalization

                    if score > title_score:
                        title_score = score
                        title = candidates_str

                    # todo order in the doc
                    # todo style based eval
                    # todo multi line names

                    # print("\tlevel: {}, cnt: {}, len: {}, ratio: {}, words: {}, alnum_penal: {}, word_rat: {}, score: {}".format(
                    #     i, cnt_score, candidate_norm_len, caps_ratio, candidate_words, non_alnum_penalization, candidate_word_ratio, score))
                    #
                    # print(candidates_str[:100])

                # print("MOST PROBABLE")
                # print([i.getText() for i in
                #        soup.find(id='pf1').find_all("div", {"class": "h1"})])
                # print("2nd MOST PROBABLE")
                # print([i.getText() for i in
                #        soup.find(id='pf1').find_all("div", {"class": "h2"})])
                # print("3rd MOST PROBABLE")
                # print([i.getText() for i in
                #        soup.find(id='pf1').find_all("div", {"class": "h3"})])

            # print("*"*40)
            return title
        except Exception as e:
            print(e)
            pass
