from PIL import Image
import requests

class bimsolutions:
    def __init__(self, book, chapter, lesson, question, filename = "answer.png"):
        if book in ["alg1", "geo", "alg2"]:
            if chapter.isdigit() and question.isdigit():
                if (lesson == "cr") or (int(chapter) >= 0 and int(lesson) >= 0 and int(question) >= 0):
                    self.chapter = int(chapter)
                    if lesson == "cr":
                        self.lesson = "cr"
                    else:
                        self.lesson = int(lesson)
                    self.question = int(question)
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
                        new_width = width + 50
                        new_height = height + 50
                        new_image = Image.new("RGBA", (new_width, new_height), "WHITE")
                        new_image.paste(image, (25, 25), mask=image)
                        new_image.convert("RGB").save(filename)
                        self.answer = "Success"
                else:
                    self.answer = "Error: Invalid chapter, lesson, or question."
            else:
                self.answer = "Error: Come on, you know that they have to be numbers."
        else:
            self.answer = "Error: Book must be `alg1, geo, or alg2`"
    def __str__(self):
        return self.answer