import instaloader

ig = instaloader.Instaloader()
username = input("Enter Insta username : ")

ig.download_profile(username)
