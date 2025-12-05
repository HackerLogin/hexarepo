import subprocess
import os

def stop():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    last_path = os.path.join(base_dir, ".last_container")

    if not os.path.exists(last_path):
        print("종료할 컨테이너 정보가 없습니다.")
        return

    with open(last_path, encoding="utf-8") as f:
        container_name = f.read().strip()

    if not container_name:
        print("컨테이너 이름이 비어 있습니다.")
        return

    subprocess.run(["docker", "stop", container_name])
    subprocess.run(["docker", "rm -f", container_name])

    print(f"{container_name} 컨테이너 종료 및 삭제 완료")

if __name__ == "__main__":
    stop()
