if sudo ban = {
    user_ban(rm_block)
    print('User has been banned')
}
if owner ban = {
    user_ban(rm_block)
    print('user has been banned')
}
if momod ban = {
    user_ban(rm_block)
    print('user has been banned')
}
if sudo_owner_momod kick = {
    user_kick(rm_remove)
    print('User has been kicked')
}
usage = {
    [ban](!/#)
    [kick](!/#)
}
patterns = {
    '..useage..'
}
