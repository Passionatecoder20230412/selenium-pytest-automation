import pytest
import requests
url = "https://automationexercise.com/api/productsList"
payload = {}
files={}
headers = {}
response = requests.post( url, headers=headers, data=payload, files=files)
print(response.json()["message"])
class EndPoints:
    BASE_URL="https://automationexercise.com/api"
    PRODUCT_URL="/productsList"
class Helpers:
    def get_api(self,url,endpoint,headers,data,files):
        url=url+endpoint
        resp=requests.get(url,headers=headers,data=data,files=files)
        return resp
class Products(EndPoints,Helpers):
    def get_products(self,headers,data,files):
        return self.get_api(self.BASE_URL,self.PRODUCT_URL,headers=headers,data=data,files=files)
@pytest.mark.api_test
class TestProducts(Products):
    def test_products(self):
        resp=self.get_products(headers=None,data=None,files=None)
        print(resp.json())
        assert resp.status_code == 200
        for i in range(len(resp.json()["products"])):
            print(resp.json()["products"][i]["name"])
        assert resp.json()["products"][25]["name"]=="Soft Stretch Jeans","--------Not found"
        return resp




