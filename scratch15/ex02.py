import math
from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import numpy as np
from typing import NamedTuple, Any


# Candidate = namedtuple('Candidate', ('level', 'lang', 'tweets', 'phd', 'result'))
class Candidate(NamedTuple):  # NamedTuple을 상속받는 클래스 선언
    level: str
    lang: str
    tweets: bool
    phd: bool
    result: bool = None  # 클래스 선언 방식의 NamedTuple은 field의 기본값을 설정 가능


def uncertainty(p):
    """0 <= p <= 1
    확률 p=0이면 사건이 절대 발생하지 않음 -> 불확실성 0
    확률 p=1이면 사건이 항상 발생 -> 불확실성 0
    확률 0<p<1이면 사건이 발생할 수도 안할 수도 있음 -> 불확실성 있음"""
    return -p * math.log(p, 2)


def entropy(class_probabilities):
    """ 엔트로피: 각 클래스의 불확실성의 정도를 모두 더한 값
    주어진 확률의 리스트에 대해서 엔트로피를 계산
    E = sum(i) [uncertainty(p_i)] = -p_1 * log(p_1) - p_2 * log(p_2) - ..."""
    ent = 0
    for p in class_probabilities:
        if p != 0:  # p=0이면 log(P) 계산 시 에러 발생
            ent += uncertainty(p)
    return ent


def binary_entropy(p):
    """사건이 일어날 확률 p, 일어나지 않을 확률 (1-p)
    Entropy = -p * log(p) - (1-p) * log(1-p)"""
    return uncertainty(p) + uncertainty(1-p)


def class_probabilities(labels):
    total_count = len(labels)
    counts = Counter(labels)  # {label_1: cnt_1, label_2: cnt_2, ...}
    print(counts)
    probabilities = [count / total_count for count in counts.values()]
    return probabilities


def partition_by(dataset, attr_name):
    """NamedTuple들의 리스트로 이루어진 dataset을 NamedTuple의 특정 attribute로 partitioning"""
    partitions = defaultdict(list)  # list를 value로 갖는 dict
    for sample in dataset:
        # 해당 attr_name의 값을 찾아서
        key = getattr(sample, attr_name)
        # dict의 키로 사용해서 sample을 저장
        partitions[key].append(sample)
    return partitions


def partition_entropy_by(dataset, by_partition, by_entropy):
    """by_partition(attr_name)으로 분리된 각 파티션에서 by_entropy(label_name)의 엔트로피 각각 계산
    파티션 내에서의 (엔트로피 * 파티션 비율)의 합을 리턴"""
    # 파티션 분리
    partitions = partition_by(dataset, by_partition)

    # 클래스(레이블)별 확률 계산을 위해 레이블 리스트 만들기
    labels = []
    for partition in partitions.values():  # 파티션 개수만큼 반복
        values = []
        for sample in partition:  # 파티션의 원소 개수만큼 반복
            values.append(getattr(sample, by_entropy))
        labels.append(values)
    print(labels)
    # 각 파티션이 차지하는 비율 계산, 각 파티션의 엔트로피에 비율 곱하기
    total_count = sum(len(label) for label in labels)
    ent = 0
    for label in labels:
        # 파티션이 가지고 있는 클래스의 확률 리스트
        cls_prob = class_probabilities(label)  # [2/5, 3/5]
        part_ent = entropy(cls_prob)  # 파티션의 엔트로피
        # 파티션 엔트로피 * 파티션의 비율
        ent += part_ent * len(label) / total_count
    return ent


class Leaf(NamedTuple):  # Leaf는 NamedTuple을 상속받는 클래스
    value: Any


class Split(NamedTuple):
    attribute: str  # 트리에서 가지(branch)가 나뉘는 기준
    subtree: dict


def predict(model, sample):
    """sample을 model(의사결정나무)에 적용했을 때 예측결과를 리턴"""
    if isinstance(model, Leaf):
        # model이 최종 노드인 Leaf 타입이면 Leaf의 value(값) 리턴
        return model.value

    # model이 Leaf가 아니면 가지를 따라 내려가야 하므로 샘플의 attribute 값을 찾아 해당 가지로 내려감
    subtree_key = getattr(sample, model.attribute)
    print('subtree_key:', subtree_key)

    subtree = model.subtree[subtree_key]
    return predict(subtree, sample)


