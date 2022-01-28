from email.mime import image
from fileinput import fileno
from PIL import Image
import requests
import os

class bimsolutions:
    def __init__(self, book, chapter, lesson, question, filename = "answer.png"):
        if book in ["alg1", "geo", "alg2"]:
            if abs(int(chapter)) != int(chapter) or int(chapter) == 0:
                self.answer = "Error: Chapter must be a positive integer greater than 0."
            elif abs(int(lesson)) != int(lesson) or int(lesson) == 0:
                self.answer = "Error: Lesson must be a positive integer greater than 0."
            elif abs(int(question)) != int(question) or int(question) == 0:
                self.answer = "Error: Question must be a positive integer greater than 0."
            else:
                self.chapter = abs(int(chapter))
                self.lesson = abs(int(lesson))
                self.question = abs(int(question))
                self.answer = f"https://static.bigideasmath.com/protected/content/dc_cc_hs/apt/images/{book}/{self.chapter:02}/{self.lesson:02}/s_{book}_ex_{self.chapter:02}_{self.lesson:02}_{self.question:03}.png"
                status = 0
                with open(filename, "wb") as f:
                    r = requests.get(self.answer)
                    if r.status_code == 200:
                        f.write(r.content)
                    else:
                        self.answer = "Error: Could not download image."
                        status = 1
                if status == 0:
                    image = Image.open(filename).convert("RGBA")
                    width, height = image.size
                    new_width = width + 10
                    new_height = height + 10
                    new_image = Image.new("RGBA", (new_width, new_height), "WHITE")
                    new_image.paste(image, (5, 5), mask=image)
                    new_image.convert("RGB").save(filename)
                    self.answer = "Success"
        else:
            self.answer = "Error: Book must be alg1, geo, or alg2"
    def __str__(self):
        return self.answer