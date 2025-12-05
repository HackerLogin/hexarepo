import subprocess

def stop():
    name = "test_challenge"
    subprocess.run(["docker", "stop", name])
    subprocess.run(["docker", "rm", name])
    print("컨테이너 종료 및 삭제 완료")

if __name__ == "__main__":
    stop()
