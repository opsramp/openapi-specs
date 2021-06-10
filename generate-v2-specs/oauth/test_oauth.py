import os, sys
sys.path.append("..")
from oas_common_models import *
from models import *
from oauth import app

client = TestClient(app)

def test_post_client_credentials():
    response = client.post(
        "/auth/oauth/token",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        },
        json={
            "grant_type": "client_credentials",
            "client_id": "jzhyhYKGkpEWAXcJ9Qd6mMkpSDMFqYUS",
            "client_secret": "PCDNBBMx77RfdG3fCUsMnFvsEMu8y86BaN82JRpjqgBDqHbm8Hcxgj4ZKZg9gp88"
        }
    )

    assert response.status_code == 200
    utils.print_dict(response.json())

    return

