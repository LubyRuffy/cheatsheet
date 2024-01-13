import os
from datasets import load_dataset
from bs4 import BeautifulSoup
import faiss
import numpy as np

faiss_index_file = "wooyun_faiss.index"
model = None


def get_model():
    global model

    if model is not None:
        return model
    from sentence_transformers import SentenceTransformer
    model_name = 'maidalun1020/bce-embedding-base_v1'
    device = "mps"  # cpu
    model = SentenceTransformer(model_name, device=device)
    return model


def get_updated_dataset():
    # 读取数据
    print("读取数据")
    dataset = load_dataset('json', data_files=os.path.expanduser('~/Downloads/bugs.json'))
    # dataset['train'].shape # (88820, 19)
    # dataset['train'].column_names #['Ranks', 'wybug_id', 'wybug_type', 'wybug_corp', 'wybug_date', 'replys', 'wybug_detail', 'wybug_open_date', 'wybug_rank_fromcorp', 'wybug_rank_0', 'wybug_author', 'wybug_reply', 'wybug_from', 'wybug_title', 'wybug_tags', 'wybug_status', 'wybug_level', 'wybug_level_fromcorp', 'id']
    dataset = dataset["train"]
    # dataset = dataset.select(range(10)) #调试用
    return dataset.map(lambda x: {
        "wybug_id": x["wybug_id"],
        "id": x["id"],
        "content": "标题: " + x['wybug_title'] + "\n\n\n"
                   + BeautifulSoup(x['wybug_detail'][1:], "lxml").text
                       .replace("\t\t\t\t\t\t", "\n\n")})


def gen_index():
    global faiss_index_file

    # 生成向量
    print("生成向量")
    updated_dataset = get_updated_dataset()
    embeddings = model.encode(updated_dataset["content"], show_progress_bar=True)
    print(embeddings.shape)  # (88820, 768)
    # print(embeddings)
    ids = updated_dataset["id"]
    # ids = [int(x.split("-")[2]) for x in updated_dataset["wybug_id"]] # 取wooyun-id

    # 存入faiss数据库
    print("存入faiss数据库")

    # Instantiate the index with faiss
    index = faiss.IndexFlatL2(embeddings.shape[1])
    # Pass the index to IndexIDMap
    # index = faiss.IndexIDMap(index)
    # Add vectors and their IDs, set to be DF indexes
    # index.add_with_ids(np.array(embeddings, dtype=np.float32), ids)
    index.add(np.array(embeddings, dtype=np.float32))
    faiss.write_index(index, faiss_index_file)


def query(query_str):
    global faiss_index_file

    # 查询数据库
    print("查询数据库")
    index = faiss.read_index(faiss_index_file)
    vector = get_model().encode([query_str])
    L2, ID = index.search(np.array(vector, dtype=np.float32), 10)
    updated_dataset = get_updated_dataset()
    for i in range(len(ID[0])):
        print(L2[0][i], updated_dataset[int(ID[0][i])])


query("由于未知资产导致的漏洞")
