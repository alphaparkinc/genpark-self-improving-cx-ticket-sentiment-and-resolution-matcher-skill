"""MCP server for CX Sentiment Resolution Matcher."""
import sys
import json
from client import CXSentimentResolutionMatcher

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "match_support_ticket",
                "description": "Matches support ticket to appropriate resolution playbook and SLA",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticket_text": {"type": "string"}
                    },
                    "required": ["ticket_text"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "match_support_ticket":
            txt = params.get("arguments", {}).get("ticket_text", "")
            res = CXSentimentResolutionMatcher.match_ticket(txt)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
