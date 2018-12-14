simple_user = {
  "logins": [
    {
      "email": "test@synapsepay.com"
    }
  ],
  "phone_numbers": [
    "901.111.1111"
  ],
  "legal_names": [
    "Test User"
  ],
  "extra": {
    "supp_id": "my_user_id",
    "cip_tag":1,
    "is_business": False
  }
}

simple_response = {
    "_id": "4qnfFH98Ff390HYasd4fqftkk3",
    "_links": {
        "self": {
            "href": "https://uat-api.synapsefi.com/v3.1/users/4qnfFH98Ff390HYasd4fqftkk3"
        }
    },
    "client": {
        "id": "12351346161345",
        "name": "Test Client"
    },
    "doc_status": {
        "physical_doc": "MISSING|INVALID",
        "virtual_doc": "MISSING|INVALID"
    },
    "documents": [],
    "emails": [],
    "extra": {
        "cip_tag": 1,
        "date_joined": 1544757747072,
        "extra_security": False,
        "is_business": False,
        "last_updated": 1544757747072,
        "public_note": None,
        "supp_id": "my_user_id"
    },
    "is_hidden": False,
    "legal_names": [
        "Test User"
    ],
    "logins": [
        {
            "email": "test@synapsepay.com",
            "scope": "READ_AND_WRITE"
        }
    ],
    "permission": "UNVERIFIED",
    "phone_numbers": [
        "901.111.1111"
    ],
    "photos": [],
    "refresh_token": "refresh_MJIU351ht3iur9r81g91f"
}

basedocs_user = {
  "logins": [
    {
      "email": "test@synapsepay.com"
    }
  ],
  "phone_numbers": [
    "901.111.1111"
  ],
  "legal_names": [
    "Test User"
  ],
  "documents":[{
        "email":"test@test.com",
        "phone_number":"901.111.1111",
        "ip":"::1",
        "name":"Test User",
        "alias":"Test",
        "entity_type":"M",
        "entity_scope":"Arts & Entertainment",
        "day":2,
        "month":5,
        "year":1989,
        "address_street":"1 Market St.",
        "address_city":"San Francisco",
        "address_subdivision":"CA",
        "address_postal_code":"94114",
        "address_country_code":"US",
        "virtual_docs":[{
            "document_value":"111-111-2222",
            "document_type":"SSN"
        }],
        "physical_docs":[{
            "document_value": "data:image/gif;base64,SUQs==",
            "document_type": "GOVT_ID"
        }],
        "social_docs":[{
            "document_value":"https://www.facebook.com/valid",
            "document_type":"FACEBOOK"
        }]
    }],
  "extra": {
    "supp_id": "my_user_id",
    "cip_tag":1,
    "is_business": False
  }
}