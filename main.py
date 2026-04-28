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
  
def main():
  try:
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth day (1-31): "))
    
    if month < 1 or month > 12 or day < 1 or day > 31:
      print("Invalid date")
      return
    
    sign = get_star_sign(day, month)
    
    if sign:
      print("Your star sign is {}!".format(sign))
    else:
      print("Invalid date")
      
  except ValueError:
    print("Please enter numbers only")
  
main()