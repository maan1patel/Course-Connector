# **CourseConnector**

## **Overview**
CourseConnector is a personalized learning platform designed to enhance the academic experience of university students by offering tailored resources based on their courses and professors. The platform integrates study materials, collaborative study groups, and peer tutoring services into a single mobile application. The goal is to make learning more effective, efficient, and less stressful for students.

---

## **Features**
- **Course-Specific Resources**: Access study materials tailored to your courses and professors.
- **Collaborative Study Groups**: Join or create study groups to connect with classmates.
- **Peer Tutoring Services**: Schedule and manage tutoring sessions with peer tutors.
- **Interactive Tools**:
  - Flashcards and quizzes.
  - Integrated academic calendar.
- **Offline Support**: Access resources even without an internet connection.
- **Additional Tools**:
  - Academic performance tracker.
  - Notes collaboration and textbook exchange platform.
  - Discussion boards and document rating system.

---

## **Architecture**
The project follows a modular structure with clear separation of concerns:
1. **User Management**: Handles authentication, profile updates, and session tracking.
2. **Study Material Management**: Upload, validate, store, and retrieve course-related resources.
3. **Tutoring Management**: Book, confirm, and process payments for tutoring sessions.
4. **Study Group Management**: Facilitate group coordination and collaboration.

---
## **Collaborators**
Hemil Patel: https://github.com/hemilpatel8182
Maan Patel: https://github.com/maan1patel
---

## **System Design**
### **Diagrams**
The system design is supported by the following diagrams:

1. **Use-Case Diagram**:
   - Demonstrates interactions between Students, Tutors, Admins, and the system.
2. **Class Diagram**:
   - Defines system entities like User, Tutor, Student, Course, StudyGroup, and their relationships.
3. **Data Flow Diagrams**:
   - **Level 0**: High-level overview of system processes.
   - **Level 1**: Detailed breakdown of major processes (e.g., user management, study material, tutoring).
   - **Level 2**: Focused diagrams for Study Material Management and Tutoring Management.
4. **Sequence Diagrams**:
   - Study Material Upload: Upload and validation workflow.
   - Tutoring Session: Booking and payment process.
   - User Authentication: Login and validation flow.

---

## **Tech Stack**
### **Front-End**
- React Native: For seamless mobile app development (iOS & Android).
- HTML/CSS/JavaScript: UI/UX enhancements.

### **Back-End**
- Node.js: Server-side scripting and API handling.
- Firebase: User authentication and real-time database for sessions.

### **Database**
- MongoDB: For storing user profiles, study materials, and session data.

### **APIs**
- Integrated third-party APIs for:
  - Academic schedules and grading systems.
  - Document sharing and collaboration tools.

### **Collaboration Tools**
- GitHub: Version control.
- Trello: Task management.
- Slack: Team communication.

---
