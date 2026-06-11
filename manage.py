from project.settings import project, socketio


def main():
    try:
        socketio.run(project, debug=True)
    except Exception as error:
        print("Error", error)

if __name__ == "__main__":
    main()