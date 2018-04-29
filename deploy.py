#!/usr/bin/env python3
import subprocess
import deploy_keys

subprocess.run(['docker','build','-t','atube_webserver','-f','website/Dockerfile','.'])
subprocess.run(deploy_keys.docker_login_cmd)
subprocess.run(['docker', 'tag', 'atube_webserver:latest', '355023123875.dkr.ecr.us-east-1.amazonaws.com/atube_webserver:latest'])
subprocess.run(['docker', 'push', '355023123875.dkr.ecr.us-east-1.amazonaws.com/atube_webserver:latest'])
