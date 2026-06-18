from pathlib import Path

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks

def add_metadata(
    chunks,
    filename,
    ticker="unknown"
):

    for chunk in chunks:

        chunk.metadata["source"] = filename

        chunk.metadata["ticker"] = ticker

    return chunks