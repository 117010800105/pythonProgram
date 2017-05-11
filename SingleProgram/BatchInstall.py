import os
libs={"numpy","matplotlib","pillow","sklearn","requests",\
      "jieba","beautifulsoup4","wheel","networkx","sympy",\
      "django","flask","werobot","PyQt5",\
      "pandas","pyopeng1","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Sucessful")
except:
    print("Failed Somehow")
      
