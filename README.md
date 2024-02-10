# midi playground
bouncing square video, FOSS edition (and gamified)

## development guide

this is how you set up the code to run it from source, rather than a bundled pyinstaller executable

download python from [here](https://python.org) specifically (3.9.1 should work). do not download from windows store. that version is really janky and doesn't work that well for more complex python programs with lots of dependencies

install requirements with `python3 -m pip install -r requirements.txt`

start program with `python3 main.py`

if you are going to contribute, it would be really cool if you completed items on the todo list (see below for link)

build command: `pyinstaller main.py --noconsole --onefile --clean --hidden-import glcontext`

## how to do custom songs now?

see [docs/SONGS.md](https://github.com/Spring-Forever-with-me/midi-playground/blob/master/docs/SONGS.md) for custom song tutorial

## credits

see [docs/CREDITS.md](https://github.com/Spring-Forever-with-me/midi-playground/blob/master/docs/CREDITS.md)

## contributors

- [quasar098](https://github.com/quasar098)
- [TheCodingCrafter](https://github.com/TheCodingCrafter) - Themes + QOL
- [PurpleJuiceBox](https://github.com/PurpleJuiceBox) - Reset to Default Button
- [sled45](https://github.com/sled45) - Mouse fix for high DPI displays
- [Times0](https://github.com/Times0) - `dark-modern` theme, Glowing, Colored pegs on bounce

## todo

see [docs/TODO.md](https://github.com/Spring-Forever-with-me/midi-playground/blob/master/docs/TODO.md)

###

# 中文版
0. **我本人对该项目的一些建议（有学业缠身不好深入改进，下次再来这里（指github）都不知多久了,有时间的情况下还是愿意来改进这个项目，所以东西先fork在本地了，不急着上传麻烦别人，有要求尽管提OrzOrz）：**
   - 地图每次进入需要重新生成，考虑生成一次（其他设置不变时）写入缓存。
   - 全屏运行造成了低性能电脑的卡顿，得增加窗口模式。（我尝试用ChatGPT写了一个resolution的设置项，然而并没有什么用。）
   - 设置页面的设置相当不明了。
   - 需要新手教程，再者判定失误的方式令人困惑。
   - 音画有时不同步。可以考虑绑定一下小球的碰撞事件。
   - 当前的语言嵌入比较难做，这也是为什么我做了翻译但是不想提交（有字体，显示方式等等问题存在，我对于中文的显示是暴力将所有字符全指向了微软雅黑，结果就是程序并不优雅，只能跑，这个方式在未来不好维护的）。
   - 同时提醒作者有人正在拿着此开源项目谋取利益。
1. **项目概述：**
   - 项目名称为 "MIDI Playground"，是一个跳跃方块视频的自由开源软件版本，并被游戏化。
  
2. **开发指南：**
   - 从源代码运行程序的设置方式：
     - 下载 Python（建议版本 3.9.1）[链接](https://python.org)，不要从 Windows 商店下载，因为那个版本可能对具有许多依赖项的更复杂的 Python 程序效果不佳。
     - 使用命令 `python3 -m pip install -r requirements.txt` 安装依赖。
     - 使用命令 `python3 main.py` 启动程序。
     - 贡献者可以查看待办事项列表，并完成相应的任务。

3. **构建命令：**
   - 构建命令为 `pyinstaller main.py --noconsole --onefile --clean --hidden-import glcontext`。

4. **如何添加自定义歌曲：**
   - 查看 [docs/SONGS.md](https://github.com/Spring-Forever-with-me/midi-playground/blob/master/docs/SONGS.md) 中的自定义歌曲教程。

5. **致谢：**
   - 查看 [docs/CREDITS.md](https://github.com/Spring-Forever-with-me/midi-playground/blob/master/docs/CREDITS.md) 获取感谢列表，包括贡献者的信息。

6. **贡献者：**
   - 列出了一些贡献者的信息，包括他们的 GitHub 链接。

7. **待办事项：**
   - 待办事项列表位于 [docs/TODO.md](https://github.com/Spring-Forever-with-me/midi-playground/blob/master/docs/TODO.md)。

如果你有特定的问题或需要更详细的信息，请告诉我。
