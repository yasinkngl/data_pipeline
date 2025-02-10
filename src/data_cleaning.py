import logging

def clean_data(data):
    " clean and transform the data"

    if not data:
        logging.error("No data provided for cleaning.")
        return None
    
    cleaned = []
    for doc in data.get("docs", []):
        title = doc.get("title")
        if title:
            "normalize the title if needed"
            cleaned.append({"title": title.strip()})
    logging.info("Data cleaned successfully. %d records processed.", len(cleaned))
    return cleaned

if __name__ == "__main__":
    from src.data_ingestion import fetch_data
    import json
    raw_data = fetch_data()
    cleaned = clean_data(raw_data)
    print(json.dumps(cleaned, indent=2))