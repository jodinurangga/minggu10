import requests
import json

# Misalkan data "word definition" yang diperoleh dari API Dictionary
word_definition = [
    {
        "definition": "the action of making or manufacturing from components or raw materials",
        "partOfSpeech": "noun"
    },
    {
        "definition": "to bring a substance into contact with a chemical",
        "partOfSpeech": "verb"
    },
    {
        "definition": "to produce something by a chemical process",
        "partOfSpeech": "verb"
    }
]

# Definisikan variabel baru yang hanya menyimpan data yang diperlukan
simplified_data = [{"definition": item["definition"], "partOfSpeech": item["partOfSpeech"]} for item in word_definition]

# Kirim data yang telah disederhanakan ke server
url = "http://localhost:5000/detail/example"
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(simplified_data), headers=headers)

if response.status_code == 200:
    print("Data berhasil dikirim ke server")
else:
    print("Terjadi kesalahan:", response.content)
