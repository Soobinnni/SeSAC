from database.Database import Database

class MovieRankDatabaseQuery(Database) :
    def get_movie_dates_grouped(self) :
        sql = 'SELECT DISTINCT date FROM rank'
        result = [date['date'] for date in self.execute_fetch(sql)]

        return result
    
    def get_movie_rank_info_on_date(self, date):
        sql = """
            SELECT *
            FROM rank r
            JOIN movie m ON m.id = movie_id
            WHERE r.date = ?
            ORDER BY ranking
        """
        result = self.execute_fetch(sql, (date,))
        return result