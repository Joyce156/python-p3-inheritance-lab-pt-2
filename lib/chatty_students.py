from student import Student

class ChattyStudent(Student):
    def hello(self):
        # Call the parent's hello() method
        super().hello()
        # Add the chatty extra dialogue
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        # Call super() ten times
        for _ in range(10):
            super().raise_hand()
