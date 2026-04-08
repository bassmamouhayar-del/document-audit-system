from flask import Flask, render_template, request
from utils.extractor import extract_text, extract_data
from utils.comparator import compare_docs
from utils.rules import apply_rules

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ref_file = request.files["reference"]
        docs = request.files.getlist("documents")

        ref_text = extract_text(ref_file)
        ref_data = extract_data(ref_text)

        results = []

        for doc in docs:
            text = extract_text(doc)
            data = extract_data(text)

            errors = compare_docs(ref_data, data)
            rules = apply_rules(data)

            results.append({
                "name": doc.filename,
                "errors": errors + rules
            })

        return render_template("dashboard.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
