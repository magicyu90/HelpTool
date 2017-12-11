
import re  # 引入正则表达式
import docx

doc = docx.Document(
    'E:\\files\\nuctech\\Training System\\paper 1.docx')
topic_number = 1
total = 0

topic_option_regex = re.compile(
    r'(?:\([A-D]\)|\（[A-D]\）)\s?[a-zA-Z0-9_\u4e00-\u9fa5,，\s、\.《》]+')  # 可以参考

for para in doc.paragraphs:
    options = topic_option_regex.findall(para.text)
    if options:
        print('number:', topic_number, 'options:', options)
    else:
        print('None')
    total += len(options)
    if total == 4:
        total = 0
        topic_number += 1
