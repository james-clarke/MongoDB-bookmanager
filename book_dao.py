from pymongo_connector import collection
from pymongo_connector import publisher_collection


def findAll():
    results = collection.find()
    return results


def findByTitle(book_title):
    results = collection.find({'title': book_title})
    return results


def findByPublisher(book_publisher):
    results = collection.find({'published_by': book_publisher})
    return results


def findByPriceRange(min_price, max_price):
    results = collection.find({'price': {'$gte': min_price, '$lte': max_price}})
    return results


def findByTitleAndPublisher(book_title, publisher_name):
    results = collection.find({'title': book_title, 'published_by': publisher_name})
    return results


def add_publisher(name, phone, city):
    publisher = {'name': name, 'phone': phone, 'city': city}
    try:
        result = publisher_collection.insert_one(publisher)
        return result
    except Exception as e:
        print("An error occurred:", e)
        return None
