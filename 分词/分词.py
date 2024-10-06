import re
# 这个代码只是进行简单的测试，只是去除了一些多余的空格符，标点符号并没有进行去除
def clean_text(text):
    # 去除多余空白
    text = ' '.join(text.split())
    # 去除换行符
    text = text.replace('\n', ' ')
    # 去除多余的空格
    text = re.sub(r'\s+', ' ', text)
    return text

def process_file(input_file_path, output_file_path):
    # 读取文件
    with open(input_file_path, 'r', encoding='utf-8') as file:
        raw_text = file.read()
    
    # 清理文本
    cleaned_text = clean_text(raw_text)
    
    # 保存清理后的文本
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

# 指定输入和输出文件路径
input_file_path = r'霸王别姬.txt'  # 替换为你的输入文件路径
output_file_path = r'output.txt'  # 替换为你希望保存的输出文件路径

process_file(input_file_path, output_file_path)

print("文本清理完成，清理后的文本已保存到输出文件。")
