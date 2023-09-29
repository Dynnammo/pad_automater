from nocodb.nocodb import NocoDBProject, APIToken, JWTAuthToken
from nocodb.filters import EqFilter
from nocodb.infra.requests_client import NocoDBRequestsClient
import os
from pprint import pprint

# Usage with API Token
class NocodbClient():
    def __init__(self):
        self.client = NocoDBRequestsClient(
            APIToken(os.environ["NOCODB_TOKEN"]),
            os.environ["NOCODB_URL"]
        )
        self.project = NocoDBProject(
            "noco", # org name. noco by default
            os.environ["NOCODB_PROJECT"] # project name. Case sensitive!!
        )
        self.table = os.environ["NOCODB_TABLE"]

    def create_pad_row(self, pad_infos={}):
        if not self.check_existing_pad(pad_infos):
            print(pad_infos["Title"])
            self.client.table_row_create(
                self.project,
                self.table,
                pad_infos
            )
            print(f'Created row: {pad_infos["Link"]}')

    def check_existing_pad(self, pad_infos):
        data = self.client.table_row_list(
            self.project,
            self.table,
            EqFilter('Title', pad_infos["Title"])
        )
        
        return len(data['list']) > 0
