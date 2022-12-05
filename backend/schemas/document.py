def documentEntity(item) -> dict:
    return {
        "title": item["title"],
        "type": item["type"],
        "category": item["category"],
        "summary": item["summary"],
        "cover": item["cover"]
    }

def documentsEntity(entity) -> list:
    return [documentEntity(item) for item in entity]