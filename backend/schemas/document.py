def documentEntity(item) -> dict:
    return {
        "name": item["name"],
        "type": item["type"],
        "category": item["category"],
        "stock": item["stock"]
    }

def documentsEntity(entity) -> list:
    return [documentEntity(item) for item in entity]