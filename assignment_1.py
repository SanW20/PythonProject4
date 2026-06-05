def clean_and_classify(messages):
    grant_keywords = ["grant","funding","deadline","scholarship"]
    report_keywords = ["report","file","send again","document"]
    general_keywords = ["how","what","can you","where","why"]
    cleaned = []

    for msg in messages:
        user_id = msg.get("user_id","").strip()
        text = msg.get("message","").strip()
        lower_text = text.lower()
        channel = msg.get("channel")
        if not user_id or not text:
            continue
        if any(word in lower_text for word in grant_keywords):
            category = "grant_search"
        elif any(word in lower_text for word in report_keywords):
            category = "report_request"
        elif any(word in lower_text for word in general_keywords):
            category = "general_question"
        else:
            category = "unknown"
        cleaned.append({"user_id":user_id, "channel":channel, "message":text, "category":category})

    return cleaned
messages = [
 {"user_id": "u1", "channel": "email", "message": "Hello, I want info about grants for education."},
 {"user_id": "u2", "channel": "whatsapp", "message": " "},
 {"user_id": "", "channel": "email", "message": "What is the deadline?"},
 {"user_id": "u3", "channel": "email", "message": "Please send the report again."},
 {"user_id": "u1", "channel": "whatsapp", "message": " Can you help me find funding? "},
 {"user_id": "u4", "channel": "telegram", "message": "Good morning!"},
 {"user_id": "u5", "channel": "email", "message": "Can you send me the scholarship document?"},
 {"user_id": "u6", "channel": "whatsapp", "message": ""},
]

print(clean_and_classify(messages))

