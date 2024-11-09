from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def select_category(self, category_id: int) -> Category:
        category_select = next(x for x in self.categories if x.id == category_id)
        return category_select

    def select_topic(self, topic_id: int) -> Topic:
        topic_select = next(x for x in self.topics if x.id == topic_id)
        return topic_select

    def select_document(self, document_id: int) -> Document:
        doc_select = next(x for x in self.documents if x.id == document_id)
        return doc_select

    def edit_category(self, category_id: int, new_name: str):
        self.select_category(category_id).edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.select_topic(topic_id).edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.select_document(document_id).edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove(self.select_category(category_id))

    def delete_topic(self, topic_id):
        self.topics.remove(self.select_topic(topic_id))

    def delete_document(self, document_id):
        self.documents.remove(self.select_document(document_id))

    def get_document(self, document_id) -> Document:
        return self.select_document(document_id)

    def __repr__(self) -> str:
        representation = '\n'.join([x.__repr__() for x in self.documents])
        return representation
