using System;
using System.Data.SQLite;
namespace DbConnection
{
    class Program
    {
        static void Main(string[] args)
        {
            SQLiteConnection sqlite_conn;
            sqlite_conn = CreateConnection();
            CreateTable(sqlite_conn);
            InsertData(sqlite_conn);
            ReadData(sqlite_conn);
        }
        static SQLiteConnection CreateConnection()
        {
            SQLiteConnection sqlite_conn;

            // Create a new database connection:
            sqlite_conn = new SQLiteConnection("Data Source=database.db;Version=3;New=True;Compress=True;");
            // Open the connection:
            try
            {
                sqlite_conn.Open();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
            return sqlite_conn;
        }
        static void CreateTable(SQLiteConnection conn)
        {
            SQLiteCommand sqlite_cmd;
            string createPersonTable = "CREATE TABLE Person(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,lastName TEXT,SSN_ID INT,FOREINGN KEY  (SSN_ID) REFERENCES SSN(id))";
            string createSSNTable = "CREATE TABLE SSN      (id INTEGER PRIMARY KEY AUTOINCREMENT,number INT,person_id INT,FOREINGN KEY (person_id) REFERENCES Person(id))";
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = createPersonTable;
            sqlite_cmd.ExecuteNonQuery();
            sqlite_cmd.CommandText = createSSNTable;
            sqlite_cmd.ExecuteNonQuery();
            var result = sqlite_cmd.ExecuteNonQuery();
            Console.WriteLine("Rows Added : {0}", result);
            Console.ReadLine();
        }

        static void InsertData(SQLiteConnection conn)
        {
            SQLiteCommand sqlite_cmd;
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = @"INSERT INTO Person (name, lastName, SSN_id) 
                                       VALUES ('John', 'Jonson', NULL);";
            sqlite_cmd.ExecuteNonQuery();
            sqlite_cmd.CommandText = @"INSERT INTO SSN(number, Person_id)
                                       VALUES (151564, 1);";
            sqlite_cmd.ExecuteNonQuery();
        }
        static void ReadData(SQLiteConnection conn)
        {
            SQLiteDataReader sqlite_datareader;
            SQLiteCommand sqlite_cmd;
            sqlite_cmd = conn.CreateCommand();
            sqlite_cmd.CommandText = "SELECT * FROM Person";
            
            sqlite_datareader = sqlite_cmd.ExecuteReader();
            while (sqlite_datareader.Read())
            {
                string myreader = sqlite_datareader.GetString(0);
                Console.WriteLine(myreader);
            }
            sqlite_cmd.CommandText = "SELECT * FROM SSN";
            sqlite_datareader = sqlite_cmd.ExecuteReader();
            while (sqlite_datareader.Read())
            {
                string myreader = sqlite_datareader.GetString(1);
                Console.WriteLine(myreader);
            }
            conn.Close();
        }
    }
}