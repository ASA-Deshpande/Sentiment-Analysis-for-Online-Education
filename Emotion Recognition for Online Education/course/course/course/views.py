from copyreg import pickle
from django.http import HttpResponse
from fer import FER
import matplotlib.pyplot as plt
import pickle 

from django.shortcuts import render


def frontpage(request):
    return render(request, 'frontpage.html')

def model(request):
    if request.method == "POST":
        image=request.FILES['img']
        test_image_one = plt.imread(image)
        emo_detector = FER(mtcnn=True)

        #pickle.dump(emo_detector, open('model.pkl', 'wb'))


        # Capture all the emotions on the image
        captured_emotions = emo_detector.detect_emotions(test_image_one)
        # Print all captured emotions with the image
        # print(captured_emotions)
        plt.imshow(test_image_one)

        # Use the top Emotion() function to call for the dominant emotion in the image
        dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
        print(dominant_emotion, emotion_score)
        return render(request, 'frontpage.html', {'d':dominant_emotion,'e':emotion_score})
    return HttpResponse('None')
