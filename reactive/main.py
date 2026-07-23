def handle_ticket_reactive(ticket: dict) -> str:
    user_tier = ticket.get("user_tier", "").upper()
    error_type = ticket.get("error_type", "").upper()

    if not user_tier or not error_type:
        return "ACTION: INVALID_TICKET"

    if user_tier == "VIP":
        return "ACTION: ESCALATE_TO_MANAGEMENT"

    elif error_type == "DB_CRASH":
        return "ACTION: RESTART_DATABASE"

    else:
        return "ACTION: ADD_TO_STANDARD_QUEUE"
    
if __name__ == "__main__":
    print(" Reactive agent experience===")
    
    ticket1 = { "error_type": "DB_CRASH"}
    print(f"Test 1 (Standard DB Crash): {handle_ticket_reactive(ticket1)}")
    
    ticket2 = {"user_tier": "VIP", "error_type": "FEATURE_REQUEST"}
    print(f"Test 2 (Vip Request): {handle_ticket_reactive(ticket2)}")
    
    # (Edge Case) 
    ticket3 = {"user_tier": "VIP", "error_type": "DB_CRASH"}
    print(f"(Vip Request){handle_ticket_reactive(ticket3)}")
    
