from flask import Flask, render_template_string, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "cloud_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

billing_data = [
    {"service": "AWS EC2", "rate": 0.30},
    {"service": "AWS S3", "rate": 0.10},
    {"service": "Azure VM", "rate": 0.28},
    {"service": "GCP Compute", "rate": 0.25},
]

login_html = """
<!DOCTYPE html>
<html>
<head>
    <title>☁️ Login | Cloud Billing</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #74ABE2, #5563DE);
            font-family: 'Poppins', sans-serif;
            color: white;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        .loader {
            border: 8px solid #f3f3f3;
            border-top: 8px solid white;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .card {
            display: none;
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="loader"></div>
    <div class="card bg-light text-dark p-4 rounded shadow" style="width: 22rem;">
        <h4 class="mb-3 text-center">☁️ Cloud Billing Login</h4>
        {% if error %}
        <div class="alert alert-danger">{{ error }}</div>
        {% endif %}
        <form method="POST">
            <input type="text" name="username" class="form-control mb-2" placeholder="Username" required>
            <input type="password" name="password" class="form-control mb-3" placeholder="Password" required>
            <button type="submit" class="btn btn-primary w-100">Login</button>
        </form>
    </div>
    <script>
        setTimeout(() => {
            document.querySelector('.loader').style.display = 'none';
            document.querySelector('.card').style.display = 'block';
        }, 2000);
    </script>
</body>
</html>
"""

dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>☁️ Dashboard | Cloud Billing</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #e0ecff, #ffffff);
            font-family: 'Poppins', sans-serif;
        }
        .table-container {
            margin-top: 40px;
        }
        .total {
            font-size: 1.2rem;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark bg-primary px-4">
        <span class="navbar-brand mb-0 h1">☁️ Cloud Billing Dashboard</span>
        <form action="/logout" method="get">
            <button class="btn btn-light">Logout</button>
        </form>
    </nav>

    <div class="container table-container">
        <table class="table table-bordered table-hover">
            <thead class="table-primary">
                <tr>
                    <th>Service</th>
                    <th>Rate ($/hr)</th>
                    <th>Quantity</th>
                </tr>
            </thead>
            <tbody>
                {% for row in billing_data %}
                <tr>
                    <td>{{ row.service }}</td>
                    <td>{{ row.rate }}</td>
                    <td><input type="number" min="0" value="0" class="form-control" onchange="updateTotal()"></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <div class="total text-center">Total Cost: $<span id="total">0.00</span></div>
    </div>

    <script>
        const rates = {{ billing_data | tojson }};
        function updateTotal() {
            let total = 0;
            const inputs = document.querySelectorAll("input[type='number']");
            inputs.forEach((input, i) => {
                const qty = parseFloat(input.value) || 0;
                total += qty * rates[i].rate;
            });
            document.getElementById("total").innerText = total.toFixed(2);
        }
    </script>
</body>
</html>
"""

logout_html = """
<!DOCTYPE html>
<html>
<head>
    <title>☁️ Goodbye</title>
    <style>
        body {
            background: linear-gradient(135deg, #74ABE2, #5563DE);
            font-family: 'Poppins', sans-serif;
            color: white;
            height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .cloud {
            font-size: 2rem;
            background: white;
            color: #5563DE;
            padding: 30px;
            border-radius: 50px;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
            animation: float 3s ease-in-out infinite;
            margin-bottom: 20px;
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        iframe {
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <div class="cloud">☁️ Thanks for using my Cloud Billing Dashboard!</div>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/bbJUcwvKCsA?autoplay=1&loop=1&playlist=bbJUcwvKCsA&mute=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if user == "admin" and password == "cloud123":
            session.permanent = True
            session["user"] = user
            return redirect(url_for("dashboard"))
        return render_template_string(login_html, error="Invalid credentials")
    return render_template_string(login_html)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template_string(dashboard_html, billing_data=billing_data)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return render_template_string(logout_html)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
