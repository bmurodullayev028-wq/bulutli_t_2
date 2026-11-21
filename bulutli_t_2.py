from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

HTML_SHABLON = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2-mustaqil ish — Docker & CI/CD</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, sans-serif; }
        body {
            background: linear-gradient(135deg, #090d16, #172033, #0f172a);
            color: #f8fafc;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 24px;
        }
        .card {
            background: rgba(23, 32, 51, 0.94);
            border: 1px solid #334155;
            border-radius: 18px;
            padding: 36px;
            max-width: 720px;
            width: 100%;
            box-shadow: 0 24px 50px rgba(0, 0, 0, 0.55);
        }
        .badge {
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid #0284c7;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 18px;
        }
        .title {
            font-size: 20px;
            color: #cbd5e1;
            line-height: 1.5;
            margin-bottom: 16px;
        }
        .big {
            font-size: 28px;
            font-weight: 800;
            color: #34d399;
            white-space: nowrap;
        }
        .info {
            margin-top: 18px;
            padding: 16px;
            background: #0b1120;
            border-radius: 12px;
            border: 1px solid #1e293b;
            font-size: 14px;
            color: #94a3b8;
            line-height: 1.7;
        }
        code { color: #38bdf8; }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">● Konteyner muhiti: {{ muhit }}</div>
        <h1 class="title">
            Murodullayev Bekzodning bulutli texnologiyalar fanidan <span class="big">2-mustaqil ishi</span>
        </h1>
        <div class="info">
            <div><strong>Texnologiya:</strong> Docker + GitHub Actions (CI/CD)</div>
            <div><strong>Versiya:</strong> <code>{{ versiya }}</code></div>
            <div><strong>Maqsad:</strong> Istalgan muhitda bir xil ishlash va avtomatik deploy</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    muhit = os.environ.get("RUN_ENV", "Docker / Lokal muhit")
    versiya = os.environ.get("APP_VERSION", "v1.0-auto")
    return render_template_string(HTML_SHABLON, muhit=muhit, versiya=versiya)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "cicd-docker-app"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)