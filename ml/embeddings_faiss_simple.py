from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
import os

query = 'fofa是什么？'
passages = [
    'FOFA 是一个网络空间测绘平台。 它将采集全球互联网的数据，允许您和您的团队随时随地取用数据。',
    '华为是一家伟大的公司。',
    '我不喜欢看电影'
]

# pycharm在调试mps时有bug
model_kwargs = {'device': 'cpu'}
if not ("PYCHARM_HOSTED" in os.environ and os.environ["PYCHARM_HOSTED"] == "1"):
    model_kwargs = {'device': 'mps'}
# print(model_kwargs)

# init embedding model
model_name = 'maidalun1020/bce-embedding-base_v1'
encode_kwargs = {'batch_size': 64, 'normalize_embeddings': True, 'show_progress_bar': True}

embed_model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# example #1. extract embeddings
query_embedding = embed_model.embed_query(query)
passages_embeddings = embed_model.embed_documents(passages)

# example #2. langchain retriever example
faiss_vectorstore = FAISS.from_texts(passages, embed_model, distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT)

retriever = faiss_vectorstore.as_retriever(search_type="similarity", search_kwargs={"score_threshold": 0.5, "k": 3})

related_passages = retriever.get_relevant_documents(query)
print(related_passages)