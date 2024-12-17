import time
import datetime

current = time.time()
print(f"Seconds since January 1, 1970: {current:,.4f} or {current:.2e} in scientific notation")

today = datetime.date.today()
print(f"{today.strftime("%b %d %Y")}")