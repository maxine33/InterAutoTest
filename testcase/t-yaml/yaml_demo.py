# encoding=utf-8
import yaml
from utils.YamlUtil import YamlReader

# with open("./data.yml", "r", encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)
res = YamlReader("./data.yml").get_data_all()
print(res)
