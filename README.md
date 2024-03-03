
# Semester Total Score (STS) Calculator (Tronc Commun, Morocco)
This improved Python application assists you in calculating your semester total score (STS), taking into account your course grades, coefficient (معامل), and test performance for Tronc Commun subjects in Morocco.

## Key Features:

- **User-friendly interface:** Guides you through the process of providing subject information, number of tests, and individual test scores.
- **Accurate calculations:** Calculates average test scores, weighted totals based on credits, and the overall semester total score considering Tronc Commun specifics.
- **Clear output:** Displays your calculated semester total score.

## How to Use:

**Save the code:** Save the provided code as a Python file (e.g., tronc_commun_sts.py).
**Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:
python tronc_commun_sts.py

**Follow the prompts:** Enter the requested information for each subject, including:
- *Number of tests:* Number of tests you took in the subject.
- *Individual test scores:* Scores for each test out of 20.
- *View your semester total score:* The script will display your calculated semester total score, helping you gauge your academic performance.

### Example Output:
Let's say you have these details for MATH:

- Number of tests: 3
- Test 1: 12
- Test 2: 16
- Test 3: 17

After you enter this, you will get asked for PC then SVT then... until BEHAVIOR (سلوك), after you will get the total semester point.

## Explanation:

Average test score for MATH: (12 + 16 + 17) / 3 = 15
Weighted total: 15 (average test score) * 4 (coefficient) = 60
Semester total score: (weighted total of all subjects) / 31 (total coefficient) = X.XXXX
