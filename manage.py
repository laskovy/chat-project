from project.settings import project


app = project
def main():
    try:
        project.run(debug=True)
    except Exception as error:
        print("Error")

if __name__ == "__main__":
    main()