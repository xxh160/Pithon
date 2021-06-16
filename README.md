# pithon

南大双创嵌入式应用大作业。

实验报告见 doc/report.md。

## func

- 红外遥控
- 蜂鸣器
- LED
- 超声波自动避障

## usage

安装 [RPi.GPIO](https://github.com/yfang1644/RPi.GPIO.git) 库，以及 [rpi_ws281x](https://github.com/yfang1644/rpi_ws281x) 库。

下载源码到树莓派，进入到根目录，运行：

```python
python3 app.py
```

而后使用红外遥控控制。

具体用法见实验报告。
