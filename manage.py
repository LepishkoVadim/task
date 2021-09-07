import dotenv

from task import app

dotenv.load_dotenv('.env')

if __name__ == '__main__':
    app.run()
