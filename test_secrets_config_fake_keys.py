#!/usr/bin/env python3
"""
TEST FILE - FAKE CREDENTIALS FOR SECRET SCANNING VALIDATION
============================================================
This file contains FAKE/TEST credentials to validate that 
secret scanning is working properly. These are NOT real credentials.

DO NOT USE THESE VALUES - THEY ARE FOR TESTING ONLY
"""

# =============================================================================
# FAKE AWS CREDENTIALS (Test Values - Not Real)
# =============================================================================
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_SESSION_TOKEN = "FwoGZXIvYXdzEBYaDKLAzLHk3EXAMPLETOKEN1234567890abcdefghijklmnop"

# =============================================================================
# FAKE GCP SERVICE ACCOUNT (Test Values - Not Real)
# =============================================================================
GCP_SERVICE_ACCOUNT = {
    "type": "service_account",
    "project_id": "fake-project-123456",
    "private_key_id": "1234567890abcdef1234567890abcdef12345678",
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy0AHB7MmE8EXAMPLE\nFAKEKEYDATAFORTESTINGONLYNOTREALPRIVATEKEYDATA1234567890\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n-----END RSA PRIVATE KEY-----\n",
    "client_email": "fake-service-account@fake-project-123456.iam.gserviceaccount.com",
    "client_id": "123456789012345678901",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
}

# =============================================================================
# FAKE AZURE CREDENTIALS (Test Values - Not Real)
# =============================================================================
AZURE_CLIENT_ID = "12345678-1234-1234-1234-123456789012"
AZURE_CLIENT_SECRET = "FAKE~Secret~Value~For~Testing~Only~1234567890"
AZURE_TENANT_ID = "87654321-4321-4321-4321-210987654321"
AZURE_SUBSCRIPTION_ID = "abcdef12-3456-7890-abcd-ef1234567890"

# =============================================================================
# FAKE DATABASE CREDENTIALS (Test Values - Not Real)
# =============================================================================
DATABASE_URL = "postgresql://admin:SuperSecretPassword123!@db.example.com:5432/production_db"
MYSQL_PASSWORD = "MySQLTestPassword456!"
MONGODB_URI = "mongodb://root:MongoDBRootPass789@mongodb.example.com:27017/admin"
REDIS_PASSWORD = "RedisTestPassword012"

# =============================================================================
# FAKE API KEYS (Test Values - Not Real)
# =============================================================================
STRIPE_SECRET_KEY = "sk_live_FAKE1234567890abcdefghijklmnopqrstuvwxyz"
STRIPE_PUBLISHABLE_KEY = "pk_live_FAKE0987654321zyxwvutsrqponmlkjihgfedcba"
SENDGRID_API_KEY = "SG.FAKE1234567890.abcdefghijklmnopqrstuvwxyz1234567890ABCD"
TWILIO_AUTH_TOKEN = "FAKE1234567890abcdef1234567890ab"
SLACK_BOT_TOKEN = "xoxb-FAKE-1234567890123-1234567890123-abcdefghijklmnopqrstuvwx"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/TFAKE1234/BFAKE5678/FAKEWebhookToken1234567890"
GITHUB_TOKEN = "ghp_FAKE1234567890abcdefghijklmnopqrstuv"
GITLAB_TOKEN = "glpat-FAKE1234567890abcdefgh"

# =============================================================================
# FAKE SSH/RSA KEYS (Test Values - Not Real)
# =============================================================================
SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEAtFAKE1234567890EXAMPLEKEYDATA1234567890abcdefghijk
NOTAREALPRIVATEKEYFORTESTINGPURPOSESONLY1234567890ABCDEFGHIJKLMN
-----END OPENSSH PRIVATE KEY-----"""

RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy0AHB7MmE8FAKEKEY123
4567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123
THISISFAKEKEYDATAFORTESTINGSECRETSCANNING1234567890NOTREAL
-----END RSA PRIVATE KEY-----"""

# =============================================================================
# FAKE JWT/AUTH TOKENS (Test Values - Not Real)
# =============================================================================
JWT_SECRET = "super-secret-jwt-signing-key-for-testing-only-1234567890"
AUTH0_CLIENT_SECRET = "FAKE-Auth0-Client-Secret-1234567890-abcdefghijklmnop"
OAUTH_CLIENT_SECRET = "FAKE_OAUTH_SECRET_1234567890_abcdefghijklmnopqrstuvwxyz"

# =============================================================================
# FAKE ENCRYPTION KEYS (Test Values - Not Real)
# =============================================================================
ENCRYPTION_KEY = "FAKE1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF12345678"
AES_256_KEY = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
HMAC_SECRET = "FAKEHMACSecretKeyForTestingOnly1234567890abcdefghijklmnop"

# =============================================================================
# FAKE WEBHOOK SECRETS (Test Values - Not Real)
# =============================================================================
GITHUB_WEBHOOK_SECRET = "FAKEGitHubWebhookSecret1234567890"
STRIPE_WEBHOOK_SECRET = "whsec_FAKE1234567890abcdefghijklmnopqrstuvwxyz"

# =============================================================================
# FAKE .ENV FILE CONTENTS (Test Values - Not Real)
# =============================================================================
"""
# Example .env file content (FAKE VALUES)
DB_PASSWORD=FakeDBPassword123!
API_SECRET=FakeAPISecret456!
ADMIN_PASSWORD=FakeAdminPass789!
SECRET_KEY=django-insecure-FAKE1234567890abcdefghijklmnopqrstuvwxyz
"""

print("WARNING: This file contains FAKE test credentials for security scanning validation!")
print("DO NOT use any of these values in production systems.")
