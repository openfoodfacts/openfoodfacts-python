from openfoodfacts import API

api = API(user_id="tejaswibks", password="your_password")

result = api.add_image(
    barcode="1234567890123",
    imagefield="front",
    imgpath="path/to/your/image.jpg"
)

print(result.status)
