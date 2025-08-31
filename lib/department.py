from __init__ import CURSOR, CONN

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    # -------------------- Table Methods --------------------
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS departments;"
        CURSOR.execute(sql)
        CONN.commit()

    # -------------------- Row Methods --------------------
    def save(self):
        """Insert a new row with object's attributes, update id"""
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        """Create an object and save it in one step"""
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update the database row for this object"""
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the database row for this object"""
        sql = "DELETE FROM departments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
