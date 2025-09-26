import sys, json

def read_json():
    raw = sys.stdin.read()
    return json.loads(raw) if raw.strip() else {}

def write_json(obj, exitcode=0):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False))
    sys.stdout.flush()
    sys.exit(exitcode)

def fail(msg, code=1):
    write_json({"ok": False, "error": str(msg)}, exitcode=code)
