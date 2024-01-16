import pymongo
import os
from helpers.date import add_date
DB_NAME = os.environ.get("DB_NAME", "")
DB_URL = os.environ.get("DB_URL", "")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]
premium_users_col = db["premium_users"]

# ... (other imports and functions)

def premium_function_usage(chat_id, interval):
    user = find_one(chat_id)

    if user and user["usertype"] == "Premium":
        current_date = add_date()[0]
        last_usage_date_key = f"last_usage_date_{interval}"
        usage_count_key = f"usage_count_{interval}"

        if last_usage_date_key not in user:
            # If it's the first time using the function for this interval, initialize the fields
            update_data = {usage_count_key: 1, last_usage_date_key: current_date}
        else:
            last_usage_date = user[last_usage_date_key]

            if (current_date - last_usage_date).days < get_interval_days(interval) and user[usage_count_key] < get_interval_limit(interval):
                # If within the specified interval and usage count is less than the limit, allow the function
                update_data = {usage_count_key: user[usage_count_key] + 1, last_usage_date_key: current_date}
            else:
                return f"Premium function usage limit for {interval} reached. Wait for the next interval."

        update_user_data({"_id": chat_id}, update_data)
        return f"Premium function for {interval} executed successfully."
    else:
        return "You need a premium account to use this function."

def get_interval_days(interval):
    if interval == "weekly":
        return 7
    elif interval == "monthly":
        return 30  # Adjust as needed
    elif interval == "yearly":
        return 365  # Adjust as needed
    else:
        return 0

def get_interval_limit(interval):
    if interval == "weekly":
        return 4
    elif interval == "monthly":
        return 10  # Adjust as needed
    elif interval == "yearly":
        return 50  # Adjust as needed
    else:
        return 0
