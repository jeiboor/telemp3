settings = {
    name
    photo
    username
    tag
    hashtag
}
settings msg = {
    lock url = ''
    lock settings == enable()
    unlock settings == disable()
    unlock url = ''
}
enable()
print("lock '..url..' enabled")
disable()
print("unlock '..url..' disabled")
access settings:
    ranks:
        sudo
        owner
        momod
