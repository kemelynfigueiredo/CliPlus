from app.database.supabase_client import supabase

response = supabase.auth.sign_in_with_password({
    "email": "recepcao@cliplus.com",
    "password": "senha123"
})

print(response.session.access_token)