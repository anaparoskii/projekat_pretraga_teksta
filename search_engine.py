from color import Color


def rank(result):
    ranked_pages = {}
    for page in result:
        if isinstance(page, int):
            if page in list(ranked_pages.keys()):
                ranked_pages[page] += 1
            else:
                ranked_pages[page] = 1
        else:
            for i in page:
                if i in list(ranked_pages.keys()):
                    ranked_pages[i] += 1
                else:
                    ranked_pages[i] = 1
    return ranked_pages


def search_result(result):
    ranked_pages = rank(result)
    sorted_pages = sorted(ranked_pages.items(), key=lambda x: x[1], reverse=True)
    return sorted_pages


def get_paragraph(page, words, code):
    if code == 1:
        paragraph = page.split('\n')
        paragraph_value = ''
        search_range = len(paragraph) // 2
        for word in words:
            for i in range(search_range, len(paragraph)):
                if word.lower() in paragraph[i].lower():
                    if paragraph_value == '':
                        paragraph_value = paragraph[i]
                    elif paragraph_value == paragraph[i]:
                        continue
                    else:
                        paragraph_value = paragraph_value + '\n' + paragraph[i]
                        break
        for word in words:
            if paragraph_value != '':
                paragraph_value = paragraph_value.replace(word, f"{Color.PURPLE}{word}{Color.RESET}")
        return paragraph_value
    else:
        paragraph = page.split('\n')
        paragraph_value = ''
        search_range = len(paragraph) // 2
        for i in range(search_range, len(paragraph)):
            if words in paragraph[i]:
                if paragraph_value == '':
                    paragraph_value = paragraph[i]
                elif paragraph_value == paragraph[i]:
                    continue
                else:
                    paragraph_value = paragraph_value + '\n' + paragraph[i]
                    break
        if paragraph_value != '':
            paragraph_value = paragraph_value.replace(words, f"{Color.PURPLE}{words}{Color.RESET}")
        return paragraph_value
