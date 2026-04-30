from flask import Flask, render_template, request

app = Flask(__name__)

def get_star_sign(day, month):
  signs = [
    ("Capricorn", (22, 12), (19, 1)),
    ("Aquarius", (20, 1), (18, 2)),
    ("Pisces", (19, 2), (20, 3)),
    ("Aries", (21, 3), (19, 4)),
    ("Taurus", (20, 4), (20, 5)),
    ("Gemini", (21, 5), (20, 6)),
    ("Cancer", (21, 6), (22, 7)),
    ("Leo", (23, 7), (22, 8)),
    ("Virgo", (23, 8), (22, 9)),
    ("Libra", (23, 9), (22, 10)),
    ("Scorpio", (23, 10), (21, 11)),
    ("Sagittarius", (22, 11), (21, 12))
  ]
  
  for sign, (start_day, start_month), (end_day, end_month) in signs:
    if(month == start_month and day >= start_day) or \
      (month == end_month and day <= end_day):
      return sign
      
  return None
  
@app.route("/", methods=["GET", "POST"])
def home():
  sign = None

  if request.method == "POST":
    month = int(request.form["month"])
    day = int(request.form["day"])
    sign = get_star_sign(day, month)

  return render_template("index.html", sign=sign)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
