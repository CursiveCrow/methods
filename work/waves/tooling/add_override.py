"""Insert one typed override into a scope binding of handbook/registry/symbol-scopes.json
by minimal text insertion (keeps the file's existing formatting).
Usage: python -B work/waves/tooling/add_override.py SCOPE_NAME OVERRIDE_JSON_FILE"""
import json, sys

path = "handbook/registry/symbol-scopes.json"
scope, ov_file = sys.argv[1], sys.argv[2]
override = json.load(open(ov_file, encoding="utf-8"))
text = open(path, encoding="utf-8").read()
data = json.loads(text)
binding = data["scopes"][scope]
key = json.dumps(scope, ensure_ascii=False) + ": {"
start = text.index(key)
# find the matching closing brace of this binding object
depth, i, in_str, esc = 0, start + len(key) - 1, False, False
while True:
    c = text[i]
    if in_str:
        if esc: esc = False
        elif c == "\\": esc = True
        elif c == '"': in_str = False
    elif c == '"': in_str = True
    elif c == "{": depth += 1
    elif c == "}":
        depth -= 1
        if depth == 0: break
    i += 1
end = i  # index of the binding's closing brace
line_start = text.rfind("\n", 0, start) + 1
indent = text[line_start:start]
inner = indent + "  "
if "overrides" in binding:
    raise SystemExit("binding already has overrides; extend manually")
ov_text = json.dumps([override], ensure_ascii=False, indent=2).replace("\n", "\n" + inner)
prefix = text[:end].rstrip()
new = prefix + ",\n" + inner + '"overrides": ' + ov_text + "\n" + indent + text[end:]
check = json.loads(new)
assert check["scopes"][scope]["overrides"] == [override]
assert {k: v for k, v in check["scopes"][scope].items() if k != "overrides"} == binding
open(path, "w", encoding="utf-8", newline="\n").write(new)
print("override added to", scope)
