s = input().strip()
ans = ""
for ch in s:
    if ch == "+":
        ans += " tighten "
    elif ch == "-":
        ans += " loosen "
    elif ans and ans[-1].isdigit() and not ch.isdigit():
        ans += "\n" + ch
    else:
        ans += ch
print(ans)

