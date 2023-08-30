"""Module for metrics calculation"""
from tqdm import tqdm


def topk_accuracy(data, test_col, gold_col, k):
    """Calculates topn_accuracy for entities and relations"""
    scores = [0] * k
    for line in tqdm(range(len(data))):
        cur_range = len(data.loc[line, test_col].split(", "))
        cur_range = min(cur_range, k)
        for cand in range(cur_range):
            if data.loc[line, test_col].split(", ")[cand] == data.loc[line, gold_col]:
                for sel_cand in range(cand, k):
                    scores[sel_cand] += 1
    for j in range(k):
        index = j + 1
        print(f"Top-{index} accuracy:", scores[j] / len(data))
