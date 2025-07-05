# Bubble Pop Game

## Project Overview

This [project](https://github.com/mechahuman/Full-Stack---Bubble-Game) is a dynamic and engaging web-based game designed to entertain players with simple yet addictive gameplay. The objective is straightforward: players pop colorful bubbles to accumulate points within a 60-second time frame. Built with a modern tech stack and a clean interface, the game ensures a responsive, enjoyable experience across devices.

---

## Core Concept

Upon launching the game, users register with a unique username. Bubbles rise from the bottom of the screen at varying speeds, sizes, and colors. Players must click the bubbles to pop them, earning points for each successful hit. The game tracks each user’s high score, encouraging competitiveness and replayability.

---

## Key Features

### User Management
- Username registration with validation.
- Unique user identification.
- Persistent user profiles and high score tracking.

### Game Mechanics
- Real-time bubble generation with randomized:
  - Sizes (30–60 pixels)
  - Colors (10 unique styles)
  - Speeds (2–4 pixels/frame)
- CSS-powered smooth motion animations.
- Real-time score tracking and 60-second countdown timer.

### Score System
- Score updates on each bubble pop.
- Backend validation and high score comparison.
- Leaderboard generation with MongoDB integration.

### Frontend Functionality
- Responsive and intuitive UI.
- Score and timer display.
- Visual feedback on user actions.
- Error message handling and controls for starting/resetting.

### Backend Functionality
- Flask-powered server-side logic.
- RESTful API with endpoints for:
  - `/api/register/`
  - `/api/update-highscore/`
  - `/api/player/<username>/`
  - `/api/all/`
- CORS handling, request validation, and error management.

---

## Technical Architecture

### Frontend
- **HTML5**: Structural layout of the game interface.
- **CSS3**: Styling, layout, and animations.
- **JavaScript**: Game logic and client-side interaction.
- **Fetch API**: Communicates with the backend for data transfer.

### Backend
- **Python**: Main language for server-side operations.
- **Flask**: Web framework for building RESTful APIs.
- **MongoDB**: NoSQL database for storing player data and scores.
- **PyMongo**: Python driver for MongoDB operations.

### Tools and Platforms
- Visual Studio Code (Development Environment)
- Git (Version Control)
- MongoDB Compass (Database UI)
- Python Virtual Environment (Dependency Isolation)

---

## Data Flow Summary

1. **Player Registration**:
   - Frontend collects username and sends it to the backend.
   - Backend stores the new player profile in MongoDB.

2. **Gameplay**:
   - Frontend manages timer and score.
   - After 60 seconds, the score is submitted to the backend.
   - Backend compares and updates high score in the database.

3. **Score Retrieval**:
   - Frontend requests leaderboard or individual data.
   - Backend fetches data from MongoDB and returns it via API.
   - Frontend renders the updated score data.

---

## How to Run the Game


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



---

## Snapshots

<img src="https://github.com/user-attachments/assets/90222201-23e0-4175-9b31-8358d237d337" width="600" alt="Screenshot description">


<img src="https://github.com/user-attachments/assets/c89fb831-76b1-4d43-83c1-24e2422533f0" width="600" alt="Screenshot description">


<img src="https://github.com/user-attachments/assets/f8f17b7a-7f11-4d7e-a06f-02e633c761cd" width="600" alt="Screenshot description">


<img src="https://github.com/user-attachments/assets/812b7644-83d5-4206-90fc-fd75fc0a1c43" width="600" alt="Screenshot description">


<img src="https://github.com/user-attachments/assets/0a4cc4f0-32e7-45c4-aa47-177e2d8f9fba" width="600" alt="Screenshot description">


## Conclusion

This project showcases the synergy between simple game concepts and modern web development tools. The Bubble Pop Game delivers an accessible and rewarding experience through its intuitive design and robust architecture. With scalable backend integration, responsive frontend, and a clear vision for future features, the game is well-positioned for continuous enhancement and wider adoption.

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software in accordance with the license terms provided in the `LICENSE` file.


