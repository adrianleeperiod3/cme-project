from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates

history = create_random_transactions(1000)
print(best_candidates(history,8,"2022-11-12"))