import json

import pyecharts


def study_json():
    """
    学习使用json模块处理json数据
    如果有中文，可以在转换时添加一个参数为ensure_ascii=False
    :return:
    """
    data = [
        {"name": "zhangsan", "age": 18, "address": "北京市"},
        {"name": "lisi", "age": 20, "address": "北京市"},
        {"name": "wangwu", "age": 17, "address": "北京市"},
        {"name": "zhaoliu", "age": 23, "address": "北京市"}
        ]

    # 使用json.dumps()方法可以将python的字典数据转换成json数据
    json_data = json.dumps(data, ensure_ascii=False)

    print(json_data)

    print(type(json_data))

    # 使用json.loads() 可以将json数据转换成python的数据类型
    dict_data = json.loads(json_data)

    print(dict_data)
    print(type(dict_data))


def study_echarts():
    """
    学习pyecharts模块

    pyecharts模块中有很多配置项，常用的2个类别的选项
        - 全局配置选项
        - 系列配置选项

    全局配置选项：
        - 配置图表的标题
        - 配置图例
        - 配置鼠标移动效果
        - 配置工具栏
        - 等整体配置项
    :return:
    """
    line = pyecharts.charts.Line()
    line.set_global_opts(
        title_opts=pyecharts.options.TitleOpts(title_target="测试标题", pos_left="center", pos_bottom="1%"),
        legend_opts=pyecharts.options.LegendOpts(pos_left="left", pos_bottom="1%"),
        toolbox_opts=pyecharts.options.ToolboxOpts(is_show=True),
        visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True),
        tooltip_opts=pyecharts.options.TooltipOpts(is_show=True)
    )
    line.add_xaxis(["中国", "美国", "英国"])
    line.add_yaxis("GDP", ["500", "1000", "1500"])

    line.render()

    print("生成成功")


if __name__ == '__main__':

    study_echarts()
