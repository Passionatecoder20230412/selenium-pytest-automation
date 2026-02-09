from API_auto.Utils.User_api import UserAPI

class TestProducts:
    def test_products_list(self):
        user_api = UserAPI()
        response = user_api.products_list()

        assert response.status_code == 200
        print(response.json())