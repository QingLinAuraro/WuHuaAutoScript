"""通用任务运行器：连接模拟器 → 加载资源 → 跑指定入口节点
用法: python tools/run_task.py <入口节点名>
"""
import sys
from maa.toolkit import Toolkit
from maa.controller import AdbController
from maa.resource import Resource
from maa.tasker import Tasker

entry = sys.argv[1] if len(sys.argv) > 1 else "startup_dispatch"

# 1. 初始化 + 连接（和测试脚本一样）
Toolkit.init_option("./deps")
devices = Toolkit.find_adb_devices()
if not devices:
    raise RuntimeError("没找到设备")
d = devices[0]
controller = AdbController(d.adb_path, d.address,
                           d.screencap_methods, d.input_methods, d.config)
controller.post_connection().wait()

# 2. 加载资源包（pipeline + 模板图 + OCR模型，全在这个目录）
resource = Resource()
resource.post_bundle("./assets/resource").wait()

# 3. 组装 Tasker 并跑任务
tasker = Tasker()
if not tasker.bind(resource, controller):
    raise RuntimeError("Tasker 绑定失败")

print(f"开始执行任务: {entry}")
task = tasker.post_task(entry).wait()
print(f"任务结束, 状态: {task.status}")