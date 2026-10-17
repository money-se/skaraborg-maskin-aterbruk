import datetime as dt
import importlib.util
import pathlib
import tempfile
import unittest
from unittest.mock import patch

PATH=pathlib.Path(__file__).resolve().parents[1]/"scripts"/"sync_tradera.py"
spec=importlib.util.spec_from_file_location("sync_tradera",PATH)
sync=importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

NOW=dt.datetime(2026,10,17,tzinfo=dt.timezone.utc)

class TraderaTests(unittest.TestCase):
    def test_valid_item(self):
        item={"id":1234,"shortDescription":"Briggs motor","categoryId":100,"buyItNowPrice":125,"endDate":"2026-10-20T12:00:00Z","status":{"ended":False,"gotWinner":False,"gotBidders":False},"remainingQuantity":1,"itemType":3}
        output=sync.normalize(item,NOW)
        self.assertEqual(output["price"],125)
        self.assertEqual(output["price_kind"],"buy_now")
        self.assertEqual(output["title"],"Briggs motor")
        self.assertEqual(output["url"],"https://www.tradera.com/item/100/1234")
    def test_auction_starting_bid(self):
        item={"id":7,"shortDescription":"Auktion","categoryId":100,"openingBid":50,"maxBid":70,"itemType":1,"status":{"ended":False,"gotWinner":False,"gotBidders":False},"remainingQuantity":1,"endDate":"2026-10-20T12:00:00Z"}
        output=sync.normalize(item,NOW)
        self.assertEqual(output["price"],50)
        self.assertEqual(output["price_kind"],"starting_bid")
    def test_sold_item_excluded(self):
        self.assertIsNone(sync.normalize({"id":2,"title":"Såld","categoryId":100,"isSold":True},NOW))
    def test_ended_item_excluded(self):
        self.assertIsNone(sync.normalize({"id":2,"title":"Slut","categoryId":100,"endDate":"2026-10-15T00:00:00Z"},NOW))
    def test_malicious_link_never_published(self):
        item={"id":5,"title":"Test","url":"javascript:alert(1)"}
        self.assertIsNone(sync.normalize(item,NOW))
    def test_unexpected_response_does_not_overwrite(self):
        class FakeResponse:
            def __enter__(self):return self
            def __exit__(self,*a):return False
            def read(self,*args):return b'{"invalid":"schema"}'
        with tempfile.TemporaryDirectory() as tmp:
            feed=pathlib.Path(tmp)/"data.json"
            feed.write_text("keep")
            with patch.object(sync,"DEST",feed),patch.dict(sync.os.environ,{"TRADERA_APP_ID":"test","TRADERA_APP_KEY":"fake"}),patch.object(sync.urllib.request,"urlopen",return_value=FakeResponse()):
                with self.assertRaises(ValueError):sync.main()
            self.assertEqual(feed.read_text(),"keep")

if __name__=="__main__":unittest.main()
