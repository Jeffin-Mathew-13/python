feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
    ' Very GOOD Service!!!',
    'poor support, not happy ',
    'GREAT experience! will come again.',
    'okay okay...',
    ' not BAD',
    'Excellent care, excellent staff!',
    'good food and good ambience!',
    'Poor response and poor handling of issue',
    'Satisfied. But could be better.',
    'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print("Enter how many more feedbacks you want to add?")
F_no=int(input())

for i in range(F_no):
    print("Enter your name")
    F_name=input()
    print("Enter your feedback")
    F_feedback=input()
    print("Enter your rating 1-5")
    F_rating=int(input())
    feedback_data["S_No"].append(len(feedback_data["S_No"])+1)
    feedback_data["Name"].append(F_name)
    feedback_data["Feedback"].append(F_feedback)
    feedback_data["Rating"].append(F_rating)

print(feedback_data)

for i in range(0,len(feedback_data["S_No"])):
    text=feedback_data["Feedback"][i]
    text=text.replace(".","")
    text=text.replace(",","")
    text=text.replace("!","")
    text=text.replace("?","")
    text=text.replace("  "," ")

    text=" ".join(text.split())

    text=text.lower()

    feedback_data["Feedback"][i]=text


def count_word_in_feedback(word):
    count = 0
    for feedback in feedback_data["Feedback"]:
        if word.lower() in feedback.lower():
            count=count+1
    return count

print("feedback containing 'good':",count_word_in_feedback("good"))
print("feedback containing 'poor':",count_word_in_feedback("poor"))
print("feedback containing 'excellent':",count_word_in_feedback("excellent"))

print("FINAL CLEANED FEEDBACK")
print(feedback_data)

avg_r=sum(feedback_data["Rating"])/len(feedback_data["Rating"])
print("AVERAGE RATING:",avg_r)

long_f=max(feedback_data["Feedback"],key=lambda x:len(x.split()) )
print("LONGEST FEEDBACK:",long_f)
print("LENGTH OF LONGEST FEEDBACK:",len(long_f.split()))

unq=set()
for feedback in feedback_data["Feedback"]:
    word=feedback.split()
    unq.update(word)
print("UNIQUE WORDS:",unq)
