"""Example usage for CX Sentiment Resolution Matcher."""
from client import CXSentimentResolutionMatcher

if __name__ == "__main__":
    msg = "I was charged twice on my invoice this morning. Please refund immediately!"
    res = CXSentimentResolutionMatcher.match_ticket(msg)
    print("Detected Category:", res["detected_category"])
    print("Urgency:", res["urgency_level"])
    print("Playbook:", res["resolution_playbook"])
