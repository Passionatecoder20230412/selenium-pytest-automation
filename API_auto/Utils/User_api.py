from API_auto.APIEndpoints.APIEndpoints import APIEndpoints
from API_auto.ApiHelpers.ApiHelpers import APIHelpers


class UserAPI:

    def __init__(self):
        self.api_helpers1 = APIHelpers()
        self.end_points=APIEndpoints()
    def proucts_list(self):
        self.api_helpers1.get_api(self.end_points.PRODUCTS_LIST,)
from API_auto.APIEndpoints.APIEndpoints import APIEndpoints
from API_auto.ApiHelpers.ApiHelpers import APIHelpers


class UserAPI:

    def __init__(self):
        self.end_points = APIEndpoints()
        self.api_helpers = APIHelpers(
            base_url=self.end_points.BASE_URL)

    def products_list(self):
        response = self.api_helpers.get_api(
            self.end_points.PRODUCTS_LIST
        )
        print(response.json())
        return response