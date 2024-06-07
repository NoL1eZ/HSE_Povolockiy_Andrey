import requests

class LegalAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://legal-api.sirotinsky.com"

    def _make_request(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.base_url + endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_root(self):
        return self._make_request("/")

    def get_efrsb_publisher_messages(self, inn):
        return self._make_request(f"/{self.token}/efrsb/publisher_messages/{inn}")

    def get_efrsb_debtor_messages(self, inn):
        return self._make_request(f"/{self.token}/efrsb/debtor_messages/{inn}")

    def get_efrsb_manager_all(self):
        return self._make_request(f"/{self.token}/efrsb/manager/all")

    def get_efrsb_manager(self, inn):
        return self._make_request(f"/{self.token}/efrsb/manager/{inn}")

    def get_efrsb_trader_all(self):
        return self._make_request(f"/{self.token}/efrsb/trader/all")

    def get_efrsb_trader(self, inn):
        return self._make_request(f"/{self.token}/efrsb/trader/{inn}")

    def get_efrsb_person(self, inn):
        return self._make_request(f"/{self.token}/efrsb/person/{inn}")

    def get_efrsb_organisation(self, inn):
        return self._make_request(f"/{self.token}/efrsb/organisation/{inn}")
