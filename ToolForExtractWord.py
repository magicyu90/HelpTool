"""
需要把Word里的内容进行提取：用正则，匹配 多个数字+一个‘、’为开头，中间夹杂“正确答案”关键字，再以换行符或回车为结尾的。
"""

import re  # 引入正则表达式
import docx


def extract_word():
    """
    Extract word
    """
    doc = docx.Document(
        'E:\\files\\nuctech\\Training System\\testa.docx')  # word文件
    topics = []  # 考题数组
    current_topic_number = 0  # 当前考题题号
    topic_regex = re.compile(r'\d+、')  # 题目正则表达式
    topic_option_regex = re.compile(r'\（[A-D]\）')  # 题目选项的正则表达式
    topic_option_des_regex = re.compile(
        r'(?:\([A-D]\)|\（[A-D]\）)[a-zA-Z0-9_\u4e00-\u9fa5,，\s、\.《》]+')  # 题目选线描述的正则表达式

    def get_topic_by_number(number):
        """
        根据题号筛选题目
        :type number: int
        """
        item = None
        for item in topics:
            if item['number'] == number:
                return item

    def judge_font_isred(rgb):
        """
        判断颜色是否接近红色
        """
        color = int('0x' + rgb.__str__(), 16)
        red = (color & 0xff0000) >> 16
        green = (color & 0xff00) >> 8
        blue = (color & 0xff)
        return red > green and red > blue

    for para in doc.paragraphs:
        a = topic_regex.search(para.text)
        b = topic_option_regex.search(para.text)
        if a:  # 如果有题号
            current_topic_number = int(a.group(0)[:-1])
            # 默认题目（题目类型是判断题）
            topic = {'number': current_topic_number, 'topic': '',
                     'answers': [], 'right answers': [], 'type': 'J'}
            topic['topic'] += para.text
            topics.append(topic)
            if para.runs[0].font.color.rgb != None:
                is_red = judge_font_isred(para.runs[0].font.color.rgb)
                if is_red:
                    topic['right answers'].extend("Y")
                else:
                    topic['right answers'].extend("N")
        elif b:  # 如果有选项
            # ans = [answer for answer in topic_option_regex.split(
            #     para.text) if answer != '']
            ans = topic_option_des_regex.findall(para.text)
            topic = get_topic_by_number(current_topic_number)
            if topic:
                topic['answers'].extend(ans)
            for run in para.runs:
                if run.font.color.rgb != None:
                    is_red = judge_font_isred(run.font.color.rgb)
                    if is_red and run.text in "ABCD":
                        topic = get_topic_by_number(current_topic_number)
                        if topic:
                            if 'N' in topic['right answers']:
                                topic['right answers'].remove('N')
                            if 'Y' in topic['right answers']:
                                topic['right answers'].remove('Y')
                            topic['right answers'].extend(run.text)
                            if len(topic['right answers']) > 1:
                                topic['type'] = 'M'
                            else:
                                topic['type'] = 'S'
        else:  # 题干剩余部分
            topic = get_topic_by_number(current_topic_number)
            if topic and len(topic['answers']) == 0:
                topic['topic'] += para.text

    print(topics)


if __name__ == '__main__':
    print('--------------------开始提取word--------------------')
    extract_word()
    print('--------------------提取word结束--------------------')
