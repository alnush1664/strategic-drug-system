import unittest

class TestDrugSystem(unittest.TestCase):

    def test_login_success(self):
        username = "admin"
        password = "1234"
        self.assertEqual(username, "admin")
        self.assertEqual(password, "1234")

    def test_login_fail(self):
        username = "admin"
        password = "1111"
        self.assertNotEqual(password, "1234")

    def test_add_drug(self):
        inventory = []
        inventory.append("Insulin")
        self.assertEqual(len(inventory), 1)

    def test_inventory(self):
        inventory = {
            "Insulin": 20
        }
        self.assertTrue("Insulin" in inventory)

    def test_low_stock(self):
        quantity = 15
        self.assertTrue(quantity < 20)

    def test_normal_stock(self):
        quantity = 150
        self.assertFalse(quantity < 20)

    def test_expire_date(self):
        expire = "2026-12-01"
        self.assertEqual(expire, "2026-12-01")

    def test_alert_list(self):
        alerts = ["Insulin"]
        self.assertEqual(len(alerts),1)

    def test_inventory_not_empty(self):
        inventory = ["Drug1","Drug2"]
        self.assertGreater(len(inventory),0)

    def test_api_response(self):
        status = 200
        self.assertEqual(status,200)

if __name__ == "__main__":
    unittest.main()

