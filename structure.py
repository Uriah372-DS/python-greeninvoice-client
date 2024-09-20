API_ENDPOINTS = {
    "account": {
        "token": ("/account/token", "POST"),  # no auth
        "password": ("/account/password", "POST"),
    },
    "businesses": {
        "get_all": ("/businesses", "GET"),
        "update": ("/businesses", "PUT"),
        "current": ("/businesses/me", "GET"),
        "get": ("/businesses/{business_id}", "GET"),
        "upload": ("/businesses/file", "POST"),
        "delete": ("/businesses/file", "DELETE"),
        "numbering": {
            "get": ("/businesses/numbering", "GET"),
            "modify": ("/businesses/numbering", "PUT"),
        },
        "footer": ("/businesses/footer", "GET"),
        "types": ("/businesses/types?lang={lang}", "GET"),  # no auth
    },
    "clients": {
        "add": ("/clients", "POST"),
        "{client_id}": {
            "get": ("/clients/{client_id}", "GET"),
            "update": ("/clients/{client_id}", "PUT"),
            "delete": ("/clients/{client_id}", "DELETE"),
            "associate": ("/clients/{client_id}/assoc", "POST"),
            "merge": ("/clients/{client_id}/merge", "POST"),
            "balance": ("/clients/{client_id}/balance", "POST"),
        },
        "search": ("/clients/search", "POST"),
    },
    "suppliers": {
        "add": ("/suppliers", "POST"),
        "{supplier_id}": {
            "get": ("/suppliers/{supplier_id}", "GET"),
            "update": ("/suppliers/{supplier_id}", "PUT"),
            "delete": ("/suppliers/{supplier_id}", "DELETE"),
            "merge": ("/suppliers/{supplier_id}/merge", "POST"),
        },
        "search": ("/suppliers/search", "POST"),
    },
    "items": {
        "add": ("/items", "POST"),
        "{item_id}": {
            "get": ("/items/{item_id}", "GET"),
            "update": ("/items/{item_id}", "PUT"),
            "delete": ("/items/{item_id}", "DELETE"),
        },
        "search": ("/items/search", "POST"),
    },
    "documents": {
        "add": ("/documents", "POST"),
        "preview": ("/documents/preview", "POST"),
        "{document_id}": {
            "get": ("/documents/{document_id}", "GET"),
            "close": ("/documents/{document_id}/close", "POST"),
            "open": ("/documents/{document_id}/open", "POST"),
            "linked": ("/documents/{document_id}/linked", "GET"),
            "download_links": ("/documents/{document_id}/download/links", "GET"),
        },
        "search": {
            "documents": ("/documents/search", "POST"),
            "payments": ("/documents/payments/search", "POST"),
        },
        "info": ("/documents/info?type={document_type}", "GET"),
        "templates": ("/documents/templates", "GET"),
        "types": ("/documents/types?lang={lang}", "GET"),  # no auth
        "statuses": ("/documents/statuses?lang={lang}", "GET"),  # no auth
    },

    "expenses": {
        "add": ("/expenses", "POST"),
        "{expense_id}": {
            "get": ("/expenses/{expense_id}", "GET"),
            "update": ("/expenses/{expense_id}", "PUT"),
            "delete": ("/expenses/{expense_id}", "DELETE"),
            "open": ("/expenses/{expense_id}/open", "POST"),
            "close": ("/expenses/{expense_id}/close", "POST"),
        },
        "search": {
            "expenses": ("/expenses/search", "POST"),
            "drafts": ("/expenses/drafts/search", "POST"),
        },
        "statuses": ("/expenses/statuses", "GET"),  # no auth
        "file": ("/expenses/file", "GET"),
        "example": {
            "add": ("/expenses/example", "POST"),  # no auth ## 'Content-Type': 'multipart/form-data; boundary=---BOUNDARY'
            "update": ("/expenses/example", "POST"),  # no auth ## 'Content-Type': 'multipart/form-data; boundary=---BOUNDARY'
        }
    },
    "accounting": ("/accounting/classifications/map", "GET"),  # REQUIRES auth
    "payments": {
        "form": ("/payments/form", "POST"),
        "tokens": {
            "search": ("/payments/tokens/search", "POST"),
            "charge": ("/payments/tokens/{token_id}/charge", "POST"),
        }
    },
    "partners": {  # basic auth
        "users": {
            "get_all": ("/partners/users", "GET"),
            "connection": {
                "approve": ("/partners/users/connection", "POST"),
                "delete": ("/partners/users/connection?email={user_email}", "DELETE"),
            },
            "get": ("/partners/users?email={user_email}", "GET"),
        }
    }
}


TOOLS_ENDPOINTS = {
    "businesses": ("/businesses/v1/occupations?locale=he_IL", "GET"),
    "geo-location": {
        "countries": ("/geo-location/v1/countries?locale={locale}", "GET"),
        "cities": ("geo-location/v1/cities?locale={locale}&country=IL", "GET"),
    },
    "currency-exchange": ("/currency-exchange/v1/latest?base={base}", "GET")
}