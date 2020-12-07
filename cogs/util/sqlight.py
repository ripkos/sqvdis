import sqlite3


class SQLite:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    # return self.cursor.execute("")

    #
    """
    def add_server(self, server_id, server_name, server_number, server_link):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `servers` (`server_id`, `server_name`, `server_number`, `server_link`) VALUES (server_id, server_name, server_number, server_link)"
            )
    """

    def check_server(self, sname):
        with self.connection:
            return self.cursor.execute("SELECT 1 FROM main.servers WHERE EXISTS ("
                                       "SELECT Server_Link FROM servers"
                                       " WHERE Server_Name= ?  )", (sname,)).fetchall()

    def get_server_link(self, sname):
        with self.connection:
            dlist = self.cursor.execute("SELECT Server_Link FROM main.servers WHERE Server_Name = ? ", (sname,)).fetchall()
            return dlist[0][0]

    def get_server_name(self, sname):
        with self.connection:
            dlist = self.cursor.execute("SELECT DISTINCT Server_FullName FROM main.servers WHERE Server_Name = ?",
                                        (sname,)).fetchall()
            return dlist[0][0]

    def check_all_servers(self, snames):
        with self.connection:
            return self.cursor.execute("SELECT 1 FROM main.servers WHERE EXISTS ("
                                       "SELECT Server_Name FROM servers"
                                       " WHERE Server_Name LIKE ? )", (snames,)).fetchall()

    def get_all_servers(self, snames):
        with self.connection:
            dlist = self.cursor.execute("SELECT Server_Name FROM main.servers WHERE Server_Name LIKE ?",
                                        (snames,)).fetchall()
            return dlist

    #
    """
    def get_moders(self):
        with self.connection:
            moderList = self.cursor.execute("SELECT `mNick` FROM `moders`").fetchall()
            return moderList

    def get_discord(self, moder):
        with self.connection:
            dis = self.cursor.execute("SELECT mDiscord FROM moders WHERE mNick = ? AND '1' = ? ", (moder, '1')).fetchall()
            if len(dis) > 0:
                return '<@'+dis[0][0]+'>'
            else:
                return '<@Ping>'
    """

    def get_server_list(self):
        with self.connection:
            dlist = self.cursor.execute(
                "SELECT Server_Name,  Server_FullName FROM main.servers ORDER BY Server_Name").fetchall()
            return dlist

    def close(self):
        self.connection.close()
