import requests


class LegalAPI:
    def __init__(self, token):
        """
        Initialize LegalAPI with authorization token.

        Args:
        token (str): Authorization token.
        """
        self.token = token
        self.base_url = "https://legal-api.sirotinsky.com/"

    def _make_request(self, endpoint):
        """
        Make a GET request to the API endpoint.

        Args:
        endpoint (str): The API endpoint to request.

        Returns:
        dict: JSON response from the API.
        """
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.base_url + endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_root(self):
        """
        Get root information from the API.

        Returns:
        dict: Root information.
        """
        return self._make_request("/")

    def get_efrsb_publisher_messages(self, inn):
        """
        Get publisher messages from EFRSB by INN.

        Args:
        inn (str): INN of the publisher.

        Returns:
        dict: Publisher messages.
        """
        return self._make_request(f"/{self.token}/efrsb/publisher_messages/{inn}")

    def get_efrsb_debtor_messages(self, inn):
        """
        Get debtor messages from EFRSB by INN.

        Args:
        inn (str): INN of the debtor.

        Returns:
        dict: Debtor messages.
        """
        return self._make_request(f"/{self.token}/efrsb/debtor_messages/{inn}")

    def get_efrsb_manager_all(self):
        """
        Get all managers from EFRSB.

        Returns:
        dict: All managers.
        """
        return self._make_request(f"/{self.token}/efrsb/manager/all")

    def get_efrsb_manager(self, inn):
        """
        Get manager from EFRSB by INN.

        Args:
        inn (str): INN of the manager.

        Returns:
        dict: Manager information.
        """
        return self._make_request(f"/{self.token}/efrsb/manager/{inn}")

    def get_efrsb_trader_all(self):
        """
        Get all traders from EFRSB.

        Returns:
        dict: All traders.
        """
        return self._make_request(f"/{self.token}/efrsb/trader/all")

    def get_efrsb_trader(self, inn):
        """
        Get trader from EFRSB by INN.

        Args:
        inn (str): INN of the trader.

        Returns:
        dict: Trader information.
        """
        return self._make_request(f"/{self.token}/efrsb/trader/{inn}")

    def get_efrsb_person(self, inn):
        """
        Get person from EFRSB by INN.

        Args:
        inn (str): INN of the person.

        Returns:
        dict: Person information.
        """
        return self._make_request(f"/{self.token}/efrsb/person/{inn}")

    def get_efrsb_organisation(self, inn):
        """
        Get organisation from EFRSB by INN.

        Args:
        inn (str): INN of the organisation.

        Returns:
        dict: Organisation information.
        """
        return self._make_request(f"/{self.token}/efrsb/organisation/{inn}")

