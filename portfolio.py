import csv
import uuid
import chromadb

class Portfolio:
    def __init__(self,file_path) -> None:
        self.file_path =file_path
        self.data = self.read_csv(file_path)
        self.client = chromadb.PersistentClient("vectorstore2")
        self.collection  = self.client.get_or_create_collection(name="portfolio")
        
    
    def read_csv(self, file_path):
        data = []
        with open(file_path,'r') as file:
            csv_f = csv.reader(file)
            next(csv_f)
            for row in csv_f:
                skills = tuple(row[:-1])
                urls = row[-1]
                data.append((skills,urls))
        return data 

    def load_portfolio(self):
        if not self.collection.count():
            for skills, urls in self.data:
                self.collection.add(
                    documents = str(skills),
                    metadatas= {"project_urls":urls},
                    ids= [str(uuid.uuid4())]
                )
    
    def query_links(self,skills):
        return self.collection.query(query_texts=skills, n_results=2).get("metadatas", [])

