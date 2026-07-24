def get_user_info(user_id: int):

    if user_id == 1:
        return {
            "plan": "Premium",
            "status": "Active",
            "previous_tickets": 2
        }

    elif user_id == 2:
        return {
            "plan": "Free",
            "status": "Active",
            "previous_tickets": 5
        }

    else:
        return {
            "plan": "Free",
            "status": "Suspended",
            "previous_tickets": 0
        }


def search_bug_database(issue:str):

    if "crash" in issue.lower():
        return {
            "bug_found": True,
            "severity": "High",
            "solution": "Restart the application"
        }

    return {
        "bug_found": False
    }


def create_ticket(priority:str):

    return f"Ticket created successfully with {priority} priority."
