import requests
import pytest
import copy

@pytest.mark.api
class TestApi:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_url = "https://restapidev.payplus.co.il/api/payment-pages/generate-link"
        # Initialize the common body payload
        self.body_template = {
            "payment_page_uid": "1c0caa1c-7782-4ff6-bfe6-c4e9fcc9d3ae",
            "charge_method": 1,
            "charge_default": "credit-card",
            "hide_other_charge_methods": False,
            "language_code": "he",
            "amount": 10,
            "currency_code": "ILS",
            "sendEmailApproval": True,
            "sendEmailFailure": False,
            "expiry_datetime": "30",
            "refURL_success": "https://www.domain.com/success/",
            "refURL_failure": "https://www.domain.com/failure/",
            "refURL_cancel": "https://www.domain.com/cancel/",
            "refURL_callback": "https://www.domain.com/callback/",
            "send_failure_callback": False,
            "custom_invoice_name": "Customer Name",
            "create_token": False,
            "initial_invoice": False,
            "invoice_language": False,
            "paying_vat": True,
            "hide_payments_field": False,
            "payments": 5,
            "payments_credit": False,
            "payments_selected": 2,
            "payments_first_amount": 5,
            "hide_identification_id": False,
            "send_customer_success_sms": False,
            "customer_failure_sms": False,
            "add_user_information": False
        }
        yield  # Allows the fixture to be used in tests

    def test_payment_page_success(self):
        # Make a copy of the body to ensure the original template is not modified
        body = copy.deepcopy(self.body_template)

        response = requests.post(self.base_url, json=body)
        print(f"Test result: response code {response.status_code}")
        assert response.status_code == 200, "Expected success response"

    def test_payment_page_missing_uid(self):
        # Make a copy of the body and remove the payment_page_uid field
        body = copy.deepcopy(self.body_template)
        body.pop("payment_page_uid", None)  # Remove the 'payment_page_uid' key

        response = requests.post(self.base_url, json=body)
        print(f"Test result: response code {response.status_code}")
        assert response.status_code == 422, "Expected a client error due to missing required fields"

    def test_payment_page_charge_default(self):
        # Make a copy of the body and remove the payment_page_uid field
        body = copy.deepcopy(self.body_template)
        body.pop("charge_default", None)  # Remove the 'payment_page_uid' key

        response = requests.post(self.base_url, json=body)
        print(f"Test result: response code {response.status_code}")
        assert response.status_code == 200, "Expected success response"

    def test_negative_amount_value(self):
        # Make a copy of the body and set the amount field as a string
        body = copy.deepcopy(self.body_template)
        body["amount"] = -1  # Sending amount as a string instead of an integer

        response = requests.post(self.base_url, json=body)
        print(f"Test result: response code {response.status_code}")
        assert response.status_code == 422, "Expected a client error due to missing required fields"

    def test_invalid_value_paying_vat(self):
        # Make a copy of the body and set the amount field as a string
        body = copy.deepcopy(self.body_template)
        body["paying_vat"] = 5  # Sending amount as a string instead of an integer

        response = requests.post(self.base_url, json=body)
        print(f"Test result: response code {response.status_code}")
        assert response.status_code == 422

    def test_empty_body(self):
        body = {}
        response = requests.post(self.base_url, json=body)
        print(f"Test result: Payment page response code {response.status_code}")
        print(f"Response body: {response.json()}")

        assert response.status_code == 422, "Expected a client error due to missing required fields"

    def test_allowed_issuers_field(self):
        # Make a copy of the original body template
        body = copy.deepcopy(self.body_template)

        # Add the allowed_issuers field to the body
        body["allowed_issuers"] = ["max", "visacal"]

        response = requests.post(self.base_url, json=body)
        print(f"Test result: Payment page response code {response.status_code}")

        assert response.status_code == 200, "Expected success response"
