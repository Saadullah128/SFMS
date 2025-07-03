# utils/quickbooks.py
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from django.conf import settings
from time import sleep
from quickbooks.objects import Invoice as QBInvoice
import os

class QuickBooksClient:
    def __init__(self):
        self.auth_client = AuthClient(
            client_id=os.getenv("QB_CLIENT_ID"),
            client_secret=os.getenv("QB_CLIENT_SECRET"),
            environment=os.getenv("QB_ENVIRONMENT"),
            redirect_uri=os.getenv("QB_REDIRECT_URI"),
        )  # Removed scopes from here
    
    def get_auth_url(self):
        """Generate authorization URL with scopes"""
        return self.auth_client.get_authorization_url(
            scopes=[Scopes.ACCOUNTING]  # Moved scopes to this method
        )
    
    def get_tokens(self, auth_code):
        """Exchange auth code for access/refresh tokens"""
        self.auth_client.get_bearer_token(auth_code)
        return {
            'access_token': self.auth_client.access_token,
            'refresh_token': self.auth_client.refresh_token,
            'realm_id': self.auth_client.realm_id
        }
    
    def refresh_token(self, refresh_token):
        """Refresh expired access token"""
        self.auth_client.refresh(refresh_token)
        return self.auth_client.access_token
    
    def sync_invoice(self, invoice, max_retries=3):
        for attempt in range(max_retries):
            try:
                qb_invoice = QBInvoice()
                # ... field mapping ...
                qb_invoice.save(qb=self.client)
                return qb_invoice.Id
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                sleep(2 ** attempt)