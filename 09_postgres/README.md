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
POSTGRES_DB="coins_db"
POSTGRES_PORT=5432
```

Use the docker-compose file in this directory and add it to your directory. Then run `docker-compose up -d`. 

```bash
psql -U your_username -d your_database
```


## Other videos 📹

## Read more 👓
