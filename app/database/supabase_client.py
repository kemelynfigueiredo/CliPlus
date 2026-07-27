from supabase import create_client, Client
from settings.config import SUPABASE_URL, SUPABASE_SERVICE_KEY
import os

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
	raise RuntimeError(
		"Supabase configuration is missing. Set SUPABASE_URL and SUPABASE_SERVICE_KEY in your environment or .env file."
	)

# Create supabase client using service key (prefer service-role key for server-side operations)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# Optional health check: do a lightweight request when running in development to surface config errors early
if os.getenv("FLASK_ENV") == "development":
	try:
		# attempt a simple request to validate credentials (non-intrusive)
		supabase.auth.get_user()
	except Exception:
		# avoid failing silently; raise a clearer message
		raise RuntimeError("Unable to reach Supabase with provided credentials. Check SUPABASE_URL and SUPABASE_SERVICE_KEY.")