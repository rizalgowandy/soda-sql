#  Copyright 2020 Soda
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import List

from sodasql.scan.db import sql_fetchone, sql_fetchall
from sodasql.scan.dialect import Dialect


class Warehouse:

    def __init__(self, dialect: Dialect):
        self.dialect = dialect
        self.connection = dialect.create_connection()

    def sql_fetchone(self, sql) -> tuple:
        return sql_fetchone(self.connection, sql)

    def sql_fetchall(self, sql) -> List[tuple]:
        return sql_fetchall(self.connection, sql)

    def create_scan(self, scan_configuration):
        return self.dialect.create_scan(self, scan_configuration)

    def close(self):
        self.connection.close()
