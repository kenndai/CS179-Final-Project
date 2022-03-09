from log import log

def op_log(message):
    log(message)

def load_log(weight):
    log(f"Container with weight: {weight}kg loaded")

def offload_log(container):
    log(f"Container: '{container}' offloaded")

def finish_log(key):
    log(f"Finished a cycle. Pop-up reminder shown to download and send out outbound manifest")

def download_log(manifest_name):
    log(f"Outbound manifest: {manifest_name} downloaded")

def balance_log(key):
    log(f"Ship is balanced")


post_dict = {
    "operator-log-entry": op_log,
    "weight-entry": load_log,
    # NAME INPUT "container-offload" WHEN FORM IS CREATED
    "container-offload": offload_log,
    "finish-cycle": finish_log,
    # NAME INPUT "download-manifest" WHEN FORM IS CREATED
    "download-manifest": download_log,
    "balanced-ship": balance_log
}