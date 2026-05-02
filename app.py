from flask import Flask, request

app = Flask(__name__)

# بيانات الموقع (هنا بنخزن النص واللون)
data = {
    "text": "أهلاً بيك في موقعي 👋",
    "color": "#000000"
}

# الصفحة الرئيسية
@app.route("/", methods=["GET", "POST"])
def home():

    global data

    # لو المستخدم بعت بيانات (تعديل)
    if request.method == "POST":
        text = request.form.get("text")
        color = request.form.get("color")

        if text:
            data["text"] = text
        if color:
            data["color"] = color

    # صفحة HTML داخل بايثون
    return f"""
    <html>
    <head>
        <title>لوحة التحكم</title>
    </head>

    <body style="text-align:center; font-family:Arial; margin-top:50px;">

        <h1>🔧 لوحة تحكم بالموقع</h1>

        <form method="POST">
            <input name="text" placeholder="اكتب النص" style="padding:10px;"><br><br>

            <input type="color" name="color" value="{data['color']}"><br><br>

            <button type="submit" style="padding:10px;">تحديث</button>
        </form>

        <hr>

        <h2 style="color:{data['color']}; font-size:30px;">
            {data['text']}
        </h2>

    </body>
    </html>
    """

# تشغيل السيرفر
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)