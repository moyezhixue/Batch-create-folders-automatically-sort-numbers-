import os

def create_directories(base_path, prefix, count):
    # 检查路径是否存在
    if not os.path.exists(base_path):
        print(f"指定的路径不存在: {base_path}")
        return

    # 创建指定数量的文件夹
    for i in range(1, count + 1):
        # 构建完整的文件夹路径
        dir_name = f"{prefix}{i}"
        full_path = os.path.join(base_path, dir_name)
        # 尝试创建文件夹
        try:
            os.makedirs(full_path)
            print(f"创建文件夹: {full_path} 成功")
        except Exception as e:
            print(f"创建文件夹失败: {full_path}, 错误: {e}")

# 主程序
if __name__ == "__main__":
    base_path = input("请输入文件夹创建的位置: ")
    prefix = input("请输入文件夹名称前缀（支持中文）: ")
    count = int(input("请输入要创建的文件夹数量: "))

    create_directories(base_path, prefix, count)
