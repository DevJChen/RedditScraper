import os
import shutil

def Remove():
    username = "appetizedd"
    post_path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap"
    log_path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\config\\log"
    for filename in os.listdir(post_path):
        file_path = os.path.join(post_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    for filename in os.listdir(log_path):
        file_path = os.path.join(log_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    cookie_path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\config\\"
    os.unlink(cookie_path + username + "_uuid_and_cookie.json")
    os.unlink(cookie_path + username + ".checkpoint")
    print("Files Cleaned")
Remove()
