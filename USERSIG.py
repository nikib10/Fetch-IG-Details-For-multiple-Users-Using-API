import instaloader

import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# List of Instagram usernames
usernames = ['karpal.singh.bandral', 'work.play.sleep', '_https.niki1']

# Variable to store the total followers count
total_followers_count = 0

# Loop to fetch details for each user
for username in usernames:
    try:
        # Loading a profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, username)
        
        # Print user details
        print("\nUser Details for", username)
        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        followers_count = profile.followers
        print(f"Followers Count: {followers_count}")
        print("Following Count: ", profile.followees)
        print("Bio: ", profile.biography)
        print("External URL: ", profile.external_url)

        # Increment the total followers count
        total_followers_count += followers_count

    except instaloader.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist.")

    except Exception as e:
        print(f"Error fetching details for {username}: {str(e)}")

# Print the total followers count
print("\nTotal Followers Count for All Users:", total_followers_count)
