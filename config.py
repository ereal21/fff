
import os
from dotenv import load_dotenv

# Load .env files
load_dotenv()
load_dotenv("steps.env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "Inereal").lstrip("@")
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "EUR")
DB_PATH = os.getenv("DB_PATH", "bot.db")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# NowPayments configuration
NOWPAYMENTS_API_KEY = os.getenv("NOWPAYMENTS_API_KEY", "").strip()
NOWPAYMENTS_IPN_URL = os.getenv("NOWPAYMENTS_IPN_URL", "").strip()
NOWPAYMENTS_API_URL = os.getenv("NOWPAYMENTS_API_URL", "https://api.nowpayments.io/v1").rstrip("/")

# Setup step media files (images or videos)
STEP1_IMAGE = os.getenv("STEP1_IMAGE", "").strip()
STEP2_IMAGE = os.getenv("STEP2_IMAGE", "").strip()
STEP3_IMAGE = os.getenv("STEP3_IMAGE", "").strip()
STEP4_IMAGE = os.getenv("STEP4_IMAGE", "").strip()
STEP5_IMAGE = os.getenv("STEP5_IMAGE", "").strip()
STEP6_IMAGE = os.getenv("STEP6_IMAGE", "").strip()
STEP7_IMAGE = os.getenv("STEP7_IMAGE", "").strip()

# Package prices in DEFAULT_CURRENCY
PACKAGES = {
    "template": 299,
    "full": 999,
}

# Discounted price for upgrading from template to full package
UPGRADE_FULL_PRICE = 699

# RDP package prices in DEFAULT_CURRENCY
RDP_PACKAGES = {
    "rdp1": 10,
    "rdp2": 20,
    "rdp3": 30,
}

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Put it in your .env file.")
