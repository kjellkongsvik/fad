from uvicorn import Config, Server


def main():
    server = Server(
        Config("fad.fad:app", host="0.0.0.0", port=5000),
    )

    server.run()


if __name__ == "__main__":
    main()