def build_tree(dataset, by_splits, target):
    print('\n>>> Building Tree ...')
    print(f'dataset({len(dataset)}) = {dataset}')
    print(f'by_splits = {by_splits}, target = {target}')

    # target의 개수 세기 - Counter 객체 생성 {True: x, False:y}
    target_counts = Counter(getattr(sample, target) for sample in dataset)
    print('target_counts:', target_counts)
    # Counter의 length가 1이면, Leaf를 생성하고 종료
    if len(target_counts) == 1:
        keys = list(target_counts.keys())
        # dict의 keys()가 리턴하는 타입은 리스트가 아니어서 [] 연산자 사용 불가
        result = keys[0]  # True 또는 False
        leaf = Leaf(result)
        print('leaf:', leaf)
        return leaf

    # 트리의 depth가 깊어져서 더이상 서브트리를 나눌 기준이 없으면
    if not by_splits:  # if len(by_splits) == 0:
        return Leaf(list(target_counts.keys())[0])

    # len(Counter)가 1이 아니면 파티션을 나눌 수 있음
    # by_splits(가지 나누는 기준)의 각 변수로 파티션 분리
    # 각 파티션별 엔트로피 계산, 가장 낮은 엔트로피 선택
    # partition_entropy_by(dataset, by_split, by_entropy)를 호출할 수 있는 wrapper 함수(helper 함수) 작성
    def split_entropy(split_attr):
        result = partition_entropy_by(dataset, split_attr, target)
        print('split entropy =', result)
        return result

    best_splitter = min(by_splits, key=split_entropy)
    print('best_splitter:', best_splitter)

    # 선택된 변수(엔트로피 최솟값을 주는 변수)로 파티션 생성
    partitions = partition_by(dataset, best_splitter)
    print('partitions:', partitions)

    # 선택한 변수를 제외한 나머지 변수 sub-tree 만들기
    new_splits = [x for x in by_splits if x != best_splitter]
    print('제거 후 by_splits:', new_splits)
    subtree = {k: build_tree(subset, new_splits, target) for k, subset in partitions.items()}

    # Split 객체를 생성해서 리턴
    return Split(best_splitter, subtree)


if __name__ == '__main__':
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, True, False),
                  Candidate('Mid', 'Python', False, False, True),
                  Candidate('Junior', 'Python', False, False, True),
                  Candidate('Junior', 'R', True, False, True),
                  Candidate('Junior', 'R', True, True, False),
                  Candidate('Mid', 'R', True, True, True),
                  Candidate('Senior', 'Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior', 'Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]

    # uncertainty 함수 그래프
    x_pts = np.linspace(0.0001, 1, 100)
    y_pts = [uncertainty(x) for x in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('y = p * log(p)')
    plt.xlim(0.0)  # 0 <= x
    plt.ylim(0.0)  # 0 <= y
    plt.show()

    # binary_entropy 함수 그래프
    x_pts = np.linspace(0.0001, 0.9999, 100)
    y_pts = [binary_entropy(x) for x in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('binary entropy')
    plt.axvline(x=0.5, color='0.75')
    plt.xlim(0)
    plt.ylim(0)
    plt.show()

    # entropy 함수 테스트
    rain_prob = [1, 0]  # 비가 올 확률 100%
    ent = entropy(rain_prob)
    print('entropy =', ent)  # 엔트로피 = 0 (최소 엔트로피/불확실성)

    rain_prob = [0.5, 0.5]  # 비가 올 확률 50%
    print('entropy =', entropy(rain_prob))  # 엔트로피 = 1.0 (최대 엔트로피/불확실성)

    rain_prob = [0.9, 0.1]  # 비가 올 확률 90%
    print('entropy =', entropy(rain_prob))  # 엔트로피 = 0.47

    # class_probabilities 함수 테스트
    levels = ['junior', 'senior', 'mid', 'junior']
    # P(junior) = 2/4, P(senior) = 1/4, P(mid) = 1/4
    cls_prob = class_probabilities(levels)
    print(cls_prob)

    # partition_by 함수 테스트
    partition_by_level = partition_by(candidates, 'level')
    print('partition_by_level:', partition_by_level)

    # partition_entropy_by 함수 테스트
    # 전체 지원자들을 level로 파티션을 나눠 result의 엔트로피 계산
    ent_level = partition_entropy_by(candidates, 'level', 'result')
    print('entropy partitioned by level:', ent_level)
    ent_lang = partition_entropy_by(candidates, 'lang', 'result')
    print('entropy partitioned by lang:', ent_lang)
    ent_tweets = partition_entropy_by(candidates, 'tweets', 'result')
    print('entropy partitioned by tweets:', ent_tweets)
    ent_phd = partition_entropy_by(candidates, 'phd', 'result')
    print('entropy partitioned by phd:', ent_phd)

    hire_tree = Split(
        'level',  # branch 나누는 기준
        # sub-tree
        {'Senior': Split(
            'tweets',
            {True: Leaf(True), False: Leaf(False)}
        ),
         'Mid': Leaf(True),  # Leaf(합격)
         'Junior': Split(
             'phd',
             {True: Leaf(False), False: Leaf(True)}
         )}
    )

    c1 = Candidate('Senior', 'Java', False, False, False)
    result = predict(hire_tree, c1)
    print('result =', result)

    c2 = Candidate('Mid', 'Python', False, False, True)
    result = predict(hire_tree, c2)
    print('합격 여부 =', result)

    # build_tree 함수 테스트
    tree = build_tree(candidates, ['level', 'lang', 'tweets', 'phd'], 'result')
    print(tree)


