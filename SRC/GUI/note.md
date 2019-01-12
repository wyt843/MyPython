# Python GUI 编程
## 几个python GUI库
    -  Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和
       Tkinter 可以在大多数的 Unix 平台下使用,同样可以应用在 Windows 和
       Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地
       运行在绝大多数平台中。
    - wxPython wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI
      图形库，允许 Python 程序员很方便的创建完整的、功能健全的 GUI 用户界面
    - Jython：Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython
      使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的
      全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。
      Jython 可以被动态或静态地编译成 Java 字节码。
    - PyGTK Thinter的替代品
    - PyQt :跨平台、商业授权


## Tkinter 编程
    - Tkinter 是Python的标准GUI库。由于 Tkinter 是内置到 python 的安装
      包中、只要安装好 Python 之后就能 import Tkinter 库、而且 IDLE 也
      是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。
    - Tkinter 绑定的是TK GUI 工具集，用Python包装Tcl的代码
    - 组件
        - 按钮
            - Button
            - RadioButton
            - CheckButton
            - ListBox
        - 文本组件
            - Entry  单行文本
            - Text   多行文本
        - 标签组件
            - Label
            - Message
        - 菜单
            - Menu
            - MenuButton
        - 滚动条
            - scale     滑动组件
            - Scrollbar 滚动条组件
        - 其他组件
            - Canvas    画布组件
            - Frame     画框
            - Toplevel  创建子窗口组件
    - 布局
        - pack：按照方位布局,参数如下
            - side：停靠方位（LEFT、TOP、RIGHT、BOTTOM）
            - fill：填充方式 X,Y,BOTH,NONE
            - expande：YES/NO
            - widget - pack it after you have packed widget
            - anchor=NSEW (or subset) - position widget according to
                                  given direction
            - before=widget - pack it before you will pack widget
            - expand=bool - expand widget if parent size grows
            - fill=NONE or X or Y or BOTH - fill widget if widget grows
            - in=master - use master to contain this widget
            - in_=master - see 'in' option description
            - ipadx=amount - add internal padding in x direction
            - ipady=amount - add internal padding in y direction
            - padx x方向外边界
            - pady y方向外边界
            - side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        - place：按照坐标布局
            - in=master - master relative to which the widget is placed
            - x=amount 设置横向位置
            - y=amount 设置纵向位置
            - width=amount 组件宽度
            - height=amount 组件高度
            - bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
            - relx=amount - locate anchor of this widget between 0.0 and 1.0
            -               relative to width of master (1.0 is right edge)
            - rely=amount - locate anchor of this widget between 0.0 and 1.0
            -               relative to height of master (1.0 is bottom edge)
            - anchor=NSEW (or subset) - position anchor according to given direction

            - relwidth=amount - width of this widget between 0.0 and 1.0
                              relative to width of master (1.0 is the same width
                              as the master)
            - relheight=amount - height of this widget between 0.0 and 1.0
                               relative to height of master (1.0 is the same
                               height as the master)

            - 案例 02.py
        - grid： 网格布局,位置比较固定
            - 利用 row、column编号，都是从0开始
            - sticky：N/E/S/W 表示上/右/下/左
            - 参数：
                - column=number - use cell identified with given column (starting with 0)
                - columnspan=number - this widget will span several columns
                - in=master - use master to contain this widget
                - in_=master - see 'in' option description
                - ipadx=amount - add internal padding in x direction
                - ipady=amount - add internal padding in y direction
                - padx=amount - add padding in x direction
                - pady=amount - add padding in y direction
                - row=number - use cell identified with given row (starting with 0)
                - rowspan=number - this widget will span several rows
                - sticky=NSEW - if cell is larger on which sides will this
                              widget stick to the cell boundary
            - 案例03.py
## 消息机制
    - Tkinter 的绑定
        - bind_all:全局范围的绑定，默认是全局快捷键，比如F1帮助文档
        - bind_class:接受三个参数，第一个类名，第二个事件，第三个操作
            - w.bind_class("Entry", "<Control-V>", my_paste)
        - bind:单独绑定某一实例
        - unbind:解除绑定
    - Entry
        - 输入框，单一
        - Entry["show"]="*" 设置遮挡字符

## 菜单
    - 普通菜单
        - Menu 定义一个parent
        - add_command:添加菜单项，如果菜单是顶层菜单 ，从左到右添加，否则下拉
            - label：菜单显示名称
            - command: 菜单绑定单机
            - acceletor:快捷键
            - underline:指定是否有下划线（热键)
            - menu:指定顶级菜单
    - 联动菜单
        - add_cascade:联动菜单，作用是引出后续菜单
        - add_cascade 的menu属性，指明菜单级联到那个菜单上
        - label:名称
        - 过程：
            - 建立 menu
            - add_command
            - add_cascade
    - 弹出式菜单
        - 弹出菜单也叫上下文菜单
        - 实现大致思路
            - 简单菜单中添加各种功能
            - 监听鼠标右键
            - 如果右键，则根据位置判断弹出
            - 调用Menu的pop方法
        - add_separator:添加分割符
## canvas 画布
    - 画布：可以自由的在上面绘制图形
    - 在画布上绘制对象 通常用create_xxxx xxx例如:line,rectangle
    - 案例 06.py