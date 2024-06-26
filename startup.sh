#!/bin/bash

# Start the Pyrogram bot in the background
python bot.py &

# Start the Flask app in the foreground
python flask_app.py


# #!/bin/bash

# # Start the Flask app in the background
# flask run --host=0.0.0.0 --port=8080 &

# # Start the Pyrogram bot in the foreground
# python bot.py