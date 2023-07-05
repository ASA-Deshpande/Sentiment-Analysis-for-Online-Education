
# Sentiment Analysis for Online Education

## Project done in Second Year as part of the Software Engineering course, following all Agile Practices
Emotion is one of the very few words in the English language that does not have a concrete definition. Yet, almost every decision we have ever made in our lives is driven by emotion. This project proposes Face Emotion Recognition (FER) model to extract and classify the emotions from an image. This can further be used to analyse the satisfaction levels of students learning remotely using online tools.

With the onslaught of the Covid-19 pandemic, digital education has become a central concept. Using video conferencing on platforms like Google Meet and Zoom has become the norm. However, due to the disconnected nature of online teaching, as well as network issues, which disrupted the flow of the conference, it is difficult for teachers to assess students' satisfaction with a particular lecture and find out their emotions accurately, which is not the case with direct education as one can only assess facial features in real time. We propose to address this issue. 
The benefits of online education are numerous, including the possibility to rewatch recorded lectures, outreach of the sessions, affordability, and a quieter option in general for all introverts out there. To make the online education system more robust, we put forth a way to get student feedback for a session. Faculty members can upload photos of students during a certain lecture, and categorize their feelings into one of three classes- satisfied, neutral and dissatisfied. Then the overall percentage of satisfied pupils can be calculated and 
appropriate strategies can be employed to improve    the satisfaction levels.

### Methodology

1.	A Machine Learning algorithm appropriate for our  project was picked.
2.	Then, we built the ML model in order to recognize these students emotional states using their facial expressions in image format.
3.	This model is created using FER library that tests certain markers in the image to classify their emotions into different categories.
4.	Then, we created the User Interface in form of a website. Our User Interface contains a Home page with introduction, About us, Contact section and Footer. It also contains Login and Sign-up activity which is authenticated using Firebase. Then we move to the subject section and select our class, upload the images and get the required classification result.
5.	The entire UI is created using HTML, CSS, JavaScript, and Node.js.
6.	Finally, we deployed the machine learning algorithm into our website using Flask to create a fully functional system.


### System Requirement Specification

•	Functional Requirements:
1.	The website will be able to create accounts for new users or log in existing ones.
2.	After logging in, faculty accounts would be able to upload photos of a certain lecture and calculate satisfaction level.
3.	Faculty can view their previous performances for a particular subject.
4.	The university accounts can fetch previous data about a faculty to make appropriate decisions.
   
•	Non-functional Requirements:
1.	System should have minimum Response time.
2.	System User Interface should be easy to use.
3.	Data-retrieval must be smooth and consistent.
4.	System shouldn't crash when accessed by multiple users.
5.	System should be secure.
   
•	System Requirements:
1.	Must be cross-platform, running across a wide variety of Operating System.
2.	Must run smoothly on all types of devices.
3.	Requires proper internet connectivity to access.

### Product Backlog

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/0a6ca4b6-f4db-4dc6-a422-4e803407907b)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/92fc9665-f72e-4f7c-b479-842c51b2422a)

 


 


VI. Sprint Planning

Sprint 1: 
Creation of Machine learning model that accepts image input and outputs a particular class for the image from the three classes.
Duration: 1 week [Estimate]
 
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/beff1d86-eab4-43b5-bddf-4699a2ecc131)

Sprint 2: 
Creation of the frontend and backend for the website
Duration: 2 weeks [Estimate]
 
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/85ecce0d-2533-4099-beae-309bf3abc6e2)

Sprint 3: 
Integration of frontend and backend and model.
Duration: 1 week [Estimate]
 
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/733788f4-0eff-40d6-8640-3e75a146a725)

Sprint 4:
Logging in for both accounts, processing and retrieving the data.
Duration: 2 weeks [Estimate]

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/65a298f5-e908-41b6-9337-19162f5a3ecc)

Sprint 5: New features.
Duration: Undetermined.
 
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/b09be0c6-f2ce-4327-ad03-7b02a87e8764)


### UML Diagrams
#### Class diagram:
Class diagrams are the most popular UML diagrams which are used for construction of software applications. Class diagram is a graphical representation of the static view of the system representing different aspects of the application. We Have multiple classes associated with our website and each class also has different methods for better functioning and performance of our website.

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/c8f5eb59-412f-49fa-9f41-4185b8210137)

#### Use Case Diagram:
The use case diagram represents the dynamic behavior of a system. Before starting with drawing a use case diagram it is essential to analyze the whole system. It shows the users associated with our website. For now, we have three different users on our website i.e., Student, Teacher and Administration to manage the interface.

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/cd6f85f7-693d-4cbb-b150-8798c6858f03)
        
#### Activity Diagram:
An activity diagram is a behavioral diagram i.e., it depicts the behavior of a system. The following activity diagram portrays the control flow from a start point to a finish point showing the various decision paths that exist while our project is being executed.

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/ddd6deba-637c-4259-b1f3-4219715d3e0f)

#### Sequence Diagram:
A sequence diagram shows process interactions arranged in time sequence. For a particular scenario of a use case of our project, the diagrams show the events that external actors generate, their operational order, and the possible inter-system events.

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/5e597a00-5b13-40c5-bade-d338349ce679)

### Output:

![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/7c132b70-7100-4341-bee2-9a58955b5ab9)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/61f1d663-83f7-4a92-9794-f7c88d4fa625)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/ca602c58-284b-4f32-8cfb-a4ee95ec073f)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/ee0f479f-ecaf-4d41-93ad-921e763b5fd8)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/5f628f00-dca3-4371-b3c1-30888a8afd59)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/83e523f5-7502-44e4-9276-7bbecfa03b7e)
![image](https://github.com/ASA-Deshpande/Sentiment-Analysis-for-Online-Education/assets/88822564/4193cfbb-b8c5-4ed9-9d05-7d46a5d89a52)

The website contains Home, About Us, Browse Course and Contact as the main activities on the navigation bar. User [Faculty here] can register or login into the system and browse the course for which he/she wants to see the result by uploading images. Further the user can also contact us by providing his/her name, email address ,phone number and address.
The Website is able to register new user and login the existing once. Faculty accounts are accepting images of students in online classes from a certain lecture and the satisfaction level is calculated. 


### Contributors
+ Anuja Deshpande
+ Dev Bohra
+ Samiksha Dongre
+ Eeshan Umrani


