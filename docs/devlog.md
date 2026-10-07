# 开发日志

## 2026-09-03 · 环境搭建 + 启动链跑通（Phase 0）

### 今日成果

1. **项目梳理与规划**
   - 基于 `MaaPracticeBoilerplate` 模板初始化仓库，梳理项目现状。
   - `策划案.md`（v0.2）完成：功能模块清单（D-01~S-01）、技术选型、目录规划、里程碑。

2. **环境验证**
   - MaaFramework 环境跑通，OCR 模型（MaaCommonAssets）就绪。
   - `tools/test_connection.py` 验证 ADB 连接 MuMu 模拟器 + 截图成功。
   - 采集登录到主页全流程截图 9 张（`screenshots/Screenshots/`）。

3. **素材目录搭建**
   - `assets/resource/image/` 建立 13 个分类目录（main/company/tea_room/…/common）。
   - 裁剪首批模板 4 张：`common/close_announce.png`、`common/close_signin.png`、`common/close_popup_1.png`、`loading/start.png`。

4. **Pipeline 框架**
   - 按模块建好 15 个空 pipeline 文件（common/startup/daily/weekly/activity/gacha）。

5. **启动链（login.json）开发并跑通** ✅
   - 流程：启动 → 关公告 → 点击进入游戏 → 每日签到 → 关活动/商城弹窗 → 主界面锚点。
   - 主界面锚点与签到结算用 OCR 识别，规避月份/立绘等易变元素。
   - 签到界面"九月签到"标题随月份变化 → 模板避开了标题区。

### Review 修正

- `startup_dispatch` 补 `timeout: 120000`，冷启动长加载不再超时失败。
- 调度类节点 next 顺序统一"先关弹窗、再干活"（popup_close_common 提到首位）。
- 去掉 popup.json 中重复的模板项；清理未被引用的整图与废模板。

### 踩坑记录

- Windows 控制台跑校验脚本需 `PYTHONIOENCODING=utf-8`（GBK 编不下 ✓/✗）。
- schema 校验脚本默认路径不存在，正确用法：
  `PYTHONIOENCODING=utf-8 python tools/validate_schema.py --schema-dir deps/tools --resource-dirs assets/resource`

### 待办（下次继续）

- [ ] D-01 派遣公司收取（从主界面进入 → 收取感应/资源 → 返回）
- [ ] `common/navigation.json` 通用"返回主界面"逻辑
- [ ] `interface.json` 清理模板壳子（项目名、删 Win32 controller、B 服 resource、示例任务）
- [ ] 主界面其余入口按钮模板（任务/游历/易物所/征集/执行）补齐
- [ ] 提交今日改动（当前 workspace 有未提交内容）
