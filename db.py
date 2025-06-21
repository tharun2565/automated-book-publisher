import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

def save_version(title, content):
    collection.add(documents=[content], ids=[title])

