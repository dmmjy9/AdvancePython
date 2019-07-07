def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk


if __name__ == '__main__':
    with open("input.txt") as f:
        for line in myreadlines(f, "{|}"):
            print(line)
