def solution(relation):
    col_len = len(relation[0])
    row_len = len(relation)

    candidate_keys = []

    def gen_combinations(start, depth, max_depth, curr, result_combs):
        if depth == max_depth:
            result_combs.append(curr[:])
            return
        for i in range(start, col_len):
            curr.append(i)
            gen_combinations(i + 1, depth + 1, max_depth, curr, result_combs)
            curr.pop()

    for length in range(1, col_len + 1):
        combinations = []
        gen_combinations(0, 0, length, [], combinations)

        for cols in combinations:
            minimality = True
            row_set = set()

            # 최소성 검사
            for key in candidate_keys:
                if set(key).issubset(set(cols)):
                    minimality = False
                    break
            if not minimality:
                continue

            # 유일성
            for r in relation:
                row_str = "".join(r[c] for c in cols)
                row_set.add(row_str)

            if len(row_set) == row_len:
                candidate_keys.append(cols)

    return len(candidate_keys)