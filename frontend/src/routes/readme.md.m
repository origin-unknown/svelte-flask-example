# Svelte + Flask

A super simple example of using Flask to serve a Svelte app and use it as a backend server.
This example simply queries and displays data from a database table on the Flask server.

## Install the dependencies and run or build the frontend
```bash
cd frontend 
npm install
npm run dev
# or 
npm run build 
```

## Install the dependencies and run the backend
```bash
cd backend
python3 -m venv . && source bin/activate
pip install -r requirements.txt
flask --app src/app.py --debug run 
```

The example is designed so that the Svelte application can be served via the Flask server when the `npm run build` command is finally executed. However, it can also be accessed during the development process via the two separately running servers of Flask and Svelte.