import psycopg2

message = {
  "cabinetId": "CAB0103UK003",
  "testGroup": [
    {
      "testSuite": [
        {
          "testSuiteName": "",
          "testCase": [
            {
              "meterId": "",
              "testCaseName": "",
              "actions": ""
            }
          ]
        }
      ],
      "testGroupName": ""
    }
  ],
  "testCaseId": 93
}


conn = psycopg2.connect(
    host= "localhost",
    database="TempMsgDB",
    user = "postgres",
    password = "griffyn")

cursor = conn.cursor()

#insert query
query = """INSERT INTO temp_test_case_table(test_case_id,cabinet_id,test_group_name,test_suite_name,test_case_name,meter_id,actions) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
record =(
        message["testCaseId"],
        message["cabinetId"],
        message["testGroup"][0]["testGroupName"],
        message["testGroup"][0]["testSuite"][0]["testSuiteName"],
        message["testGroup"][0]["testSuite"][0]["testCase"][0]["testCaseName"],
        message["testGroup"][0]["testSuite"][0]["testCase"][0]["meterId"],
        message["testGroup"][0]["testSuite"][0]["testCase"][0]["actions"])

cursor.execute(query,record)
conn.commit()


#select query
query = """SELECT * FROM temp_test_case_table"""
cursor.execute(query)
rows = cursor.fetchall()
for x in rows:
    print(rows)


conn.close()