import sqlite3
import os
import subprocess


def videoProcesor():
    print("We are going to process your video")

    conn = create_connection("../smarttools/db.sqlite3")
    uploaded_videos = select_all_videos_pending(conn)

    for video in uploaded_videos:
        video_id = video['id']
        video_path = video['video']
        update_uploads_video_state(conn, video_id, "PROCESANDO")
        run_video_converter(video_id, video_path)
        update_uploads_video_state(conn, video_id, "FINALIZADO")

    conn.close()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def select_all_videos_pending(conn):
    try:
        conn.row_factory = sqlite3.Row
        query = "SELECT * FROM uploads_video ORDER BY created_At"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    except sqlite3.Error as error:
        print("Error: Failed retrieving uploads_videos info" + error)

    return rows


def update_uploads_video_state(conn, id, state):
    update_query = "UPDATE uploads_video SET name = " + "'" + state + "'" + " where id=" + str(id)
    try:
        conn.cursor().execute(update_query)
        conn.commit()
    except sqlite3.Error as error:
        print("Error: Failed to update upload_videos" + error)


def run_video_converter(video_id, video_path):
    os.chdir("C:\\Users\\Andres Eslava\\PycharmProjects\\smarttools\\smarttools\\media\\videos")
    in_video_name = video_path.split("/")[1]
    out_video_name = video_path.split("/")[1].split(".")[0].strip()
    os.system("ffmpeg -y -i " + in_video_name + " " + str(video_id) + "_" + out_video_name + ".mp4")
    print(os.getcwd())
    return video_id


videoProcesor()
