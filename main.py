from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
from RandomHistory import today
from Pricing import avg_purchase

history = create_random_transactions(5)
print(history)
print(best_candidates(history,3,str(today)))
print(avg_purchase(history))