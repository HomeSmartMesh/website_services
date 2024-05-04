from utils import mqtt_client as mc
import threading
import subprocess
import os
from os.path import join
import state

def markdown_builder(topic,payload):
    print("markdown builder")
    mc.publish("markdown/confirmation",{"build":payload})
    if("resource" in payload):
        resource = payload["resource"]
        path = payload.get("path")
        thread = threading.Thread(target=build_website,args=(resource,path))
        thread.start()
    return

def build_website(resource,path):
    try:
        if(path is None):
            path = state.resources[resource]["path"]
            if(resource not in state.resources):
                mc.publish("markdown/error", {
                    "error": f"resource not found",
                    "resource": resource
                    })
                return
        original_dir = os.getcwd()
        os.chdir("/builder")
        os.environ['OUT_DIR']       = f'/web/{resource}'
        os.environ['PUBLIC_BASE']   = ''
        os.environ['STRUCTURE']     = f'/process/{resource}/structure'
        os.environ['CONTENT']       = path
        subprocess.run("pnpm run build", shell=True, check=True)
        os.chdir(original_dir)

        mc.publish("markdown/completion", resource)
    except Exception as e:
        print(f"unhandled exception {e}")
        mc.publish("markdown/error", {"error": str(e)})
        return

def update_resource(topic,payload):
    id = topic.split("/")[2]
    state.resources[id] = payload
    return

mc.add_action("markdown/build",markdown_builder)
mc.add_action("fetcher/resources/#",update_resource)
mc.start()
