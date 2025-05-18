from bs4 import BeautifulSoup

def extract_tests(session, url):
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    tests = []
    for link in soup.select("a[href*='/test/']"):
        title = link.get_text(strip=True)
        href = "https://testbook.com" + link["href"]
        tests.append({"title": title, "url": href})
    return tests

def extract_questions(session, url):
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    questions = []
    for q in soup.select(".question"):
        question_text = q.select_one(".question-text").get_text(strip=True)
        options = [opt.get_text(strip=True) for opt in q.select(".option")]
        questions.append({"question": question_text, "options": options})
    return questions
