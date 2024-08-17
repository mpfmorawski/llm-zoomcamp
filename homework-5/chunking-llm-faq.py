if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    import hashlib

    def generate_document_id(doc):
        combined = f"{doc['course']}-{doc['question']}-{doc['text'][:10]}"
        hash_object = hashlib.md5(combined.encode())
        hash_hex = hash_object.hexdigest()
        document_id = hash_hex[:8]
        return document_id

    documents = []

    for doc in data['documents']:
        doc['course'] = data['course']
        doc['document_id'] = generate_document_id(doc)
        documents.append(doc)

    print(len(documents))

    return documents


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'