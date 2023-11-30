from pymongo_connector import collection


def findAll():
    results = collection.find()
    return results


def findByTitle(book_title):
    results = collection.find({'title': book_title})
    return results


def findByPublisher(book_publisher):
    results = collection.find({'published_by': book_publisher})
    return results
