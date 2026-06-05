def clean_and_classify(messages):
    grants_words = ["grant","funding","deadline","scholarship"]
    reportr_words = ["report","file","send again","document"]
    generalq_words = ["how","what","can you","where","why"]
    cleaned = []

    for i in messages:
        user_id = i.get("user_id").strip()
        text = i.get("message").lower().strip()
        channel = i.get("channel")
        if not user_id or not text:
            continue
        if any(j in text for j in grants_words):
            category = "grant_search"
        elif any(j in text for j in reportr_words):
            category = "report_request"
        elif any(j in text for j in generalq_words):
            category = "general_questions"
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

