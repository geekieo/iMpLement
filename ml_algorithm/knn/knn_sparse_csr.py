#!/usr/bin/python3
''' 
Description: KNN with sparse data
implament using csr_matrix
'''

import numpy as np
from scipy.sparse import csr_matrix


def kNN_Sparse(local_data_csr, query_data_csr, top_k):
    # calculate the square sum of each vector
    local_data_sq = local_data_csr.multiply(local_data_csr).sum(1)
    query_data_sq = query_data_csr.multiply(query_data_csr).sum(1)

    # calculate the dot
    distance = query_data_csr.dot(local_data_csr.transpose()).todense()

    # calculate the distance
    num_query, num_local = distance.shape
    distance = np.tile(query_data_sq,
                       (1, num_local)) + np.tile(local_data_sq.T,
                                                 (num_query, 1)) - 2 * distance

    # get the top k
    topK_idx = np.argsort(distance)[:, 0:top_k]
    topK_similarity = np.zeros((num_query, top_k), np.float32)
    for i in range(num_query):
        topK_similarity[i] = distance[i, topK_idx[i]]

    return topK_similarity, topK_idx


def run_knn():
    top_k = np.array(2, dtype=np.int32)
    local_data_offset = np.array([0, 1, 2, 4, 6], dtype=np.int64)
    local_data_index = np.array([0, 1, 0, 1, 0, 2], dtype=np.int32)
    local_data_value = np.array([1, 2, 3, 4, 8, 9], dtype=np.float32)
    local_data_csr = csr_matrix(
        (local_data_value, local_data_index, local_data_offset),
        dtype=np.float32)
    print(local_data_csr.todense())

    query_offset = np.array([0, 1, 4], dtype=np.int64)
    query_index = np.array([0, 0, 1, 2], dtype=np.int32)
    query_value = np.array([1.1, 3.1, 4, 0.1], dtype=np.float32)
    query_csr = csr_matrix(
        (query_value, query_index, query_offset), dtype=np.float32)
    print(query_csr.todense())

    topK_similarity, topK_idx = kNN_Sparse(local_data_csr, query_csr, top_k)

    for i in range(query_offset.shape[0] - 1):
        print("for %d image, top %d is " % (i, top_k), topK_idx[i])
        print("corresponding similarity: ", topK_similarity[i])


if __name__ == '__main__':
    run_knn()
