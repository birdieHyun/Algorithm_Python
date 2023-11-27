from itertools import combinations


def is_valid_sequence(teams, sequence):
    wins = [0] * len(teams)
    current_teams = [team[:] for team in teams]

    for match in sequence:
        team1_idx, team2_idx = match
        team1 = current_teams[team1_idx]
        team2 = current_teams[team2_idx]

        if sum(team1) > sum(team2):
            wins[team1_idx] += 1
            if wins[team1_idx] >= 2:
                return False
        else:
            wins[team2_idx] += 1
            if wins[team2_idx] >= 2:
                return False

    return all(win > 0 for win in wins)


def generate_match_combinations(teams, sequence, match_combinations):
    if len(sequence) == len(match_combinations):
        return is_valid_sequence(teams, sequence)

    for match in match_combinations:
        if match not in sequence:
            sequence.append(match)
            if generate_match_combinations(teams, sequence, match_combinations):
                return True
            sequence.pop()

    return False


def solution(teams):
    team_indices = list(range(len(teams)))
    all_match_combinations = list(combinations(team_indices, 2))

    for k in range(1, len(all_match_combinations) + 1):
        match_combinations = list(combinations(all_match_combinations, k))

        for match_combo in match_combinations:
            sequence = []
            if generate_match_combinations(teams, sequence, match_combo):
                return k

    return 0


# 초기 팀 데이터
teams = [[1, 14], [2, 12], [3, 10], [4, 8]]

valid_count = solution(teams)
print(valid_count)  # 결과 출력
