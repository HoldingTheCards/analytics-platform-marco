from prefect import flow, task
import subprocess, sys, os, time

@task
def generate_events():
    cmd = [sys.executable, "scripts/generate_synthetic_events.py", "--out", "data/events.csv", "--rows", "5000"]
    subprocess.run(cmd, check=True)

@task
def dbt_build():
    cmds = [
        ["dbt", "--version"],
        ["dbt", "build"]
    ]
    for c in cmds:
        try:
            subprocess.run(c, check=True)
        except Exception as e:
            print("Command failed:", c, e)

@flow(name="analytics_local_pipeline")
def pipeline():
    generate_events()
    dbt_build()

if __name__ == "__main__":
    pipeline()
