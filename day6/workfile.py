# print(dir(open))

# try:
#     f = open(r'/home/remvord/shara/DOKI/proxmox', 'r', 1024)
#     for r in f:
#         print(r)
# except Exception as e:
#     print(e)
# finally:
#     f.close()


# with open(r'/home/remvord/shara/DOKI/proxmox', 'r', 1024) as f:
#     # print(f.name)
#     for r in f:
#         print(r)

try:
    fc = open(r'/home/remvord/shara/DOKI/1.jpg', 'wb')
    with open(r'/home/remvord/shara/DOKI/1.png', 'rb') as f:
        for r in f:
            # print(r)
            fc.write(r)
finally:
    fc.close()
with open(r'/home/remvord/shara/DOKI/1.jpg', 'wb') as f:
    f.seek(100)
    f.write(b'1')
    f.seek(-96, 2)
    f.write(b'1')
    pass