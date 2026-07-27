import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
# Support multiple common env names: prefer explicit SUPABASE_SERVICE_KEY but fall back
# to SUPABASE_SECRET_KEY or SUPABASE_SERVICE_ROLE_KEY if present (many projects name it differently).
SUPABASE_SERVICE_KEY = (
	os.getenv("SUPABASE_SERVICE_KEY")
	or os.getenv("SUPABASE_SECRET_KEY")
	or os.getenv("SUPABASE_SERVICE_ROLE_KEY")
)

MAIL_EMAIL  = os.getenv("MAIL_EMAIL")
MAIL_SENHA  = os.getenv("MAIL_SENHA")