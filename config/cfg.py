config = dict(
      milvus = dict (
            host = "localhost",
            port = "19530",
            collection_name = "face_infos",
      ),
      mysql = dict (
            host = "localhost",
            port = "3306",
            user = "root",
            pwd = "123456",
            dbname = "faceai",
            tables =["face_infos",],
            table = "face_infos"
      ),
)