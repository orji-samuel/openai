from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Example data (later replace with database queries)
    data = {
        "total_policies": 1245,
        "total_clients": 560,
        "expiring_documents": 18,
        "pending_claims": 12,
        "storage_used": 124,   # GB
        "storage_total": 500,  # GB
        "compliance_rate": 92  # percentage
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)