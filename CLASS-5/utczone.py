import pytz
import datetime

# Define timezone for Dhaka
Dhaka = pytz.timezone('Asia/Dhaka')

# Get current time in Dhaka
dhaka_time = datetime.datetime.now(Dhaka)

# Print the timezone object
print("Timezone Object:", Dhaka)

# Print the current time in Dhaka
print("Current Time in Dhaka:", dhaka_time.strftime("%Y-%m-%d %H:%M:%S %p"))  # Formatted output
