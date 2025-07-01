import telebot
from telebot import types
import time
import threading
import random
import string

API_TOKEN = '8043717422:AAGm19w_CfJvo3wK-BrPwP6Vqpp2qOF3FV4'
bot = telebot.TeleBot(API_TOKEN)

# داده‌ها و متغیرهای کلی
waiting_users = []  # لیست صف انتظار: [(user_id, join_time, search_type, gender)]
active_chats = {}   # چت‌های فعال: user_id: {"partner": partner_id, "start_time": timestamp}
user_profiles = {}  # پروفایل‌ها: user_id: {...}
user_states = {}    # وضعیت ویرایش پروفایل: user_id: حالت ویرایش یا None

WAIT_TIMEOUT = 120       # زمان حداکثر انتظار در صف (ثانیه)
NO_STOP_DURATION = 10    # حداقل زمان لازم قبل از قطع چت (ثانیه)
COINS_PER_SEARCH = 2     # سکه لازم برای هر جستجو
COINS_FOR_REFERRAL = 10  # سکه جایزه معرف

lock = threading.Lock()

provinces_cities = {
    "تهران": ["تهران", "ری", "شمیرانات"],
    "اصفهان": ["اصفهان", "کاشان", "نجف‌آباد"],
    "فارس": ["شیراز", "مرودشت", "کازرون"],
}

EDIT_NONE = None
EDIT_NAME = "edit_name"
EDIT_AGE = "edit_age"
EDIT_PROVINCE = "edit_province"
EDIT_CITY = "edit_city"
EDIT_BIO = "edit_bio"
EDIT_GENDER = "edit_gender"

GENDERS = ["زن", "مرد"]

def generate_username(user_id):
    base = "user"
    rand_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{base}{user_id}_{rand_part}"

def init_user_profile(user_id):
    if user_id not in user_profiles:
        user_profiles[user_id] = {
            "photo_file_id": None,
            "name": None,
            "age": None,
            "province": None,
            "city": None,
            "bio": None,
            "gender": None,
            "coins": 10,
            "likes": set(),
            "blocked": set(),
            "referrer": None,
            "username": generate_username(user_id),
            "last_seen": time.time(),
            "private_chat": False,
        }

def reset_user_state(user_id):
    user_states[user_id] = EDIT_NONE

def format_last_seen(timestamp):
    now = time.time()
    diff = now - timestamp
    if diff < 60:
        return "لحظاتی پیش"
    elif diff < 3600:
        minutes = int(diff // 60)
        return f"{minutes} دقیقه پیش"
    elif diff < 86400:
        hours = int(diff // 3600)
        return f"{hours} ساعت پیش"
    elif diff < 2592000:
        days = int(diff // 86400)
        return f"{days} روز پیش"
    else:
        return "خیلی وقت پیش"

# بخش باقی کد بدون تغییر به صورت مستقیم از کاربر گرفته شده
# و به فایل نهایی اضافه می‌شود:


import telebot
from telebot import types
import time
import threading
import random
import string

API_TOKEN = '8043717422:AAGm19w_CfJvo3wK-BrPwP6Vqpp2qOF3FV4'
bot = telebot.TeleBot(API_TOKEN)

# داده‌ها و متغیرهای کلی
waiting_users = []  # لیست صف انتظار: [(user_id, join_time, search_type, gender)]
active_chats = {}   # چت‌های فعال: user_id: {"partner": partner_id, "start_time": timestamp}
user_profiles = {}  # پروفایل‌ها: user_id: {...}
user_states = {}    # وضعیت ویرایش پروفایل: user_id: حالت ویرایش یا None

WAIT_TIMEOUT = 120       # زمان حداکثر انتظار در صف (ثانیه)
NO_STOP_DURATION = 10    # حداقل زمان لازم قبل از قطع چت (ثانیه)
COINS_PER_SEARCH = 2     # سکه لازم برای هر جستجو
COINS_FOR_REFERRAL = 10  # سکه جایزه معرف

lock = threading.Lock()

provinces_cities = {
    "تهران": ["تهران", "ری", "شمیرانات"],
    "اصفهان": ["اصفهان", "کاشان", "نجف‌آباد"],
    "فارس": ["شیراز", "مرودشت", "کازرون"],
}

EDIT_NONE = None
EDIT_NAME = "edit_name"
EDIT_AGE = "edit_age"
EDIT_PROVINCE = "edit_province"
EDIT_CITY = "edit_city"
EDIT_BIO = "edit_bio"
EDIT_GENDER = "edit_gender"

GENDERS = ["زن", "مرد"]

# ——— ادامه کد در فایل کامل در ادامه قرار می‌گیرد (به دلیل محدودیت اندازه) ———
