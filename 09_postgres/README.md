# Postgres SQL

<a href="" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/FOLDER_NAME/.png?raw=true" alt="DESCRIPTION" width="600">
</a>

## Connect to postgres

We will spin up a postgres container with docker compose and connect to it in the terminal. Start with creating a .env in your folder and fill in information for your postgres setup:

```bash
POSTGRES_HOST="localhost"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="your_supersafe_password" # NOTE: change this
POSTGRES_DB="myh_db"
POSTGRES_PORT=5432
```

Use the docker-compose file in this directory and add it to your directory. Then run `docker-compose up -d`. Go into your postgres container with

```bash
docker exec -it postgres bash
```

```bash
psql -U your_username -d your_database
```

> [!NOTE]
> The password is not required when connecting to postgres locally i.e. inside of the container. When connecting from the host machine directly it will require a password. This is the default settings of postgres.

## Reference on postgres commands

This is not a complete list, but some that might be useful for reference.

### Useful psql commands

| Command            | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `\l`               | List all databases                                        |
| `\c database_name` | Connect to a specific database                            |
| `\dt`              | List all tables in the current database                   |
| `\d table_name`    | Show table structure (columns, types, constraints)        |
| `\du`              | List all users and roles                                  |
| `\conninfo`        | Show current connection info (user, database, host, port) |
| `\q`               | Quit `psql`                                               |

### Table management (DDL)

| Command                                                       | Description                          |
| ------------------------------------------------------------- | ------------------------------------ |
| `CREATE DATABASE db_name;`                                    | Create a new database                |
| `DROP DATABASE db_name;`                                      | Delete a database (**irreversible**) |
| `ALTER DATABASE db_name RENAME TO new_name;`                  | Rename a database                    |
| `CREATE TABLE table_name (id SERIAL PRIMARY KEY, name TEXT);` | Create a new table                   |
| `DROP TABLE table_name;`                                      | Delete a table (**irreversible**)    |
| `ALTER TABLE table_name ADD COLUMN column_name TYPE;`         | Add a new column                     |
| `ALTER TABLE table_name DROP COLUMN column_name;`             | Remove a column                      |
| `ALTER TABLE table_name RENAME TO new_table_name;`            | Rename a table                       |
| `TRUNCATE TABLE table_name;`                                  | Remove all rows from a table         |

### User & role management (DCL)

| Command                                                  | Description                         |
| -------------------------------------------------------- | ----------------------------------- |
| `GRANT ALL PRIVILEGES ON DATABASE db_name TO user;`      | Grant full privileges to a user     |
| `REVOKE ALL PRIVILEGES ON DATABASE db_name FROM user;`   | Revoke privileges                   |
| `CREATE USER user_name WITH PASSWORD 'your_password';`   | Create a new user                   |
| `DROP USER user_name;`                                   | Delete a user                       |
| `ALTER USER user_name WITH SUPERUSER;`                   | Grant superuser privileges          |
| `ALTER USER user_name WITH PASSWORD 'new_password';`     | Change user password                |
| `GRANT CONNECT ON DATABASE db_name TO user_name;`        | Allow user to connect to a database |
| `GRANT USAGE ON SCHEMA public TO user_name;`             | Allow user to use public schema     |
| `GRANT ALL PRIVILEGES ON TABLE table_name TO user_name;` | Grant all privileges on a table     |

### Query data (DQL)

| Command                                                    | Description                             |
| ---------------------------------------------------------- | --------------------------------------- |
| `SELECT * FROM table_name;`                                | Select all data from a table            |
| `SELECT column1, column2 FROM table_name WHERE condition;` | Select specific columns with conditions |
| `SELECT COUNT(*) FROM table_name;`                         | Count number of rows                    |
| `SELECT DISTINCT column_name FROM table_name;`             | Select distinct values                  |
| `SELECT * FROM table_name ORDER BY column_name ASC/DESC;`  | Sort results                            |

### Updating & deleting data (DML)

| Command                                                              | Description                            |
| -------------------------------------------------------------------- | -------------------------------------- |
| `INSERT INTO table_name (column1, column2) VALUES (value1, value2);` | Insert new data                        |
| `UPDATE table_name SET column1 = value WHERE condition;`             | Update existing data                   |
| `DELETE FROM table_name WHERE condition;`                            | Delete specific rows                   |
| `DELETE FROM table_name;`                                            | Delete all rows (**use with caution**) |

---

## Other videos 📹

## Read more 👓
