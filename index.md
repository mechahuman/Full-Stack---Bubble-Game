BUBBLE GAME PROJECT
===================

What is this project?
--------------------
This is a simple bubble-popping game where players can:
- Create a username
- Pop bubbles to score points
- Save their high scores
- Play multiple times

How to run the game:
-------------------
1. Make sure MongoDB is installed and running on your computer
2. Open two terminal windows
3. In first terminal:
   - Go to backend folder: cd backend
   - Run: python app.py
4. In second terminal:
   - Go to frontend/public folder: cd frontend/public
   - Run: python -m http.server 8080
5. Open your web browser
6. Go to: http://localhost:8080

How to play:
-----------
1. Click "New User" and enter your username
2. Click "Start Game"
3. Click on bubbles to pop them and score points
4. Try to get the highest score in 60 seconds
5. Your high score will be saved automatically

Technical Stuff:
--------------
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: MongoDB
- No login needed, just enter a username and play! 
