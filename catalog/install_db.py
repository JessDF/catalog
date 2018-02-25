from item_database_config import Category
from database_operations import DatabaseOperations

db = DatabaseOperations()
new_categories = [Category(name='Plants'),
                  Category(name='Bathroom'),
                  Category(name='School'),
                  Category(name='Bedroom'),
                  Category(name='Kitchen')]
for new_category in new_categories:
    db.addToDatabase(new_category)
