from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'Cannot open database', 'Click cancel to exit', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expense (id INTEGER primary key AUTOINCREMENT, date VARCHAR(20), category VARCHAR(20), description VARCHAR(50), balance REAL, status VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expense (date, category, description, balance, status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expense SET date=?, category=?, description=?, balance=?, status=? WHERE id=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expense WHERE id=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expense"
        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []
        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="balance")

    def total_income(self):
        return self.get_total(column="balance", filter="status", value="Income")

    def total_outcome(self):
        return self.get_total(column="balance", filter="status", value="Outcome")

    def total_groceries(self):
        return self.get_total(column="balance", filter="category", value="Groceries")

    def total_entertainment(self):
        return self.get_total(column="balance", filter="category", value="Entertainment")

    def total_auto(self):
        return self.get_total(column="balance", filter="category", value="Auto")

    def total_other(self):
        return self.get_total(column="balance", filter="category", value="Other")