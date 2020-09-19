from app import create_app
from routes import init_routes

app = create_app()
init_routes(app)


def main():
    app.run()


if __name__ == '__main__':
    main()
