import logging

def clean_data(data):
    " clean and transform the data"

    if not data:
        logging.error("No data provided for cleaning.")
        return None
    
    cleaned = []
    for doc in data.get("docs", []): #.get("docs", []) If "docs" is not present in data, it returns an empty list ([]) by default. safe access method that ensures you always get a list (or at least avoid an error) when "docs" might be missing from the data.
        title = doc.get("title")
        if title:
            "normalize the title if needed"
            cleaned.append({"title": title.strip()}) #.strip() removes any leading, and trailing whitespaces.
    logging.info("Data cleaned successfully. %d records processed.", len(cleaned))
    return cleaned

if __name__ == "__main__":
    from data_ingestion import fetch_data
    import json
    raw_data = fetch_data()
    cleaned = clean_data(raw_data)
    print(json.dumps(cleaned, indent=2)) #json.dumps() function will convert a subset of Python objects (like a dict) into a json formatted string.