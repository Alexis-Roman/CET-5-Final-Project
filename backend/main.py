from website import create_ap

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)