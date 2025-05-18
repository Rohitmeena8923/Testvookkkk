def generate_test_html(questions):
    html = '<b>Test Questions:</b>\n'
    for i, q in enumerate(questions):
        html += f"\n<b>Q{i+1}:</b> {q['question']}\n"
        for opt in q['options']:
            html += f"- {opt}\n"
    html += "\n<a href='https://your-flask-app-url/submit'>Submit</a>"
    return html
