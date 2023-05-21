import json


def update_version(version_data, new_version, changelog):
    version_list = version_data["history_versions"]
    version_list.append({"version": new_version, "changelog": changelog})
    version_list.sort(key=lambda x: tuple(map(int, x["version"].split("."))), reverse=True)
    version_data["latest_version"] = version_list[0]
    return version_data


def delete_version(version_data, version_to_delete):
    version_list = version_data["history_versions"]
    version_list = [v for v in version_list if v["version"] != version_to_delete]
    version_list.sort(key=lambda x: tuple(map(int, x["version"].split("."))), reverse=True)
    if not version_list:
        version_data["latest_version"] = {}
        version_data["history_versions"] = []
    else:
        if version_to_delete == version_data["latest_version"]["version"]:
            version_data["latest_version"] = version_list[0]
        version_data["history_versions"] = version_list
    return version_data


def generate_version_data():
    try:
        with open("versions.json", "r", encoding='utf-8') as file:
            version_data = json.load(file)
    except FileNotFoundError:
        version_data = {"latest_version": {}, "history_versions": []}

    while True:
        print("\n请选择要执行的操作：")
        print("1. 添加版本")
        print("2. 删除版本")
        print("3. 退出")

        choice = input("输入选项编号: ")

        if choice == "1":
            new_version = input("请输入新版本号（格式为 [int].[int].[int]）: ")
            changelog = input("请输入更新日志(空则从input.txt读取): ")
            # 如果填入的更新日志为空，就从"input.txt"中读取
            if not changelog:
                with open("input.txt", "r", encoding='utf-8') as file:
                    changelog = file.read()
            version_data = update_version(version_data, new_version, changelog)
            print("已添加新版本。")
        elif choice == "2":
            version_to_delete = input("请输入要删除的版本号: ")
            version_data = delete_version(version_data, version_to_delete)
            print("已删除指定版本。")
        elif choice == "3":
            break
        else:
            print("无效的选项，请重新输入。")

    with open("versions.json", "w") as file:
        json.dump(version_data, file, indent=4)

    print("操作完成。")


# 程序入口函数
if __name__ == "__main__":
    generate_version_data()
