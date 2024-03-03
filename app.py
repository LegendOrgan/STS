totals = 0
test_scores_dict = {}
weights = {
    "MATH": 4,
    "PC": 4,
    "SVT": 4,
    "AR": 2,
    "FR": 3,
    "ENG": 3,
    "HG": 2,
    "INFO": 2,
    "SPORT": 2,
    "ISLAMICEDU": 2,
    "PHILO": 2,
    "BEHAV": 1
}

for subject, weight in weights.items():
    num_tests = int(input(f"How many tests have you done in {subject}: "))
    test_scores = []

    for n in range(1, num_tests + 1):
        test_score = float(input(f"What was the result for test {n}: "))
        test_scores.append(test_score)

    test_scores_dict[subject] = test_scores


for subject, weight in weights.items():
    average_score = sum(test_scores_dict[subject]) / len(test_scores_dict[subject])
    weighted_average = average_score * weight
    totals += weighted_average

actotal = totals / 31
print(f"You got: {actotal}")
