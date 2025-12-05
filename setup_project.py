import os

# Step 1: Create requirements.txt
with open('requirements.txt', 'w') as f:
    f.write('flask\n')

# Step 2: Create Procfile for Heroku
with open('Procfile', 'w') as f:
    f.write('web: python app.py\n')

# Step 3: Print instructions for user
print("\nProject setup complete!")
print("Next steps:")
print("1. Install Flask: pip install flask")
print("2. Run the app: python app.py")
print("3. To deploy on Heroku:")
print("   a. Install Heroku CLI")
print("   b. heroku login")
print("   c. heroku create fishmusic-mobileconfig")
print("   d. git init; git add .; git commit -m 'Initial commit'; git push heroku master")
print("4. Integrate with your website by linking or embedding the app.")
print("5. See DEPLOYMENT_GUIDE.md for full details.")
