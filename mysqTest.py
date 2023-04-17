import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python"
)
cursor =mydb.cursor()
cursor.execute("INSERT INTO `data`(`ppt_post_title`) VALUES ('');")
datas = cursor.fetchall()
for data in datas:
    print(data)

cursor.close()
mydb.commit()
mydb.close() # 關閉資料庫連線
# print(mydb)