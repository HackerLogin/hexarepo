import subprocess
import random
import re
import os

# 포트 범위
MIN_PORT = 30000
MAX_PORT = 40000

def find_free_port():
    while True:
        p = random.randint(MIN_PORT, MAX_PORT)
        res = subprocess.run(["lsof", "-i", f":{p}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:  # 아무도 사용 안 하면 ok
            return p

def get_internal_port():
    content = open("Dockerfile").read()
    m = re.search(r"EXPOSE\s+(\d+)", content)
    return int(m.group(1)) if m else 5000  # 기본 5000

def deploy():
    name = "test_challenge"
    internal = get_internal_port()
    external = find_free_port()

    # build
    subprocess.run(["docker", "build", "-t", name, "."], check=True)

    # run
    subprocess.run([
        "docker", "run", "-d",
        "-p", f"{external}:{internal}",
        "--name", name,
        name
    ], check=True)

    print("자동 생성 완료")
    print(f"접속 URL: http://<서버IP>:{external}")

if __name__ == "__main__":
    deploy()
