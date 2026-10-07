"""连接测试：找到 MuMu → 连接 → 截一张图保存"""
import cv2
from maa.toolkit import Toolkit
from maa.controller import AdbController

Toolkit.init_option("./deps")          # 告诉框架 dll 在哪

devices = Toolkit.find_adb_devices()   # 自动扫描 adb 设备
if not devices:
    raise RuntimeError("没找到设备，检查 adb connect 是否成功")
print(f"发现 {len(devices)} 个设备，使用第一个: {devices[0].name}")

device = devices[0]
controller = AdbController(
    adb_path=device.adb_path,
    address=device.address,
    screencap_methods=device.screencap_methods,
    input_methods=device.input_methods,
    config=device.config,
)
controller.post_connection().wait()    # 异步连接，等它完成
print("连接成功！")

image = controller.post_screencap().wait().get()   # 截图，拿到 numpy 图像
cv2.imwrite("test_screenshot.png", image)
print(f"截图已保存: test_screenshot.png, 尺寸 {image.shape[1]}x{image.shape[0]}")