from TransitionMatrix import key
from datetime import datetime
import pytz

today = datetime.now(pytz.timezone('America/Chicago'))

def create_random_transactions(int):
    transactions = []
    for i in range(int):
            temp_trans = []
            temp_trans.append("USER")
            temp_trans.append(f"TXN{i+1}")