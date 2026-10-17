import importlib.util
import pathlib
import unittest
PATH = pathlib.Path(__file__).resolve().parents[1] / "scripts/sync_shopify.py"
spec = importlib.util.spec_from_file_location("sync_shopify", PATH)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)
class ShopifySyncTests(unittest.TestCase):
    def test_public_product(self):
        value=sync.clean({"handle":"test-product","title":"Testprodukt","product_type":"Muggar","variants":[{"price":"149.00","available":True}],"images":[{"src":"https://cdn.shopify.com/test.jpg"}]})
        self.assertEqual(value["price"],149)
        self.assertEqual(value["url"],"https://skaraborgmerch.se/products/test-product")
        self.assertEqual(value["category"],"Muggar")
    def test_no_unavailable_variants(self):
        self.assertIsNone(sync.clean({"handle":"product","title":"Test","variants":[{"price":"99","available":False}]}))
    def test_invalid_handle(self):
        self.assertIsNone(sync.clean({"handle":"../../private","title":"Test","variants":[{"price":"99"}]}))
if __name__=="__main__":
    unittest.main()
