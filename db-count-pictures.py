from config import frdb
print(frdb.execute("SELECT count(*) AS num FROM pictures")[0]["num"])

