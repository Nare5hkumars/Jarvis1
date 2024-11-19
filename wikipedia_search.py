import wikipedia

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found"
    except Exception as e:
        print(f"Error in search_wikipedia function: {e}")
        return "Error retrieving Wikipedia data"

if __name__ == "__main__":
    query = "Albert Einstein"
    results = search_wikipedia(query)
    print(results)
