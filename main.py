from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
from RandomHistory import today

history = create_random_transactions(10000)
print(best_candidates(history,3,str(today)))