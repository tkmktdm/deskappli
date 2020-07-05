#----------------
#標準ライブラリ
#----------------
#import pymysql.cursors #Raspberry Pi，Win用
import MySQLdb          #mac用

#上の方をmacで使う場合は
# pip3 install pymysql
#でインストールする必要がある

class connect:
    def setting(self):
        cnct = MySQLdb.connect(  #Win,mac用
                host = "localhost",  #ホスト名
                user = "root",       #MySQLユーザ名
                password = "",       #MySQLユーザパスワード
                db = "test",         #データベース名
                charset = "utf8"     #文字コード
                )
        table = "testTable"
        status = '(user_name, mail_address, password, created, modified)'
        cur = cnct.cursor()
        return cnct,cur,table,status

    def insert(self, un, um, up, incur):
        cnct = incur
        cur = cnct.cursor()
        table = "testTable"
        status = '(user_name, mail_address, password, created, modified)'
        users=[]
        search = ('SELECT * FROM ' + table + ';')
        allSearch = cur.execute(search)
        #print(allSearch)
        result_users = cur.fetchall()
        for i in range(allSearch):
            users.append(result_users[i][1])
        #print(users)
        #testdata = ("b", "b@mail.com", "test", now(), now())
        #データの追加
        judge_user = 0
        usern = un
        userm = um
        userp = up
        #insert="INSERT INTO " + table + " " + status + " VALUES ('b', 'b@mail.com', 'test', now(), now());"
        for i in users:
            if i == usern:
                judge_user = 1

        if judge_user != 1 and usern != '' and userm != '' and userp != '':
            insert="INSERT INTO " + table + " " + status + " VALUES ('" + usern + "', '" + userm + "', '" + userp + "', now(), now());"
            #insert="INSERT INTO " + table + " " + status + " VALUES " + testdata + ";"
            cur.execute(insert)
            cnct.commit()
            rtn = 'new insert_database'
        elif usern == '' or userm == '' or userp == '':
            rtn = 'null object error'
        else:
            rtn = 'exist'
        
        return rtn

'''
#---------
# 接続
#---------
#cnct = pymysql.connect( #Raspberry Pi用
cnct = MySQLdb.connect(  #Win,mac用
    host = "localhost",  #ホスト名
    user = "root",       #MySQLユーザ名
    password = "",       #MySQLユーザパスワード
    db = "test",         #データベース名
    charset = "utf8"     #文字コード
    )
table = "testTable"           #テーブル名
status = '(user_name, mail_address, password, created, modified)'

cur = cnct.cursor()

#---------
# ここでデータベースの操作を行う
#---------

#tableがあれば削除して作成
table = 'test_table'
cur.execute("DROP TABLE IF EXISTS `%s`;", table)
cur.execute(
    CREATE TABLE IF NOT EXISTS `%s` (
    `id` int auto_increment primary key,
    `name` varchar(50) not null,
    `passward` varchar(100) not null,
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
)

cur.execute("SELECT * FROM " + table + ";")
results = cur.fetchall()
print("全て表示")
print(results)
print("\n")

#同じ名前のユーザーを調べる
users=[]
search = ('SELECT * FROM ' + table + ';')
allSearch = cur.execute(search)
#print(allSearch)
result_users = cur.fetchall()
for i in range(allSearch):
    users.append(result_users[i][1])
#print(users)


#testdata = ("b", "b@mail.com", "test", now(), now())


#データの追加
judge_user = 0
usern = 'b'
userm = 'b@mail.com'
userp = 'test'
#insert="INSERT INTO " + table + " " + status + " VALUES ('b', 'b@mail.com', 'test', now(), now());"
for i in users:
    if i == usern:
        judge_user = 1

if judge_user != 1:
    insert="INSERT INTO " + table + " " + status + " VALUES ('" + usern + "', '" + userm + "', '" + userp + "', now(), now());"
#insert="INSERT INTO " + table + " " + status + " VALUES " + testdata + ";"
    cur.execute(insert)
    cnct.commit()
else:
    print('exist')
#データベースに加えた変更を保存

#データの取得・表示
cur.execute("SELECT * FROM " + table + ";")
results = cur.fetchall()
#print("全て表示")
#print(results)
#print("\n")

print("1行ずつ表示")
for r in results:
    print(r) # r は配列なので，要素単位で表示する場合はインデックスを指定すれば良い．例：print(r[0])

#データの削除
delete = "DELETE FROM " + TABLE + ";"
cur.execute(delete) #全データ削除．削除データを指定する場合は，WHERE句で指定
cnct.commit()   #データベースに加えた変更を保存

#print("\n") #2行改行する．1行だけ改行する場合は print() と指定


#データの取得・表示
cur.execute("SELECT * FROM " + TABLE + ";")
results = cur.fetchall()
if results:
    print("データあり")
    print(results)
else:
    print("データなし")


#---------
# 切断
#---------

cur.close()
cnct.close()

""" ターミナルでMySQL操作

MySQLの起動
$ mysql.server start

MySQL接続
$ mysql -u root

MySQLの終了
$ mysql.server stop


'''
