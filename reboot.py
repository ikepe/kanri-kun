
from sqlite3 import connect
from webbrowser import get
import yaml
import paramiko

def reboot():
  # config.yamlから情報を引き出す
  with open("config.yml") as file:
    config = yaml.safe_load(file)
    ssh_ip = config["IP"]
    ssh_user = config["user"]
    #ssh_port = config["port"]
    #ssh_rhost = config["remort_host"]
    #ssh_rport = config["remort_port"]
    #ssh_lport = config["local_port"]
    ssh_command = config["CMD"]
    ssh_key = config["ssh_key"]

  # sshクライアントの作成
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.WarningPolicy())

  client.connect(ssh_ip,
                        username = ssh_user,
                        key_filename = ssh_key,
                        timeout = 5.0)

  stdin, stdout, stderr = client.exec_command(ssh_command)

  # コマンド実行結果を変数に格納
  cmd_result = ''
  for line in stdout:
      cmd_result += line

  # 実行結果を出力
  print(cmd_result)

  # ssh接続断
  client.close()
  del client, stdin, stdout, stderr
