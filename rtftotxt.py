import docx
import glob

for i in range(1, 3):
    for file in glob.glob("blog{}/*.rtf".format(i)):
        filename = file[6:-4]
        print(filename)
        doc = docx.Document(file)
        all_paras = doc.paragraphs
        filename = "blog-text{}/"+filename+".txt"
        with open(filename.format(i), "w", encoding="utf-8") as f:
            for para in all_paras:
                f.write(str(para.text))
