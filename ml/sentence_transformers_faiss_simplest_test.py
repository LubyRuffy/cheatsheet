import faiss
import sentence_transformers

# 模型
model = sentence_transformers.SentenceTransformer('maidalun1020/bce-embedding-base_v1')

# 文本
texts = ["这是一篇关于自然语言处理的文档。", "这是一个关于计算机视觉的文档。", "这是一个关于机器学习的文档。"]

# 生成向量
embeddings = model.encode(texts)

# 构建索引
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# 查询
query = "机器学习的文档"
query_embedding = model.encode([query])
distances, indices = index.search(query_embedding, 3)

# 输出结果
for i in range(len(indices[0])):
    print(distances[0][i], texts[int(indices[0][i])])