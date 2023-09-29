from nocodb_parser import NocodbClient
from hedgedoc import get_pad_list
import os

pad_list = get_pad_list()
nocodb_client = NocodbClient()

print(len(pad_list))
for pad in pad_list:
    pad_info = {
        "Author": "TODO",
        "Title": pad['text'],
        "Link": f"{os.environ['HEDGEDOC_URL']}/{pad['id']}",
    }
    nocodb_client.create_pad_row(pad_info)