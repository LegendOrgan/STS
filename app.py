total = 0
matmo = {
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

for key, value in matmo.items():
    i = input(f"Total in {key}: ")
    total += float(i)*value


actotal = total/31
print(f"You got: {actotal}" )