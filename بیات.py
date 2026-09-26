from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>بیات | سایت من</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Tahoma,Arial,sans-serif;background:#070914;color:#f5f7ff;line-height:1.8}
nav{position:sticky;top:0;z-index:10;display:flex;justify-content:space-between;align-items:center;padding:18px 7%;background:rgba(7,9,20,.88);backdrop-filter:blur(14px);border-bottom:1px solid #202544}
.logo{font-size:25px;font-weight:bold;color:#8b7cff}
nav a{color:#dce1ff;text-decoration:none;margin-right:24px}
nav a:hover{color:#9b8cff}
.hero{min-height:88vh;display:flex;align-items:center;padding:70px 8%;background:radial-gradient(circle at 80% 25%,rgba(124,92,255,.25),transparent 35%),radial-gradient(circle at 15% 80%,rgba(45,120,255,.18),transparent 30%)}
.hero-content{max-width:760px}
.badge{display:inline-block;padding:7px 15px;border:1px solid #39336b;border-radius:999px;color:#a99cff;background:#11132a;margin-bottom:20px}
h1{font-size:clamp(42px,7vw,78px);line-height:1.15;margin-bottom:22px}
.gradient{background:linear-gradient(90deg,#8b7cff,#55a7ff);-webkit-background-clip:text;color:transparent}
.hero p{font-size:19px;color:#aeb5d6;max-width:650px;margin-bottom:30px}
.buttons{display:flex;gap:14px;flex-wrap:wrap}
.btn{display:inline-block;padding:13px 25px;border-radius:12px;text-decoration:none;font-weight:bold}
.primary{background:#7c5cff;color:white;box-shadow:0 10px 35px rgba(124,92,255,.25)}
.secondary{border:1px solid #303655;color:#e7eaff;background:#0e1120}
section{padding:90px 8%}
.title{text-align:center;font-size:38px;margin-bottom:12px}
.subtitle{text-align:center;color:#929abd;margin-bottom:45px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.card{background:linear-gradient(145deg,#101326,#0b0e1c);border:1px solid #202644;border-radius:18px;padding:28px;transition:.25s}
.card:hover{transform:translateY(-6px);border-color:#5749a8}
.icon{font-size:35px;margin-bottom:12px}
.card h3{margin-bottom:8px}
.card p{color:#969fbd}
.about{max-width:900px;margin:auto;text-align:center;color:#b0b7d2;font-size:18px}
.contact{max-width:700px;margin:auto}
input,textarea{width:100%;padding:15px;margin-bottom:15px;border:1px solid #252b49;border-radius:12px;background:#0c0f1d;color:white;outline:none}
input:focus,textarea:focus{border-color:#7661e8}
textarea{min-height:150px;resize:vertical}
button{width:100%;border:0;cursor:pointer;padding:15px;border-radius:12px;background:#7c5cff;color:white;font-size:16px;font-weight:bold}
.message{margin-bottom:18px;padding:12px;border-radius:10px;background:#151a31;color:#bfc7ff}
footer{text-align:center;padding:30px;border-top:1px solid #1d223c;color:#777f9e}
@media(max-width:700px){nav{padding:15px 5%}nav div:last-child{display:none}section{padding:65px 5%}.hero{padding:60px 5%}}
</style>
</head>
<body>
<nav><div class="logo">بیات</div><div><a href="#home">خانه</a><a href="#services">خدمات</a><a href="#about">درباره</a><a href="#contact">تماس</a></div></nav>
<header class="hero" id="home"><div class="hero-content"><span class="badge">به سایت من خوش آمدید</span><h1>یک سایت <span class="gradient">مدرن و حرفه‌ای</span></h1><p>این سایت با پایتون و Flask ساخته شده و برای معرفی، نمونه‌کار و ساخت یک وب‌سایت شخصی مدرن آماده است.</p><div class="buttons"><a class="btn primary" href="#services">مشاهده خدمات</a><a class="btn secondary" href="#contact">ارتباط با من</a></div></div></header>
<section id="services"><h2 class="title">خدمات</h2><p class="subtitle">چیزهایی که می‌توانی در این سایت معرفی کنی</p><div class="cards">
<div class="card"><div class="icon">💻</div><h3>طراحی سایت</h3><p>ساخت صفحات مدرن، سریع و واکنش‌گرا برای موبایل و کامپیوتر.</p></div>
<div class="card"><div class="icon">🚀</div><h3>پروژه‌های پایتون</h3><p>معرفی پروژه‌ها و برنامه‌هایی که با Python ساخته شده‌اند.</p></div>
<div class="card"><div class="icon">🎮</div><h3>ساخت بازی</h3><p>نمایش پروژه‌های بازی و برنامه‌های تعاملی.</p></div>
</div></section>
<section id="about"><h2 class="title">درباره من</h2><p class="subtitle">یک معرفی کوتاه</p><div class="about">این قسمت برای معرفی خودت، مهارت‌ها، پروژه‌ها و کارهایی که انجام می‌دهی طراحی شده است.</div></section>
<section id="contact"><h2 class="title">تماس با من</h2><p class="subtitle">پیامت را ارسال کن</p><div class="contact">{% if message %}<div class="message">{{ message }}</div>{% endif %}<form method="POST"><input type="text" name="name" placeholder="نام شما" required><input type="email" name="email" placeholder="ایمیل شما" required><textarea name="text" placeholder="پیام شما..." required></textarea><button type="submit">ارسال پیام</button></form></div></section>
<footer>© 2026 بیات — ساخته شده با Python + Flask</footer>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            message = f"ممنون {name}! پیام شما دریافت شد."
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
