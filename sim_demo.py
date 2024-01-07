import tkinter as tk
from tkinter import ttk

from walking_sample import walking_sim_demo
from ball_detect import ball_detect_demo

# 字体
demo_font = ('Arial', 16)



def run_visual_demo():
    print("视觉演示脚本运行中...")
    ball_detect_demo()
    

def open_main_window():
    # 关闭初始页面
    intro_window.destroy()

    # 创建主窗口
    root = tk.Tk()
    root.title("机器人课程仿真演示程序")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 768
    window_height = 400
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False)

    # 配置网格的权重
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)
    root.grid_rowconfigure(0, weight=1)

    # 按钮样式
    style = ttk.Style()
    style.configure('Custom.TButton', font=demo_font)

    # 创建运动控制部分
    motion_frame = ttk.LabelFrame(root, text="运动控制仿真")
    motion_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    # 配置运动控制部分的网格权重
    motion_frame.grid_columnconfigure(1, weight=2)
    for i in range(5):  # 假设运动控制部分有五行
        motion_frame.grid_rowconfigure(i, weight=1)
    
    # 添加说明标签
    motion_demo_label = ttk.Label(motion_frame, text="修改参数后点击“开始运行”查看效果，\n仿真延迟系数为0时最流畅", font=demo_font)
    motion_demo_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
    
    # 添加输入框和按钮
    speed_label = ttk.Label(motion_frame, text="仿真延迟系数:", font=demo_font)
    speed_label.grid(row=1, column=0, sticky=tk.W)
    speed = ttk.Entry(motion_frame, font=demo_font)
    speed.grid(row=1, column=1)
    speed.insert(0, '0.0')

    target_x_label = ttk.Label(motion_frame, text="目标X位置:", font=demo_font)
    target_x_label.grid(row=2, column=0, sticky=tk.W)
    target_x = ttk.Entry(motion_frame, font=demo_font)
    target_x.grid(row=2, column=1)
    target_x.insert(0, '1.0')

    target_y_label = ttk.Label(motion_frame, text="目标Y位置:", font=demo_font)
    target_y_label.grid(row=3, column=0, sticky=tk.W)
    target_y = ttk.Entry(motion_frame, font=demo_font)
    target_y.grid(row=3, column=1)
    target_y.insert(0, '0.0')

    target_theta_label = ttk.Label(motion_frame, text="目标θ位置:", font=demo_font)
    target_theta_label.grid(row=4, column=0, sticky=tk.W)
    target_theta = ttk.Entry(motion_frame, font=demo_font)
    target_theta.grid(row=4, column=1)
    target_theta.insert(0, '0.0')

    def run_motion_control():
        try:
            speed_value = float(speed.get())
            target_x_value = float(target_x.get())
            target_y_value = float(target_y.get())
            target_theta_value = float(target_theta.get())
            print("视觉演示脚本运行中...")
            walking_sim_demo(speed_value, target_x_value, target_y_value, target_theta_value)
        except ValueError:
            # 这里可以弹出一个错误提示窗口或者设置默认值
            print("请输入有效的速度和目标位置值！")
        return run_motion_control

    run_motion_button = ttk.Button(motion_frame, text="开始运行", style='Custom.TButton', command=run_motion_control)
    run_motion_button.grid(row=5, column=0, columnspan=2)

    # 创建视觉演示部分
    visual_frame = ttk.LabelFrame(root, text="视觉识别足球")
    visual_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    # 配置视觉演示部分的网格权重
    visual_frame.grid_columnconfigure(1, weight=2)
    for i in range(5):  # 假设运动控制部分有五行
        visual_frame.grid_rowconfigure(i, weight=1)

    # 添加说明标签
    visual_demo_label = ttk.Label(visual_frame, text="点击“开始演示”按钮，\n按回车依次查看效果：", font=demo_font, justify='left')
    visual_demo_label.grid(row=0, column=0, sticky='nsew')
    visual_demo_label = ttk.Label(visual_frame, text="1.原始图像", font=demo_font, justify='left')
    visual_demo_label.grid(row=1, column=0, sticky='nsew')
    visual_demo_label = ttk.Label(visual_frame, text="2.灰度图像", font=demo_font, justify='left')
    visual_demo_label.grid(row=2, column=0, sticky='nsew')
    visual_demo_label = ttk.Label(visual_frame, text="3.中值模糊图像", font=demo_font, justify='left')
    visual_demo_label.grid(row=3, column=0, sticky='nsew')
    visual_demo_label = ttk.Label(visual_frame, text="4.识别球体", font=demo_font, justify='left')
    visual_demo_label.grid(row=4, column=0, sticky='nsew')

    # 添加演示视觉程序按钮
    run_visual_button = ttk.Button(visual_frame, text="开始演示", style='Custom.TButton', command=run_visual_demo)
    run_visual_button.grid(row=5, column=0)

    root.mainloop()


# 创建进入页面
intro_window = tk.Tk()
intro_window.title("机器人仿真演示程序")

# 设置窗口大小并居中显示
screen_width = intro_window.winfo_screenwidth()
screen_height = intro_window.winfo_screenheight()
window_width = 768
window_height = 512
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
intro_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
intro_window.resizable(False, False)

# 按钮样式
style = ttk.Style()
style.configure('Custom.TButton', font=demo_font)

# 创建综合介绍的标签
intro_label = tk.Label(intro_window, text=(
"综合演示介绍\n\n"
"欢迎体验我们的机器人课程仿真演示程序。在这个综合演示中，我们将通过两个关键部分来展现机器人的智能能力：运动控制和视觉识别。\n\n"
"演示一：运动控制仿真\n"
"首先，我们将演示机器人的步态规划和运动控制。您将看到一个机器人模型在虚拟环境中接受目标坐标，并根据这些坐标执行平滑的行走动作。\n\n"
"演示二：视觉识别足球\n"
"紧接着，我们会展示机器人的视觉识别能力。通过处理一张含有足球的图片，程序将使用OpenCV库来检测图像中的球体。\n\n"
"现在，让我们开始这一激动人心的演示，一起探索机器人技术的奥妙！"
), justify='left', font=demo_font, wraplength=window_width - 20)
intro_label.pack(pady=20)

# 创建开始按钮
start_button = ttk.Button(intro_window, text="开始演示", style='Custom.TButton', command=open_main_window)
start_button.pack(pady=10)

# 运行初始页面
intro_window.mainloop()