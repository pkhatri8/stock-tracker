from flask_app import create_app

app = create_app()

# Required for Vercel
if __name__ == "__main__":
    app.run()
