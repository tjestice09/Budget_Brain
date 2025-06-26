import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.reply_logic import generate_reply

def test_groceries():
    result = generate_reply("How much did I spend on groceries?")
    assert "groceries" in result.lower()

def test_spend():
    result = generate_reply("How much did I spend?")
    assert "spent $150" in result

def test_random():
    result = generate_reply("What am I doing here?")
    assert "didn't understand" in result