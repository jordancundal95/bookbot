def count_words(text: str) -> int:                          # function that counts the amount of words within a given text
    return len(text.split())                                # .split() seperates the words, using len(text.split()) gives the number of words

def count_characters(text: str) -> dict[str, int]:          # function that counts the amount of characters within a given text, returns them as key value pairs in a dict
    counts: dict[str, int] = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def character_report_items(char_counts: dict[str, int]) -> list[dict]:
    items: list[dict] = []
    for ch, n in char_counts.items():
        if ch.isalpha():
            items.append({"char": ch, "num": n})
    items.sort(key=sort_on, reverse=True)
    return items