import chromadb
import uuid

client = chromadb.Client()

collection = client.create_collection(name="lotr_scripts")

with open("lotr_scripts.csv", "r", encoding="utf-8") as f:
    data: list[str] = []
    scripts: list[str] = f.read().splitlines()
    for script in scripts:
        splits: list[str] = script.split(",")
        data.append(": ".join([splits[1], splits[2]]))

collection.add(
    ids=[str(uuid.uuid4()) for _ in data],
    documents=data,
    metadatas=[{"line": line} for line in range(len(data))]
)

results = collection.query(
    query_texts=[
        "Gollum",
        "Gandalf"
    ],
    n_results=50
)

for i, query_results in enumerate(results["documents"]):
    print(f"\nQuery {i}")
    print("\n".join(query_results))


