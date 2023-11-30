from pymongo_connector import collection
from pymongo_connector import publisher_collection


# Find and return all books in the collection.
def findAll():
    results = collection.find()
    return results


# Find and return books by their title.
def findByTitle(book_title):
    results = collection.find({'title': book_title})
    return results


# Find and return books by their publisher.
def findByPublisher(book_publisher):
    results = collection.find({'published_by': book_publisher})
    return results


# Find and return books within a specified price range.
def findByPriceRange(min_price, max_price):
    results = collection.find({'price': {'$gte': min_price, '$lte': max_price}})
    return results


# Find and return books by a combination of title and publisher.
def findByTitleAndPublisher(book_title, publisher_name):
    results = collection.find({'title': book_title, 'published_by': publisher_name})
    return results


# Add a new publisher to the Publisher collection.
def addPublisher(name, phone, city):
    publisher = {'name': name, 'phone': phone, 'city': city}
    try:
        result = publisher_collection.insert_one(publisher)
        return result
    except Exception as e:
        print("An error occurred:", e)
        return None


# Add a new book to the Book collection.
def addBook(isbn, title, year, published_by, previous_edition, price):
    book_data = {'ISBN': isbn, 'title': title, 'year': year, 'published_by': published_by,
                 'previous_edition': previous_edition, 'price': price}
    try:
        result = collection.insert_one(book_data)
        return result
    except Exception as e:
        print("An error occurred:", e)
        return None


# Edit an existing book in the Book collection.
def editBook(isbn, title=None, year=None, published_by=None, previous_edition=None, price=None):
    update_book = {}
    if title:
        update_book['title'] = title
    if year:
        update_book['year'] = year
    if published_by:
        update_book['published_by'] = published_by
    if previous_edition:
        update_book['previous_edition'] = previous_edition
    if price:
        update_book['price'] = price
    if not update_book:
        print("No new data provided to update.")
        return None
    try:
        result = collection.update_one({'ISBN': isbn}, {'$set': update_book})
        return result
    except Exception as e:
        print("An error occurred:", e)
        return None


# Delete a book from the Book collection based on its ISBN.
def deleteBook(isbn):
    try:
        result = collection.delete_one({'ISBN': isbn})
        return result
    except Exception as e:
        print("An error occurred:", e)
        return None
