import unittest
import os
import mylib.CRUD as crud

class TestSimpleCRUD(unittest.TestCase):
    def setUp(self):
        self.db_file = './data/test_database.db'
        self.db = crud.Database(self.db_file)

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_user_crud(self):
        # Create and get user
        user_id = self.db.create_user("john@example.com", "John", "Doe", "123 Main St", 100)
        user = self.db.get_user(user_id)
        self.assertEqual(user['email'], "john@example.com")

        # Update user
        self.db.update_user(user_id, email="johndoe@example.com", balance=200)
        updated_user = self.db.get_user(user_id)
        self.assertEqual(updated_user['email'], "johndoe@example.com")
        self.assertEqual(updated_user['balance'], 200)

        # Delete user
        self.db.delete_user(user_id)
        deleted_user = self.db.get_user(user_id)
        self.assertIsNone(deleted_user)

    def test_product_crud(self):
        # Create and get product
        product_id = self.db.create_product("Laptop", "Electronics", 999.99, 10)
        product = self.db.get_product(product_id)
        self.assertEqual(product['name'], "Laptop")

        # Update product
        self.db.update_product(product_id, price=899.99, stock=15)
        updated_product = self.db.get_product(product_id)
        self.assertEqual(updated_product['price'], 899.99)
        self.assertEqual(updated_product['stock'], 15)

        # Delete product
        self.db.delete_product(product_id)
        deleted_product = self.db.get_product(product_id)
        self.assertIsNone(deleted_product)

if __name__ == '__main__':
    unittest.main()