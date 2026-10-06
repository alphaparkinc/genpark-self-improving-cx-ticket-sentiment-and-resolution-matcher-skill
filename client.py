"""Self-Improving CX Ticket Sentiment & Resolution Matcher.
100% Python Standard Library.
"""

class CXSentimentResolutionMatcher:
    """Analyzes customer ticket emotional urgency, maps matching resolution playbooks, and templates responses."""
    
    PLAYBOOKS = {
        "billing_dispute": {
            "urgency": "HIGH",
            "playbook": "Immediate refund verification and credit balance ledger adjustment.",
            "sla_hours": 2
        },
        "service_outage": {
            "urgency": "CRITICAL",
            "playbook": "Check status page incidents, escalate to on-call engineer, reply with incident tracker.",
            "sla_hours": 1
        },
        "feature_request": {
            "urgency": "LOW",
            "playbook": "Log feedback in Product Roadmap board and send acknowledgement email.",
            "sla_hours": 24
        }
    }
    
    @classmethod
    def match_ticket(cls, ticket_text: str) -> dict:
        text_lower = ticket_text.lower()
        matched_cat = "feature_request"
        
        if any(kw in text_lower for kw in ["charged twice", "refund", "billing", "invoice incorrect", "overcharged"]):
            matched_cat = "billing_dispute"
        elif any(kw in text_lower for kw in ["down", "500 error", "crash", "outage", "broken", "offline"]):
            matched_cat = "service_outage"
            
        playbook_info = cls.PLAYBOOKS[matched_cat]
        sentiment = "ANGRY" if "frustrated" in text_lower or "unacceptable" in text_lower or "immediately" in text_lower else "NEUTRAL"
        
        return {
            "detected_category": matched_cat,
            "sentiment": sentiment,
            "urgency_level": playbook_info["urgency"],
            "resolution_playbook": playbook_info["playbook"],
            "sla_target_hours": playbook_info["sla_hours"]
        }
