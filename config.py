global token, default_music_volume, moderator_roles, bot_admin_id, max_queue_size  # NO TOUCH THIS LINE

token = ''  # Bot Login Token (String, Between ''s)

default_music_volume = 0.4  # Between 0.0 and 1.0 (Integer) Default: 0.4

max_queue_size = 0  # Maximum number of songs in the queue, 0 if infinite (Integer) Default: 0
# NOTE Queueing music currently does not work due to limitations of how the music function was written

bot_admin_id = 467470594619867158  # Discord user id of main bot admin (Integer) Probably your ID

moderator_roles = [  # List of names of the moderator roles for the bot (These have permission to load and unload cogs)
    'moderator',
    'moderators',
    'admin',
    'admins',
    'administrator',
    'administrators'
]