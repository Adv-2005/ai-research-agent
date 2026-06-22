# ingestion/document_store.py

import pickle


def save_chunks(chunks):

    with open(
        "storage/documents.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )


def load_chunks():

    with open(
        "storage/documents.pkl",
        "rb"
    ) as f:

        return pickle.load(f)